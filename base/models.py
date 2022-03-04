from django.db import models

class table(models.Model):
    Platform = models.CharField(verbose_name='name',max_length=50,blank=True)
    Username = models.CharField(max_length=50,blank=True)
    url = models.URLField()
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.Username
    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Home"

class NewsLetterSubscribers(models.Model):
    name = models.CharField(max_length=255,blank=True)
    email = models.CharField(max_length=255,unique=True,default="")
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "NewsLetter Subscribers"
        verbose_name_plural = "NewsLetter Subscribers"

class aboutus(models.Model):
    Sentence = models.TextField(blank=True)
    Sentence2 = models.TextField(blank=True)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"
    

class analytical_apps_Algo_trader(models.Model):
    Sentence = models.TextField(blank=True)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = "Analytical Apps Algo Trader"
        verbose_name_plural = "Analytical Apps Algo Trader"

class analytical_apps_prospecting(models.Model):
    Sentence = models.TextField(blank=True)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = "Analytical Apps Prospecting"
        verbose_name_plural = "Analytical Apps Prospecting"


class analytical_apps_trade_ideas(models.Model):
    Sentence = models.TextField(blank=True)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = "Analytical Apps Trade Ideas"
        verbose_name_plural = "Analytical Apps Trade Ideas"

class analytical_apps_market_mover(models.Model):
    Sentence = models.TextField(blank=True)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = "Analytical Apps Market Mover"
        verbose_name_plural = "Analytical Apps Market Mover"

    

def market_path(instance, filename):
    return '{0}/market-outlook/{1}/{2}'.format(instance.Language, instance.Date.strftime('%Y%m%d'), filename)
# DATE_INPUT_FORMATS = ['%d-%m-%Y']
class market(models.Model):
    Product = models.CharField(max_length=500,blank=True)
    Country = models.CharField(max_length=500,blank=True,null=True)
    Date = models.DateField()
    Description = models.CharField(max_length=500,blank=True)
    Research = models.FileField(upload_to=market_path)
    YouTube = models.CharField(max_length=500,blank=True)
    Podcast = models.CharField(max_length=500,blank=True)
    Language = models.CharField(max_length=500)

    def __str__(self):
        return self.Product

    class Meta:
        verbose_name = "Market Outlook"
        verbose_name_plural = "Market Outlook"

def path_equity(instance, filename):
    return '{0}/equity-research/{1}/{2}/{3}'.format(instance.Language, instance.Market, instance.Ticker.lower(), filename)

class equity(models.Model):
    Language = models.CharField(max_length=100)

    Product = models.CharField(max_length=1100,blank=True,default="none")
    EQUITY_TYPES = [
        ('public', 'Public'),
        ('private', 'Private')
    ]
    Market = models.CharField(max_length=1100, choices=EQUITY_TYPES, default='public')
    Date = models.DateField()
    Ticker = models.CharField(max_length=1100,blank=True)
    Description = models.CharField(max_length=5100,blank=True,default="none")
    Research = models.FileField(upload_to=path_equity )
    Youtube = models.CharField(max_length=1100,blank=True)
    Podcast = models.CharField(max_length=1100,blank=True)
    # chk_field_name = models.FilePathField(path ="C:/Users/SHAN/Desktop/Working",null=True)

    def __str__(self):
        return self.Product

    class Meta:
        verbose_name = "Equity Research"
        verbose_name_plural = "Equity Research"

def path_learning(instance, filename):
    return '{0}/how-to/make-green-money-via/{1}'.format(instance.Language,filename)

class learning(models.Model):
    Language = models.CharField(max_length=50)
    Product = models.CharField(max_length=50,blank=True, default="N/A")
    Topic = models.CharField(max_length=50,blank=True)
    Class = models.CharField(max_length=50,blank=True, default="N/A")
    Date = models.DateField(blank=True)
    Description = models.CharField(max_length=50,blank=True,default="none")
    Research = models.FileField(upload_to=path_learning )
    Youtube = models.CharField(max_length=50,blank=True)
    Podcast = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.Podcast
        
    class Meta:
        verbose_name = "Learning Center"
        verbose_name_plural = "Learning Center"

def path_money_making_trading(instance, filename):
    return '{0}/money-making/trading/{1}/{2}'.format(instance.Language, instance.Trade_Date.strftime('%Y%m%d'), filename)

class money_making_trading(models.Model):
    Language = models.CharField(max_length=50,default="en")
    Product = models.CharField(max_length=50,blank=True, default="none")
    Class = models.CharField(max_length=50,blank=True, default="none")
    Trade_Date = models.DateField(blank=True)
    Identifier = models.CharField(max_length=50,blank=True, default="none")
    Outcome = models.IntegerField(max_length=50,blank=True)
    Initial_Inv = models.IntegerField(max_length=50,blank=True)
    ROI = models.CharField(max_length=50,blank=True, default="none")
    ReCap = models.FileField(upload_to=path_money_making_trading)
    Youtube = models.CharField(max_length=50,blank=True)
    Podcast = models.CharField(max_length=50,blank=True, default="none")

    def save(self):
        self.ROI = str(float(self.ROI)*100)
        super().save()
    
    def __str__(self):
        return self.Product

    class Meta:
        verbose_name = "Money Making Trading"
        verbose_name_plural = "Money Making Trading"

def path_money_making_investing(instance, filename):
    return '{0}/money-making/investing/{1}/{2}'.format(instance.Language, instance.Entry_Date.strftime('%Y%m%d'), filename)

class money_making_investing(models.Model):
    Language = models.CharField(max_length=50,default="en")
    Product = models.CharField(max_length=50,blank=True, default="none")
    Market = models.CharField(max_length=50,blank=True, default="none")
    Entry_Date = models.DateField(blank=True)
    Ticker = models.CharField(max_length=50,blank=True, default="none")
    Name = models.CharField(max_length=50,blank=True)
    Exit_Date = models.DateField(blank=True,null=True)
    Position = models.IntegerField(blank=True)
    Outcome = models.IntegerField(blank=True)
    Initial_Inv = models.IntegerField(blank=True)
    ROI = models.FloatField(blank=True)
    ReCap = models.FileField(upload_to=path_money_making_investing)
    Youtube = models.CharField(max_length=50,blank=True)
    Podcast = models.CharField(max_length=50,blank=True)

    def save(self):
        if self.ROI != None:
            self.ROI = float("{:.2f}".format(float(self.ROI)*100))
        super().save()

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Money Making Investing"
        verbose_name_plural = "Money Making Investing"

class ListPage(models.Model):
    Menu_Name = models.CharField(max_length=100, blank=True)
    Child_Name = models.CharField(max_length=100, blank=True)
    Main_Child = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=100)
    Language = models.CharField(max_length=50)
    Priority = models.IntegerField(default=0)

    def __str__(self):
        return self.Menu_Name

    class Meta:
        verbose_name = "Page List"
        verbose_name_plural = "Page List"
        

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

class NewsLetter(models.Model):
    Sentence = models.TextField(blank=True)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language


    class Meta:
        verbose_name = "NewsLetter"
        verbose_name_plural = "NewsLetter"


class social_network(models.Model):
    Sentence = models.TextField(blank=True)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = "Social Network"
        verbose_name_plural = "Social Network"