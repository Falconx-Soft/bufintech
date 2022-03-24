from email import message
from multiprocessing import context
from pydoc import plain
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CutomUserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
# Create your views here.
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe, json
from base.views import setCurrentLanguage
from django.urls import reverse
import uuid
from django.core.mail import send_mail

stripe.api_key = settings.STRIPE_SECRET_KEY

def loginUser(request):
	# setCurrentLanguage(request, Language)
	if request.user.is_authenticated:
		try:
			user_payment = Api_key.objects.get(user = request.user)
		except:
			user_payment = None
		print('user_payment',user_payment)
		if user_payment != None:
			return redirect('redirect_index')
		else:
			# return redirect('payment')
			return redirect('redirect_index')
	msg = None
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		try:
			user = User.objects.get(username=username)
			user = authenticate(request, username=username, password=password) # check password

			if user is not None and accountsCheck.objects.get(user=user).is_verified:
				login(request, user)
				try:
					user_payment = Api_key.objects.get(user = request.user)
				except:
					user_payment = None
				print('user_payment',user_payment)
				if user_payment != None:
					return redirect('redirect_index')
				else:
					# return redirect('payment')
					return redirect('redirect_index')
			else:
				msg = 'User/Something is wrong'
		except:
			msg = 'User not recognized / verified.'
	if "current_language" not in request:
		request.session['current_language'] = "en"
		Language = request.session['current_language']
	context = {
		'msg':msg,
		'Language':Language
	}
	return render(request,'User/login.html',context)

def Sign_Up(request):
	msg = None
	form = CutomUserCreationForm
	if request.method == 'POST':
		form = CutomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			# user.username = user.username.lower()
			user.save()
			
			auth_token = str(uuid.uuid4())
			accountsCheck_obj = accountsCheck.objects.create(user=user, auth_token = auth_token)
			accountsCheck_obj.save()

			verificationMain(user.email,auth_token,request)
			msg = 'Varification link has send to your mail id. Kindly verify your account.'
			context = {'form':form, 'msg':msg}
			return render(request,'User/SignUp.html', context)
			
		else:
			msg = 'Error.'
	context = {'form':form, 'msg':msg}
	return render(request,'User/SignUp.html', context)

def verificationMain(email, auth_token,request):
	subject = 'Please verify your account'
	message = f'Hi please click on the link to verify your account {request.build_absolute_uri()}verify/{auth_token}'
	email_from = settings.EMAIL_HOST_USER
	recipient_list = [email]
	send_mail(subject,message,email_from, recipient_list)

def verify(request, auth_token):
	accountsCheck_obj = accountsCheck.objects.get(auth_token = auth_token)
	if accountsCheck:
		accountsCheck_obj.is_verified = True
		accountsCheck_obj.save()
		return redirect('login')

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def Profile(request):
	customer = None
	invoice  = None
	invoices = None
	upcoming = []
	profile = None
	card=None
	c = None
	n = None
	try:
		customer = Api_key.objects.filter(user=request.user)
		if len(customer) != 0:
			card = stripe.PaymentMethod.list(
				customer=customer[0].customer_Id,
				type="card",
				)
			c = stripe.Customer.retrieve(customer[0].customer_Id)
			customer = customer[0]
			invoice = stripe.Invoice.list(customer = customer.customer_Id)
			invoices = (invoice.data)
			s = stripe.Subscription.list(customer = customer.customer_Id)
			for i in s:
				upcoming.append(stripe.Invoice.upcoming( subscription = i.id))
			print('\ninvoices',invoices)
			print('\nupcoming,upcoming',upcoming)
			

	except Exception as e:
		print('exception pro',e)
	context={
		'upcoming': upcoming, 
		'invoices': invoices, 
		'customer': customer, 
		"payment_tab" : True, 
		'card': card, 
		'profile' : profile,
		'c' : c,
		'n' : n
	}
	return render(request,'User/profile.html', context= context)


