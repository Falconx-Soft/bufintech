from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.core import serializers
from django.contrib.auth.decorators import login_required
from User.models import Api_key

def setCurrentLanguage(request, Language):
    request.session['current_language'] = Language
    return

def index(request, Language):
    display_url = True
    try:
        user_payment = Api_key.objects.get(user = request.user)
    except:
        user_payment = None
    print('user_payment',user_payment)
    if user_payment != None:
        pass
        # return redirect('redirect_index')
    else:
        display_url = False
        # return redirect('payment')
    setCurrentLanguage(request, Language)
    context = {}
    context['display_url'] = display_url
    nav_items = ListPage.objects.filter(Language=request.session['current_language']).order_by('Priority').values_list("Menu_Name","url").distinct()
    context['nav_items'] = list(dict.fromkeys(nav_items))
    context['values'] = table.objects.filter(language=request.session['current_language'])
    context['table_form'] = TableForm()
    context['Language'] = request.session['current_language']
    data = serializers.serialize("python",table.objects.filter(language=request.session['current_language']) )
    context['data'] = data
    context['NewsLetterText'] = NewsLetter.objects.filter(language=request.session['current_language']).values('Sentence')
    print(context['NewsLetterText'])
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        try:
            subscriber = NewsLetterSubscribers.objects.filter(email=email)
            if subscriber:
                context['error'] = "You have already subscribed"
            else:
                NewsLetterSubscribers.objects.create(name=name,email=email,phone=phone)
                context['success'] = True
        except Exception as e:
            context['error'] = str(e)
    return render(request,'base/index.html',context)

def redirect_index(request):
    if "current_language" not in request:
        request.session['current_language'] = "en"
    
    return redirect('index', Language = request.session['current_language'])

def about(request, Language):
    setCurrentLanguage(request, Language)
    nav_items = ListPage.objects.filter(Language=request.session['current_language']).order_by('Priority').values_list("Menu_Name","url").distinct()    
    try:
        obj = aboutus.objects.filter(language = request.session['current_language'])
        data = serializers.serialize("python",aboutus.objects.filter(language= request.session['current_language']) )
        socialmedia = SocialMedia.objects.all()
        return render (request,'base/aboutus.html',{'values':obj,'table_form':AboutusForm(),'data':data, 'SocialMedia': socialmedia, 'nav_items':list(dict.fromkeys(nav_items)),'Language':Language})
    except:
        return render (request,'base/aboutus.html',{'message':"No data found!",'nav_items':list(dict.fromkeys(nav_items)),'Language':Language})

def market_outlook(request, Language):
    display_url = True
    try:
        user_payment = Api_key.objects.get(user = request.user)
    except:
        user_payment = None
    if user_payment != None:
        pass
        # return redirect('redirect_index')
    else:
        display_url = False
    setCurrentLanguage(request, Language)
    nav_items = ListPage.objects.filter(Language=request.session['current_language']).order_by('Priority').values_list("Menu_Name","url").distinct()    
    hidden = [0,6]
    try:
        obj = market.objects.filter(Language = request.session['current_language'])
        data = serializers.serialize("python",market.objects.filter(Language = request.session['current_language']) )
        return render (request,'base/market.html',{'display_url':display_url, 'values':obj,'table_form':MarketForm(),'data':data , 'hidden': hidden, 'nav_items':list(dict.fromkeys(nav_items)),'Language':Language})
    except Exception as e:
        return render (request,'base/market.html',{'display_url':display_url,'message':"No data found!",'nav_items':list(dict.fromkeys(nav_items)),'Language':Language})

