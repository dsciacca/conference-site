from django import forms
from django.forms import ModelForm
from registrant.models import Registrant

TITLE_CHOICES = ('Mr.', 'Ms.', 'Dr.')
CARDTYPE_CHOICES = ('Visa', 'Mastercard', 'American Express')
MEALS_CHOICES = ('Full Meal Plan', 'Second Day Dinner Only')
SESSION1_CHOICES = ('Microsoft Powerpoint', 'Microsoft Excel', 'Microsoft Word')
SESSION2_CHOICES = ('Email Etiquette', 'One-on-one Meeting Etiquette', 'Presentation Etiquette')
SESSION3_CHOICES = ('Team Building', 'Strategies for Improving Focus', 'Effective Communication')


class RegistrationForm(ModelForm):
    class Meta:
        model = Registrant
        fields = [
            'title',
            'firstname',
            'lastname',
            'street_address_1',
            'street_address_2',
            'city',
            'state',
            'zipcode',
            'telephone',
            'email',
            'website',
            'position',
            'company',
            'meals',
            'billing_firstname',
            'billing_lastname',
            'card_type',
            'card_number',
            'card_csv',
            'exp_year',
            'exp_month',
            'session1',
            'session2',
            'session3'
        ]

    widgets = {
        'title': forms.Select(choices=TITLE_CHOICES),
        'meals': forms.RadioSelect(choices=MEALS_CHOICES),
        'card_type': forms.RadioSelect(choices=CARDTYPE_CHOICES),
        'session1': forms.RadioSelect(choices=SESSION1_CHOICES),
        'session2': forms.RadioSelect(choices=SESSION2_CHOICES),
        'session3': forms.RadioSelect(choices=SESSION3_CHOICES)
    }
