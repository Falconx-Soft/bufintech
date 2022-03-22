from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Api_key)

admin.site.register(accountsCheck)


class paymentMethodAdmin(admin.ModelAdmin):
	list_display = ('payment_type','method','amount')
admin.site.register(paymentMethod,paymentMethodAdmin)


admin.site.register(oneTimePayment)