def equityView(request, Language):
    display_url = True
    try:
        user_payment = Api_key.objects.get(user = request.user)
    except:
        user_payment = None
    if user_payment != None:
        pass
        # return redirect('redirect_index')
    else:
        display_url = False
    setCurrentLanguage(request, Language)
    hidden = [0,1]
    nav_items = ListPage.objects.filter(Language=request.session['current_language']).order_by('Priority').values_list("Menu_Name","url").distinct()        
    try:
        obj = equity.objects.filter(Language=request.session['current_language'])
        data = serializers.serialize("python",equity.objects.filter(Language=request.session['current_language']) )
        tickers = obj.values('Ticker').distinct()
        return render (request,'base/equity.html',{'display_url':display_url, 'obj':obj,'table_form':EquityForm(),'data':data, 'hidden':hidden,'nav_items':list(dict.fromkeys(nav_items)),'Language':Language, 'tickers': tickers})
    except Exception as e:
        return render (request,'base/equity.html',{'display_url':display_url, 'message':"No data found!",'nav_items':list(dict.fromkeys(nav_items)),'Language':Language})

def money_making(request, Language):
    display_url = True
    try:
        user_payment = Api_key.objects.get(user = request.user)
    except:
        user_payment = None
    if user_payment != None:
        pass
        # return redirect('redirect_index')
    else:
        display_url = False
    setCurrentLanguage(request, Language)
    nav_items = ListPage.objects.filter(Language=request.session['current_language']).order_by('Priority').values_list("Menu_Name","url").distinct() 
    sub_items = ListPage.objects.filter(Language=request.session['current_language'], url="money-making").order_by('-id').values_list("Child_Name").distinct()
    print("############################")
    print(nav_items)
    hidden = [0,1]
    hidden1 = [0,1]
    try:
        obj = money_making_trading.objects.filter(Language=request.session['current_language'])
        data = serializers.serialize("python",money_making_trading.objects.filter(Language=request.session['current_language'] ) )
        plays = obj.values('ReCap').distinct()
        obj1 = money_making_investing.objects.filter(Language=request.session['current_language'] )
        data1 = serializers.serialize("python",money_making_investing.objects.filter(Language=request.session['current_language'] ) )
        companies = obj1.values("Name").distinct()
        return render (request,'base/money_making.html',{'display_url':display_url, 'obj1':obj1,'table_form1':Money_making_investingForm(),'data1':data1,
                                                        'obj':obj,'table_form':Money_making_tradingForm(),'data':data,
                                                        'hidden':hidden, 'hidden1':hidden1, 'nav_items':list(dict.fromkeys(nav_items)),
                                                        'sub_items':sub_items,'Language':Language,
                                                        'companies':companies, 'plays':plays
                                                        })
    except Exception as e:
        return render (request,'base/money_making.html',{'display_url':display_url, 'message':"No data found!","nav_items":list(dict.fromkeys(nav_items)),'sub_items':sub_items,'Language':Language})

def learn(request, Language):
    display_url = True
    try:
        user_payment = Api_key.objects.get(user = request.user)
    except:
        user_payment = None
    if user_payment != None:
        pass
        # return redirect('redirect_index')
    else:
        display_url = False
    hidden = [0,1]
    setCurrentLanguage(request, Language)
    nav_items = ListPage.objects.filter(Language=request.session['current_language']).order_by('Priority').values_list("Menu_Name","url").distinct() 

    obj = learning.objects.filter(Language=request.session['current_language'])
    data = serializers.serialize("python",learning.objects.filter(Language=request.session['current_language']) )
    categories = obj.values("Topic").distinct()
    print("******************************")
    print(categories)
    return render (request,'base/learning.html',{'display_url':display_url, 'obj':obj,'table_form':LearningForm(),'data':data, 'hidden':hidden,"nav_items":list(dict.fromkeys(nav_items)),'Language':Language, 'categories':categories})   

    # try:
    #     obj = learning.objects.filter(Language=request.session['current_language'])
    #     data = serializers.serialize("python",learning.objects.filter(Language=request.session['current_language']) )
    #     categories = obj.values("via").distinct()
    #     print("******************************")
    #     print(obj)
    #     print(data)
    #     return render (request,'base/learning.html',{'display_url':display_url, 'obj':obj,'table_form':LearningForm(),'data':data, 'hidden':hidden,"nav_items":nav_items,'Language':Language, 'categories':categories})
    # except Exception as e:
    #     return render (request,'base/learning.html',{'display_url':display_url, 'message':"No data found!","nav_items":nav_items,'Language':Language})

