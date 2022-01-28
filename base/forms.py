from django.forms import ModelForm
from .models import *


class TableForm(ModelForm):
    class Meta:
        model=table
        fields = '__all__'

class AboutusForm(ModelForm):
    class Meta:
        model = aboutus
        fields = '__all__'

class MarketForm(ModelForm):
    class Meta:
        model = market
        fields = '__all__'

class EquityForm(ModelForm):
    class Meta:
        model = equity
        fields = '__all__'

class LearningForm(ModelForm):
    class Meta:
        model = learning
        fields = '__all__'

class Money_making_tradingForm(ModelForm):
    class Meta:
        model = money_making_trading
        fields = '__all__'

class Money_making_investingForm(ModelForm):
    class Meta:
        model = money_making_investing
        fields = '__all__'

class List_of_pagesForm(ModelForm):
    class Meta:
        model = ListPage
        fields = '__all__'

class social_networkForm(ModelForm):
    class Meta:
        model = social_network
        fields = '__all__'