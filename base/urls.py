from django.urls import path, re_path

from . import views

urlpatterns = [ 
    path('', views.redirect_index, name='redirect_index'),
    re_path(r'^(?P<Language>[a-z]{2})$', views.index, name='index'),
    re_path(r'^(?P<Language>[a-z]{2})/about-us$', views.about, name='about'),
    re_path(r'^(?P<Language>[a-z]{2})/market-outlook$', views.market_outlook, name='market_outlook'),
    re_path(r'^(?P<Language>[a-z]{2})/equity-research$', views.equityView, name='equity'),
    re_path(r'^(?P<Language>[a-z]{2})/learning-center$', views.learn, name='learn'),
    re_path(r'^(?P<Language>[a-z]{2})/money-making$', views.money_making, name='money_making'),
    re_path(r'^(?P<Language>[a-z]{2})/list-of-pages$', views.list_of_pages, name='list_of_pages'),
    re_path(r'^(?P<Language>[a-z]{2})/analytical-applications$', views.analytic_apps, name='analytic_apps'),
    re_path(r'^(?P<Language>[a-z]{2})/social_network$', views.social_network, name='social_network'),
]