def list_of_pages(request, Language):
    display_url = True
    try:
        user_payment = Api_key.objects.get(user = request.user)
    except:
        user_payment = None
    if user_payment != None:
        pass
        # return redirect('redirect_index')
    else:
        display_url = False
    setCurrentLanguage(request, Language)
    nav_items = ListPage.objects.filter(Language=request.session['current_language']).values_list("Menu_Name","url").distinct()    

    try:
        obj = ListPage.objects.filter(Language=request.session['current_language'])
        data = serializers.serialize("python",ListPage.objects.filter(Language=request.session['current_language']) )
        return render (request,'base/list_of_pages.html',{'display_url':display_url, 'obj':obj,'table_form':List_of_pagesForm(),'data':data,"nav_items":nav_items,'Language':Language})
    except:
        return render (request,'base/list_of_pages.html',{'display_url':display_url, 'message':"No data found!","nav_items":nav_items,'Language':Language})

def analytic_apps(request, Language):
    display_url = True
    try:
        user_payment = Api_key.objects.get(user = request.user)
    except:
        user_payment = None
    if user_payment != None:
        pass
        # return redirect('redirect_index')
    else:
        display_url = False
    setCurrentLanguage(request, Language)
    nav_items = ListPage.objects.filter(Language=request.session['current_language']).order_by('Priority').values_list("Menu_Name","url").distinct()    
    try:
        obj = analytical_apps_Algo_trader.objects.filter(language = request.session['current_language'])
        systematic_trading_data = serializers.serialize("python",analytical_apps_Algo_trader.objects.filter(language= request.session['current_language']) )

        obj1 = analytical_apps_trade_ideas.objects.filter(language = request.session['current_language'])
        stock_picker_data = serializers.serialize("python",analytical_apps_trade_ideas.objects.filter(language= request.session['current_language']) )

        obj2 = analytical_apps_market_mover.objects.filter(language = request.session['current_language'])
        market_mover_data = serializers.serialize("python",analytical_apps_market_mover.objects.filter(language= request.session['current_language']) )

        obj2 = analytical_apps_prospecting.objects.filter(language = request.session['current_language'])
        company_prospecting_data = serializers.serialize("python",analytical_apps_prospecting.objects.filter(language= request.session['current_language']) )

        return render (request,'base/analytics_apps.html',{
                                                    'display_url':display_url,
                                                    'systematic_trading_data':systematic_trading_data,
                                                    'stock_picker_data':stock_picker_data,
                                                    'market_mover_data':market_mover_data,
                                                    'company_prospecting_data':company_prospecting_data,
                                                    'nav_items':list(dict.fromkeys(nav_items)),
                                                    'Language': Language,
                                                    'analytic_apps':True
                                                })
    except:
        return render (request,'base/analytics_apps.html',{ 'display_url':display_url,'analytic_apps':True, 'message':"No data found!",'nav_items':list(dict.fromkeys(nav_items)),'Language':Language})

def social_networks(request,Language):
    setCurrentLanguage(request, Language)
    nav_items = ListPage.objects.filter(Language=request.session['current_language']).order_by('Priority').values_list("Menu_Name","url").distinct()    
    try:
        obj = social_network.objects.filter(language = request.session['current_language'])
        data = serializers.serialize("python",social_network.objects.filter(language= request.session['current_language']) )
        return render (request,'base/social_network.html',{'values':obj,'table_form':social_networkForm(),'data':data, 'nav_items':list(dict.fromkeys(nav_items)),'Language':Language})
    except:
        return render (request,'base/social_network.html',{'message':"No data found!",'nav_items':list(dict.fromkeys(nav_items)),'Language':Language})


