from django.contrib import admin
from django.urls import path, re_path

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.loginUser, name="login"),
	path('register/', views.register, name="register"),
	path('logout/', views.logoutUser, name="logout"),
      # Payment urls
	path('payment/', views.Payment, name="payment"),
      path('complete', views.completePayment, name='complete'),
      # card update

      path('add_card', views.add_card, name="add_card"),

      re_path(r'^delete_payment/(?P<id>\w+)/$', views.delete_payment, name="delete_payment"),
      re_path(r'^make_default/(?P<id>\w+)/$', views.make_default, name="make_default"),
      # Payment urls end
	path('reset_password/', auth_views.PasswordResetView.as_view(template_name="User/restPassword/restPassword.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="User/restPassword/passwordRestSend.html"),
          name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="User/restPassword/newPssword.html"),
          name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="User/restPassword/passwordResetComplete.html"),
          name="password_reset_complete"),

      path('verify/<auth_token>', views.verify, name="verify"),

      path('profile/', views.Profile , name = "profile")
]
