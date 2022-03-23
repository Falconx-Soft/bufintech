from django.db import models
from django.contrib.auth import backends, get_user_model
from django.contrib.auth.models import User
# Create your models here.


class Api_key(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    paymentMenthod = models.CharField(max_length=150)
    customer_Id = models.CharField(max_length=150)
    subscription_ID = models.CharField(max_length=150)
    verification_id = models.CharField(verbose_name="Stripe Verification Session ID", blank=True, null=True, default="0", max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class accountsCheck(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    crated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class paymentMethod(models.Model):
    payment_type = models.CharField(max_length=100)
    method = models.CharField(max_length=10000)
    amount = models.IntegerField(default=0)
    description = models.CharField(max_length=10000,blank=True,null=True)

    def __str__(self):
        return self.payment_type

class oneTimePayment(models.Model):
    amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.amount)