def algo_trader(request,Language):
    display_url = True
    try:
        user_payment = Api_key.objects.get(user = request.user)
    except:
        user_payment = None
    if user_payment != None:
        pass
        # return redirect('redirect_index')
    else:
        display_url = False
    setCurrentLanguage(request, Language)
    nav_items = ListPage.objects.filter(Language=request.session['current_language']).order_by('Priority').values_list("Menu_Name","url").distinct()    
    try:
        obj = analytical_apps_Algo_trader.objects.filter(language = request.session['current_language'])
        systematic_trading_data = serializers.serialize("python",analytical_apps_Algo_trader.objects.filter(language= request.session['current_language']) )

        obj1 = analytical_apps_trade_ideas.objects.filter(language = request.session['current_language'])
        stock_picker_data = serializers.serialize("python",analytical_apps_trade_ideas.objects.filter(language= request.session['current_language']) )

        obj2 = analytical_apps_market_mover.objects.filter(language = request.session['current_language'])
        market_mover_data = serializers.serialize("python",analytical_apps_market_mover.objects.filter(language= request.session['current_language']) )

        obj2 = analytical_apps_prospecting.objects.filter(language = request.session['current_language'])
        company_prospecting_data = serializers.serialize("python",analytical_apps_prospecting.objects.filter(language= request.session['current_language']) )

        return render (request,'base/analytics_apps.html',{
                                                    'display_url':display_url,
                                                    'systematic_trading_data':systematic_trading_data,
                                                    'stock_picker_data':stock_picker_data,
                                                    'market_mover_data':market_mover_data,
                                                    'company_prospecting_data':company_prospecting_data,
                                                    'nav_items':list(dict.fromkeys(nav_items)),
                                                    'Language': Language,
                                                    'analytic_apps':True,
                                                    'name':"AlgoTrader"
                                                })
    except:
        return render (request,'base/analytics_apps.html',{ 'display_url':display_url,'analytic_apps':True, 'message':"No data found!",'nav_items':list(dict.fromkeys(nav_items)),'Language':Language,'name':"AlgoTrader"})

def trade_ideas(request,Language):
    display_url = True
    try:
        user_payment = Api_key.objects.get(user = request.user)
    except:
        user_payment = None
    if user_payment != None:
        pass
        # return redirect('redirect_index')
    else:
        display_url = False
    setCurrentLanguage(request, Language)
    nav_items = ListPage.objects.filter(Language=request.session['current_language']).order_by('Priority').values_list("Menu_Name","url").distinct()    
    try:
        obj = analytical_apps_Algo_trader.objects.filter(language = request.session['current_language'])
        systematic_trading_data = serializers.serialize("python",analytical_apps_Algo_trader.objects.filter(language= request.session['current_language']) )

        obj1 = analytical_apps_trade_ideas.objects.filter(language = request.session['current_language'])
        stock_picker_data = serializers.serialize("python",analytical_apps_trade_ideas.objects.filter(language= request.session['current_language']) )

        obj2 = analytical_apps_market_mover.objects.filter(language = request.session['current_language'])
        market_mover_data = serializers.serialize("python",analytical_apps_market_mover.objects.filter(language= request.session['current_language']) )

        obj2 = analytical_apps_prospecting.objects.filter(language = request.session['current_language'])
        company_prospecting_data = serializers.serialize("python",analytical_apps_prospecting.objects.filter(language= request.session['current_language']) )

        return render (request,'base/analytics_apps.html',{
                                                    'display_url':display_url,
                                                    'systematic_trading_data':systematic_trading_data,
                                                    'stock_picker_data':stock_picker_data,
                                                    'market_mover_data':market_mover_data,
                                                    'company_prospecting_data':company_prospecting_data,
                                                    'nav_items':list(dict.fromkeys(nav_items)),
                                                    'Language': Language,
                                                    'analytic_apps':True,
                                                    'name':"TradeIdeas"
                                                })
    except:
        return render (request,'base/analytics_apps.html',{ 'display_url':display_url,'analytic_apps':True, 'message':"No data found!",'nav_items':list(dict.fromkeys(nav_items)),'Language':Language,'name':"TradeIdeas"})

