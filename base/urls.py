from django.urls import path, re_path

from . import views

urlpatterns = [ 
    path('', views.redirect_index, name='redirect_index'),
    re_path(r'^(?P<Language>[a-z]{2})$', views.index, name='index'),
    re_path(r'^(?P<Language>[a-z]{2})/about-us$', views.about, name='about-us'),
    re_path(r'^(?P<Language>[a-z]{2})/market-outlook$', views.market_outlook, name='market-outlook'),
    re_path(r'^(?P<Language>[a-z]{2})/equity-research$', views.equityView, name='equity-research'),
    re_path(r'^(?P<Language>[a-z]{2})/learning-center$', views.learn, name='learning-center'),
    re_path(r'^(?P<Language>[a-z]{2})/money-making$', views.money_making, name='money-making'),
    re_path(r'^(?P<Language>[a-z]{2})/list-of-pages$', views.list_of_pages, name='list_of_pages'),
    re_path(r'^(?P<Language>[a-z]{2})/analytical-apps$', views.analytic_apps, name='analytical-apps'),
    re_path(r'^(?P<Language>[a-z]{2})/social-network$', views.social_networks, name='social-network'),
]