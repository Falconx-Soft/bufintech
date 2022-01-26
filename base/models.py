from django.db import models

class table(models.Model):
    Platform = models.CharField(verbose_name='name',max_length=50,blank=True)
    Clickable = models.CharField(max_length=50,blank=True)
    url = models.URLField()
    language = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Home"

class newsletter(models.Model):
    name = models.CharField(max_length=255,blank=True)
    email = models.CharField(max_length=255,unique=True)
    phone = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Subscribers List"
        verbose_name_plural = "Subscribers List"

class aboutus(models.Model):
    Sentence = models.TextField(blank=True)
    language = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"

class analytics_apps_systematic_trad(models.Model):
    Sentence = models.TextField(blank=True)
    language = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = "Analytics Apps Systematic Trader"
        verbose_name_plural = "Analytics Apps Systematic Trader"

class analytics_apps_company_prospecting(models.Model):
    Sentence = models.TextField(blank=True)
    language = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = "Analytics Apps Company Prospecting"
        verbose_name_plural = "Analytics Apps Company Prospecting"


class analytics_apps_stock_picker(models.Model):
    Sentence = models.TextField(blank=True)
    language = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = "Analytics Apps Stock Picker"
        verbose_name_plural = "Analytics Apps Stock Picker"

class analytics_apps_market_mover(models.Model):
    Sentence = models.TextField(blank=True)
    language = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = "Analytics Apps Market Mover"
        verbose_name_plural = "Analytics Apps Market Mover"

      

def market_path(instance, filename):
    return '{0}/market-outlook/{1}/{2}/{3}'.format(instance.Language,instance.SubCategory.lower(), instance.Date.strftime('%Y%m%d'), filename)

class market(models.Model):
    Date_Language = models.CharField(max_length=50,blank=True)
    Date = models.DateField()
    Product = models.CharField(max_length=50,blank=True)
    Region = models.CharField(max_length=50,blank=True)
    FileName = models.CharField(max_length=50,blank=True)
    Description = models.CharField(max_length=500,blank=True)
    Research = models.FileField(upload_to=market_path)
    YouTube = models.CharField(max_length=50,blank=True)
    Podcast = models.CharField(max_length=50,blank=True)
    Language = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.FileName

    class Meta:
        verbose_name = "Market Outlook"
        verbose_name_plural = "Market Outlook"

def path_equity(instance, filename):
    return '{0}/equity-research/{1}/{2}/{3}'.format(instance.Language, instance.equity_type, instance.Ticker.lower(), filename)

class equity(models.Model):
    Ticker_Date_Language = models.CharField(max_length=50,blank=True)
    Language = models.CharField(max_length=50,blank=True)
    Ticker = models.CharField(max_length=50,blank=True)
    Date = models.DateField()
    Name = models.CharField(max_length=50,blank=True)
    EQUITY_TYPES = [
        ('public', 'Public'),
        ('private', 'Private')
    ]
    Market = models.CharField(max_length=10, choices=EQUITY_TYPES, default='public')
    Industry = models.CharField(max_length=50,blank=True)
    Founded = models.IntegerField(blank=True)
    Website = models.CharField(max_length=255,blank=True)
    Total_Assets = models.IntegerField(blank=True)
    Net_income = models.IntegerField(blank=True)
    ClosePrice= models.IntegerField(verbose_name="Close Price",blank=True)
    Beta = models.IntegerField(blank=True)
    Market_Cap = models.IntegerField(blank=True)
    Float = models.IntegerField(blank=True)
    Outstanding_Shares = models.IntegerField(blank=True)
    ADV_10d = models.IntegerField(blank=True)
    Insider_Shares = models.IntegerField(blank=True)
    Institutional_Shares = models.IntegerField(blank=True)
    Research = models.FileField(upload_to=path_equity )
    Youtube = models.CharField(max_length=50,blank=True)
    Podcast = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Equity Research"
        verbose_name_plural = "Equity Research"

def path_learning(instance, filename):
    return '{0}/how-to/make-green-money-via/{1}/{2}'.format(instance.Language,instance.via.lower(), filename)

class learning(models.Model):
    Date_Category_Language = models.CharField(max_length=50,blank=True)
    Language = models.CharField(max_length=50,blank=True)
    Date = models.DateField(blank=True)
    Topic = models.CharField(max_length=50,blank=True)
    FileName = models.CharField(max_length=50,blank=True)
    Research = models.FileField(upload_to=path_learning )
    Youtube = models.CharField(max_length=50,blank=True)
    Podcast = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.FileName
        
    class Meta:
        verbose_name = "Learning Center"
        verbose_name_plural = "Learning Center"

def path_money_making_trading(instance, filename):
    return '{0}/money-making/trading/{1}/{2}/{3}'.format(instance.Language, instance.Play, instance.Date.strftime('%Y%m%d'), filename)

class money_making_trading(models.Model):
    Date_Play = models.CharField(max_length=50,blank=True)
    Language = models.CharField(max_length=50,blank=True,  default="en")
    Date = models.DateField(blank=True)
    Play = models.CharField(max_length=50,blank=True)
    Plan = models.CharField(max_length=50,blank=True)
    Outcome = models.CharField(max_length=50,blank=True)
    url = models.FileField(upload_to=path_money_making_trading)
    Youtube = models.CharField(max_length=50,blank=True)
    Podcast = models.CharField(max_length=50,blank=True)
    
    def __str__(self):
        return self.Play

    class Meta:
        verbose_name = "Money Making Trading"
        verbose_name_plural = "Money Making Trading"

def path_money_making_investing(instance, filename):
    return '{0}/money-making/investing/{1}/{2}/{3}'.format(instance.Language, instance.Short_Name, instance.Date.strftime('%Y%m%d'), filename)

class money_making_investing(models.Model):
    Date_Company = models.CharField(max_length=50,blank=True)
    Language = models.CharField(max_length=50,blank=True, default="en")
    Date = models.DateField(blank=True,default=None)
    Short_Name = models.CharField(max_length=50,blank=True)
    Full_Name = models.CharField(max_length=50,blank=True)
    Equity_Type = models.CharField(max_length=50,blank=True)
    Entry = models.DateField(blank=True)
    Position = models.IntegerField(blank=True)
    Exit = models.DateField(blank=True)
    Strategy = models.CharField(max_length=50,blank=True)
    url = models.FileField(upload_to=path_money_making_investing)
    Youtube = models.CharField(max_length=50,blank=True)
    Podcast = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.Full_Name

    class Meta:
        verbose_name = "Money Making Investing"
        verbose_name_plural = "Money Making Investing"

class ListPage(models.Model):
    Menu_Name = models.CharField(max_length=100, blank=True)
    Child_Name = models.CharField(max_length=100, blank=True)
    Main_Child = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=100)
    Language = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.Menu_Name

    class Meta:
        verbose_name = "List Main Pages"
        verbose_name_plural = "List Main Pages"

class SocialMedia(models.Model):
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='SocialMedia/')
    name = models.CharField(max_length=100)
    height = models.IntegerField(default=70)
    width = models.IntegerField(default=70)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Media"

class NewsLetterSubscribe(models.Model):
    Sentence = models.TextField(blank=True)
    language = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.language


    class Meta:
        verbose_name = "NewsLetter Subscribe"
        verbose_name_plural = "NewsLetter Subscribe"