def market_mover(request,Language):
    display_url = True
    try:
        user_payment = Api_key.objects.get(user = request.user)
    except:
        user_payment = None
    if user_payment != None:
        pass
        # return redirect('redirect_index')
    else:
        display_url = False
    setCurrentLanguage(request, Language)
    nav_items = ListPage.objects.filter(Language=request.session['current_language']).order_by('Priority').values_list("Menu_Name","url").distinct()    
    try:
        obj = analytical_apps_Algo_trader.objects.filter(language = request.session['current_language'])
        systematic_trading_data = serializers.serialize("python",analytical_apps_Algo_trader.objects.filter(language= request.session['current_language']) )

        obj1 = analytical_apps_trade_ideas.objects.filter(language = request.session['current_language'])
        stock_picker_data = serializers.serialize("python",analytical_apps_trade_ideas.objects.filter(language= request.session['current_language']) )

        obj2 = analytical_apps_market_mover.objects.filter(language = request.session['current_language'])
        market_mover_data = serializers.serialize("python",analytical_apps_market_mover.objects.filter(language= request.session['current_language']) )

        obj2 = analytical_apps_prospecting.objects.filter(language = request.session['current_language'])
        company_prospecting_data = serializers.serialize("python",analytical_apps_prospecting.objects.filter(language= request.session['current_language']) )

        return render (request,'base/analytics_apps.html',{
                                                    'display_url':display_url,
                                                    'systematic_trading_data':systematic_trading_data,
                                                    'stock_picker_data':stock_picker_data,
                                                    'market_mover_data':market_mover_data,
                                                    'company_prospecting_data':company_prospecting_data,
                                                    'nav_items':list(dict.fromkeys(nav_items)),
                                                    'Language': Language,
                                                    'analytic_apps':True,
                                                    'name':"MarketMover"
                                                })
    except:
        return render (request,'base/analytics_apps.html',{ 'display_url':display_url,'analytic_apps':True, 'message':"No data found!",'nav_items':list(dict.fromkeys(nav_items)),'Language':Language,'name':"MarketMover"})

def prospecting(request,Language):
    display_url = True
    try:
        user_payment = Api_key.objects.get(user = request.user)
    except:
        user_payment = None
    if user_payment != None:
        pass
        # return redirect('redirect_index')
    else:
        display_url = False
    setCurrentLanguage(request, Language)
    nav_items = ListPage.objects.filter(Language=request.session['current_language']).order_by('Priority').values_list("Menu_Name","url").distinct()    
    try:
        obj = analytical_apps_Algo_trader.objects.filter(language = request.session['current_language'])
        systematic_trading_data = serializers.serialize("python",analytical_apps_Algo_trader.objects.filter(language= request.session['current_language']) )

        obj1 = analytical_apps_trade_ideas.objects.filter(language = request.session['current_language'])
        stock_picker_data = serializers.serialize("python",analytical_apps_trade_ideas.objects.filter(language= request.session['current_language']) )

        obj2 = analytical_apps_market_mover.objects.filter(language = request.session['current_language'])
        market_mover_data = serializers.serialize("python",analytical_apps_market_mover.objects.filter(language= request.session['current_language']) )

        obj2 = analytical_apps_prospecting.objects.filter(language = request.session['current_language'])
        company_prospecting_data = serializers.serialize("python",analytical_apps_prospecting.objects.filter(language= request.session['current_language']) )

        return render (request,'base/analytics_apps.html',{
                                                    'display_url':display_url,
                                                    'systematic_trading_data':systematic_trading_data,
                                                    'stock_picker_data':stock_picker_data,
                                                    'market_mover_data':market_mover_data,
                                                    'company_prospecting_data':company_prospecting_data,
                                                    'nav_items':list(dict.fromkeys(nav_items)),
                                                    'Language': Language,
                                                    'analytic_apps':True,
                                                    'name':"Prospecting"
                                                })
    except:
        return render (request,'base/analytics_apps.html',{ 'display_url':display_url,'analytic_apps':True, 'message':"No data found!",'nav_items':list(dict.fromkeys(nav_items)),'Language':Language,'name':"Prospecting"})