# Stripe payment
@login_required(login_url='login')
def Payment(request):
	total_amount = 10
	monthlyPayment = paymentMethod.objects.get(payment_type="monthly")
	yearlyPayment = paymentMethod.objects.get(payment_type="yearly")
	oneTimePaymentAmonut = oneTimePayment.objects.all()[0].amount
	customer = ''
	try:

		# ! If customer is old and only have one instance...
		customer = Api_key.objects.get(
			user = User.objects.get(username = request.user.username)
		)
	# ! If Customer is brand new...
	except Api_key.DoesNotExist:
		try:
			customer = stripe.Customer.create(
				# payment_method=stripe.PaymentMethod.retrieve(paymentMethod),
				email=request.user.email,
				description='About Payment Plan',
				name=request.user.get_full_name(),
				
			)
		except Exception as e:
			print('cannot create stripe customer',e)
	# ! If customer is old and have multiple instances...
	except Api_key.MultipleObjectsReturned:
		customer = Api_key.objects.filter(user=request.user)[0]
	except Exception as e:
		print('api key issue')
		
	# if(isinstance(customer, Api_key) is True):
	# 	print('instance exists')
	# 	return redirect('redirect_index')
	context = {
		'monthlyPayment':monthlyPayment,
		'yearlyPayment':yearlyPayment,
		'oneTimePaymentAmonut':oneTimePaymentAmonut
	}
	return render(request,'User/payment.html', context)


@csrf_exempt
def completePayment(request):
	print('Request\n', request.GET)
	paymentMethodTmp = request.POST.get('payment_method')
	monthly = request.POST.get('monthly')
	yearly = request.POST.get('yearly')

	monthlyPayment = paymentMethod.objects.get(payment_type="monthly")
	yearlyPayment = paymentMethod.objects.get(payment_type="yearly")
	oneTimePaymentobj = oneTimePayment.objects.all()

	print('\n', paymentMethod, monthly,yearly)
	plans_products_list_ID=settings.PRODUCT_LIST_IDS
	if monthly == 'true':
		plan = monthlyPayment.method
	elif yearly == 'true':
		plan = yearlyPayment.method
		print('yearly')
	else:
		plan = monthlyPayment.method
	try:
		num_results = Api_key.objects.filter(user=request.user).count()

		if num_results > 0:
			prev_data = Api_key.objects.get(user=request.user)
			stripe.Subscription.delete(
				prev_data.subscription_ID,
				)
			prev_data.delete()
			print("Data deleted*********************")
		customer = stripe.Customer.create(
				payment_method=stripe.PaymentMethod.retrieve(paymentMethodTmp),
				email=request.user.email,
				description='About Payment Plan',


				invoice_settings={
							'default_payment_method': paymentMethodTmp
					}
		)
		subscription_pay = stripe.Subscription.create(
			customer=customer.id,
			expand=['latest_invoice.payment_intent'],
			items=[
				{
				'plan': plan,
				},
			],
		)
		
		try:
			Intent = stripe.PaymentIntent.create(amount=oneTimePaymentobj[0].amount*100, #in 
							currency="usd",
							payment_method=paymentMethodTmp,
							description = "one time payment",  #text 
							customer= customer.id
							)
			stripe.PaymentIntent.confirm(
							Intent,
							payment_method=paymentMethodTmp,
							)
		except Exception as error:
			print(error,"***************stripe error")

		Api_key.objects.create(
						user=request.user,
						paymentMenthod=paymentMethodTmp, 
						customer_Id=customer.id,
						subscription_ID=subscription_pay.id
					)
		return JsonResponse(json.loads( json.dumps( {"success":"Subscription is created", "stripe_error" : False})),status=200)
	except:
		return JsonResponse(json.loads( json.dumps( {"error":"Subscription is not created", "stripe_error" : False})), status=400)

