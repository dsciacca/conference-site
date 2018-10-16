from django.db import models
# added stuff from web - gets rid of ImproperlyConfigured error but now AppRegistryNotReady error
# from django.conf import settings
# settings.configure()
# Create your models here.


class Registrant(models.Model):
    titlechoices = (('Dr.', 'Dr.'), ('Mr.', 'Mr.'), ('Ms.', 'Ms.'), ('Mrs.', 'Mrs.'))
    mealschoices = (('mealpack', 'Full Meal Plan'), ('dinnerday2', 'Second Day Dinner Only'))
    cardchoices = (('V', 'Visa'), ('MC', 'Mastercard'), ('AE', 'American Express'))
    session1choices = (('Workshop A', 'Microsoft Powerpoint'), ('Workshop B', 'Microsoft Excel'),
                       ('Workshop C', 'Microsoft Word'))
    session2choices = (('Workshop D', 'Email Etiquette'), ('Workshop E', 'One-on-one Meeting Etiquette'),
                       ('Workshop F', 'Presentation Etiquette'))
    session3choices = (('Workshop G', 'Team Building'), ('Workshop H', 'Strategies to Improve Focus'),
                       ('Workshop I', 'Effective Communication'))
    title = models.CharField(choices=titlechoices, max_length=5)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=25)
    date_of_registration = models.DateField(auto_now_add=True)
    street_address_1 = models.CharField(max_length=30)
    street_address_2 = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    telephone = models.CharField(max_length=12)
    email = models.EmailField(max_length=30)
    website = models.URLField(max_length=100)
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    meals = models.CharField(choices=mealschoices, max_length=15)
    billing_firstname = models.CharField(max_length=20)
    billing_lastname = models.CharField(max_length=25)
    card_type = models.CharField(choices=cardchoices, max_length=30)
    card_number = models.CharField(max_length=16)
    card_csv = models.CharField(max_length=4)
    exp_year = models.CharField(max_length=4)
    exp_month = models.CharField(max_length=2)
    session1 = models.CharField(choices=session1choices, max_length=15)
    session2 = models.CharField(choices=session2choices, max_length=15)
    session3 = models.CharField(choices=session3choices, max_length=15)
