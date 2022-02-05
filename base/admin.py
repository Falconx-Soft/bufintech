from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources

#NewLetterSubscribe
class NewsLetterSubscribeResource(resources.ModelResource):

    class Meta:
        model = NewsLetterSubscribe

class NewsLetterSubscribeAdmin(ImportExportModelAdmin):
    resource_class = NewsLetterSubscribeResource


#Table
class TableResource(resources.ModelResource):

    class Meta:
        model = table

class TableAdmin(ImportExportModelAdmin):
    resource_class = TableResource



#Analytics Apps Systematic Trading
class AnalyticsAppsSystematicTradResource(resources.ModelResource):

    class Meta:
        model = analytics_apps_systematic_trad

class AnalyticsAppsSystematicTradAdmin(ImportExportModelAdmin):
    resource_class = AnalyticsAppsSystematicTradResource

#Analytics Apps Company Prospecting
class AnalyticsAppsCompanyProspecting(resources.ModelResource):

    class Meta:
        model = analytics_apps_company_prospecting

class AnalyticsAppsCompanyProspectingAdmin(ImportExportModelAdmin):
    resource_class = AnalyticsAppsCompanyProspecting
    
    
#Analytics Apps Stock Picker
class AnalyticsAppsStockPickerResource(resources.ModelResource):

    class Meta:
        model = analytics_apps_stock_picker

class AnalyticsAppsStockPickerAdmin(ImportExportModelAdmin):
    resource_class = AnalyticsAppsStockPickerResource


#Analytics Apps Market Mover   
class AnalyticsAppsMarketMoverResource(resources.ModelResource):

    class Meta:
        model = analytics_apps_market_mover

class AnalyticsAppsMarketMoverAdmin(ImportExportModelAdmin):
    resource_class = AnalyticsAppsMarketMoverResource    

#Equity
class EquityResource(resources.ModelResource):

    class Meta:
        model = equity

class EquityAdmin(admin.ModelAdmin):
    list_display = ('Product', 'Language', 'Market','Date','Ticker' ,'Description', 'Research', 'Youtube', 'Podcast')

#Learning
class LearningResource(resources.ModelResource):

    class Meta:
        model = learning

class LearningAdmin(admin.ModelAdmin):
    list_display = ('Product', 'Language', 'Topic','Class','Date', 'Description', 'Research', 'Youtube', 'Podcast')

#Market
class MarketResource(admin.ModelAdmin):
    list_display = ('Product', 'Language', 'Country','Date', 'Description', 'Research', 'YouTube', 'Podcast')
        

# class MarketAdmin(ImportExportModelAdmin):
#     resource_class = MarketResource

#Market
class MoneyInvestingResource(resources.ModelResource):

    class Meta:
        model = money_making_investing


class MoneyInvestingAdmin(admin.ModelAdmin):
    list_display = ('Product', 'Language', 'Market','Entry_Date', 'Ticker', 'Name','Exit_Date','Position','Outcome','Initial_Inv','ROI' ,'ReCap', 'Youtube', 'Podcast')

#Market
class MoneyTradingResource(resources.ModelResource):

    class Meta:
        model = money_making_trading

class MoneyTradingAdmin(admin.ModelAdmin):
    list_display = ('Product', 'Language', 'Class','Trade_Date', 'Identifier', 'Outcome','Initial_Inv','ROI','ReCap', 'Youtube', 'Podcast')
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

class ListPageAdmin(admin.ModelAdmin):
    list_display = ('Menu_Name', 'Child_Name', 'Main_Child','url', 'Language')
    
class SocialMediaResource(resources.ModelResource):

    class Meta:
        model = SocialMedia
class SocialMediaAdmin(ImportExportModelAdmin):
    resource_class = SocialMediaResource

admin.site.register(table, TableAdmin)
admin.site.register(newsletter)
admin.site.register(market,MarketResource)
admin.site.register(equity, EquityAdmin)
admin.site.register(learning,LearningAdmin)
admin.site.register(money_making_investing,MoneyInvestingAdmin)
admin.site.register(money_making_trading,MoneyTradingAdmin)
admin.site.register(aboutus, AboutAdmin)
admin.site.register(ListPage, ListPageAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(NewsLetterSubscribe, NewsLetterSubscribeAdmin)
admin.site.register(analytics_apps_market_mover, AnalyticsAppsMarketMoverAdmin)
admin.site.register(analytics_apps_stock_picker, AnalyticsAppsStockPickerAdmin)
admin.site.register(analytics_apps_systematic_trad, AnalyticsAppsSystematicTradAdmin)
admin.site.register(analytics_apps_company_prospecting, AnalyticsAppsCompanyProspectingAdmin)
admin.site.register(social_network)