# Add a new payment method (Stripe API)
@csrf_exempt
def add_card(request):
	try:
		customer = Api_key.objects.get(user=request.user)
	except:
		return redirect('payment')
	if request.method == 'POST':
		data = json.loads(request.body)
		find_eq = True
		paymentMethod = data['payment_method']
		card = data['card']
		# print("data['phone']",data['phone'])
		details = data['details']
		# print(data["default"])
		default_card = data["default"]
		print('data'*10,data)
		# template_name="payment/paymentupdate.html"
		# context={
		# }
		# return render(request, template_name, context)
		try:
			customer = Api_key.objects.get(user=request.user)
			# print(stripe.PaymentMethod.list(customer=customer.customer_Id,type="card",))
			list_cards = stripe.PaymentMethod.list(
				customer=customer.customer_Id,
				type="card",
			)
			print('list_cards', list_cards)
			new_fingerprint = stripe.PaymentMethod.retrieve(paymentMethod).card.fingerprint
			for i in list_cards:
				if i.card.fingerprint ==  new_fingerprint:
					find_eq = False
					break

			# print()
			# finger_1 = stripe.PaymentMethod.retrieve(customer.paymentMenthod).card.fingerprint
			# finger_2 = stripe.PaymentMethod.retrieve(paymentMethod).card.fingerprint
			# new card 
			if find_eq:
				if default_card:
					stripe.PaymentMethod.attach(
						paymentMethod,
						customer=customer.customer_Id,
						# invoice_settings={'default_payment_method': paymentMethod},
					)
					stripe.Customer.modify(
						customer.customer_Id,
						invoice_settings={'default_payment_method': paymentMethod}
					)
				else:
					stripe.PaymentMethod.attach(
					paymentMethod,
					customer=customer.customer_Id,
				)
			else:
				messages.info(request, "Requested Payment Method has already existed in your payment method list.")
		
		except Api_key.MultipleObjectsReturned:
			print('e1')
			customer = Api_key.objects.filter(user=request.user)[0]
			# finger_1 = stripe.PaymentMethod.retrieve(customer.paymentMenthod).card.fingerprint
			# finger_2 = stripe.PaymentMethod.retrieve(paymentMethod).card.fingerprint
			list_cards = stripe.PaymentMethod.list(
				customer=customer.customer_Id,
				type="card",
			)
			new_fingerprint = stripe.PaymentMethod.retrieve(paymentMethod).card.fingerprint
			for i in list_cards:
				if i.card.fingerprint ==  new_fingerprint:
					find_eq = False
					break
			if find_eq:
				if default_card:
					stripe.PaymentMethod.attach(
						paymentMethod,
						customer=customer[0].customer_Id,
						# invoice_settings={'default_payment_method': paymentMethod},
					)
					stripe.Customer.modify(
						customer.customer_Id,
						invoice_settings={'default_payment_method': paymentMethod}
					)
				else:
					stripe.PaymentMethod.attach(
					paymentMethod,
					customer=customer[0].customer_Id,
				)
			else:
				messages.info(request, "Requested Payment Method has already existed in your payment method list")
		except Exception as e:
			print(e)
			msg = "Please make a payment first"
			messages.info(request, str(msg))
			return redirect('payment')
	template_name="User/payment/paymentupdate.html"
	context={
	}
	return render(request, template_name, context)

# ? Make an existing payment method as default (Stripe API)
def make_default(request, id):
	try:
		customer = Api_key.objects.filter(user=request.user)
		if len(customer) != 0:
			customer = customer[0]
			stripe.Customer.modify(
				customer.customer_Id,
				invoice_settings={'default_payment_method': id}
			)
		else:
			customer  = None
			card =None
	except Exception as e:
		print(e)
		messages.info(request, str(e))
		return redirect("profile")
	return redirect("profile")

# ?	Delete an existing payment method (Stripe API)
@login_required
def delete_payment(request, id):
	try:
		customer = Api_key.objects.get(user=request.user)
		p =stripe.PaymentMethod.list(
			customer=customer.customer_Id,
			type="card",
		)
		if len(p) == 1:
			msg = "Please add another default card before deleting this one."
			messages.info(request, str(msg))
		else:
			stripe.PaymentMethod.detach(id)
			msg = "Successfully deleted"
			messages.info(request, str(msg))
	except Api_key.DoesNotExist:
		msg = "Invalid Request. Payment Method to that customer does not exists."
		messages.info(request, str(msg))
	except Api_key.MultipleObjectsReturned:
		customer = Api_key.objects.filter(user=request.user)[0]
	except Exception as e:
		msg = "Invalid Request"
		messages.info(request, str(msg))

	return redirect("profile")

# Stripe payment end