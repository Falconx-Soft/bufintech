from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources

#NewLetterSubscribe
class NewsLetterSubscribersResource(resources.ModelResource):

    class Meta:
        model = NewsLetterSubscribers

class NewsLetterSubscribersAdmin(ImportExportModelAdmin):
    resource_class = NewsLetterSubscribersResource


#Table
class TableResource(resources.ModelResource):

    class Meta:
        model = table

class TableAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('Platform', 'Username', 'url','language')
    resource_class = TableResource


#Analytics Apps Systematic Trading
class AnalyticsAppsSystematicTradResource(resources.ModelResource):

    class Meta:
        model = analytical_apps_Algo_trader

class AnalyticsAppsSystematicTradAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('Sentence', 'language')
    resource_class = AnalyticsAppsSystematicTradResource

#Analytics Apps Company Prospecting
class AnalyticsAppsCompanyProspecting(resources.ModelResource):

    class Meta:
        model = analytical_apps_prospecting

class AnalyticsAppsCompanyProspectingAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('Sentence', 'language')
    resource_class = AnalyticsAppsCompanyProspecting
    
    
#Analytics Apps Stock Picker
class AnalyticsAppsStockPickerResource(resources.ModelResource):

    class Meta:
        model = analytical_apps_trade_ideas

class AnalyticsAppsStockPickerAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('Sentence', 'language')
    resource_class = AnalyticsAppsStockPickerResource


#Analytics Apps Market Mover   
class AnalyticsAppsMarketMoverResource(resources.ModelResource):

    class Meta:
        model = analytical_apps_market_mover

class AnalyticsAppsMarketMoverAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('Sentence', 'language')
    resource_class = AnalyticsAppsMarketMoverResource    

#Equity
class EquityResource(resources.ModelResource):

    class Meta:
        model = equity


class EquityAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('Product', 'Language', 'Market','Date','Ticker' ,'Description', 'Research', 'Youtube', 'Podcast')
    resource_class = EquityResource 

#Learning
class LearningResource(resources.ModelResource):

    class Meta:
        model = learning

class LearningAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('Product', 'Language', 'Topic','Class','Date', 'Description', 'Research', 'Youtube', 'Podcast')
    resource_class = LearningResource
#Market

class MarketResource(resources.ModelResource):

    class Meta:
        model = market
 
class MarketResource(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('Product', 'Language', 'Country','Date', 'Description', 'Research', 'YouTube', 'Podcast')
    resource_class = MarketResource
        

#Market
class MoneyInvestingResource(resources.ModelResource):

    class Meta:
        model = money_making_investing


class MoneyInvestingAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('Product', 'Language', 'Market','Entry_Date', 'Ticker', 'Name','Exit_Date','Position','Outcome','Initial_Inv','ROI' ,'ReCap', 'Youtube', 'Podcast')
    resource_class = MoneyInvestingResource

#Market
class MoneyTradingResource(resources.ModelResource):

    class Meta:
        model = money_making_trading

class MoneyTradingAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('Product', 'Language', 'Class','Trade_Date', 'Identifier', 'Outcome','Initial_Inv','ROI','ReCap', 'Youtube', 'Podcast')
    resource_class = MoneyTradingResource

#Market
class AboutResource(resources.ModelResource):

    class Meta:
        model = aboutus

#About
class AboutAdmin(ImportExportModelAdmin):
    resource_class = AboutResource


class ListPageResource(resources.ModelResource):

    class Meta:
        model = ListPage

class ListPageAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('Menu_Name', 'Child_Name', 'Main_Child','url', 'Language','Priority')
    resource_class = ListPageResource
    
class SocialMediaResource(resources.ModelResource):

    class Meta:
        model = SocialMedia

class SocialMediaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('link', 'image', 'name','height', 'width')
    resource_class = SocialMediaResource

class SocialNetworkResource(resources.ModelResource):

    class Meta:
        model = social_network

class SocialNetworkAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('Sentence', 'language')
    resource_class = SocialNetworkResource

admin.site.register(table, TableAdmin)
admin.site.register(NewsLetter)
admin.site.register(market,MarketResource)
admin.site.register(equity, EquityAdmin)
admin.site.register(learning,LearningAdmin)
admin.site.register(money_making_investing,MoneyInvestingAdmin)
admin.site.register(money_making_trading,MoneyTradingAdmin)
admin.site.register(aboutus, AboutAdmin)
admin.site.register(ListPage, ListPageAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(NewsLetterSubscribers, NewsLetterSubscribersAdmin)
admin.site.register(analytical_apps_market_mover, AnalyticsAppsMarketMoverAdmin)
admin.site.register(analytical_apps_trade_ideas, AnalyticsAppsStockPickerAdmin)
admin.site.register(analytical_apps_Algo_trader, AnalyticsAppsSystematicTradAdmin)
admin.site.register(analytical_apps_prospecting, AnalyticsAppsCompanyProspectingAdmin)
admin.site.register(social_network, SocialNetworkAdmin)


