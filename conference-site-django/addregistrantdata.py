import json
from registrant.models import Registrant
import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'conference-site-django.settings'
django.setup()
dataPath = 'input/registrant_data.json'

try:
    with open(dataPath) as file:
        dataObject = json.load(file)
        count = 0
        for registrant in dataObject['registrants']:
            person = Registrant(
                title=registrant['title'],
                firstname=registrant['firstname'],
                lastname=registrant['lastname'],
                date_of_registration=registrant['date_of_registration'],
                city=registrant['city'],
                state=registrant['state'],
                zipcode=registrant['zipcode'],
                telephone=registrant['telephone'],
                email=registrant['email'],
                website=registrant['website'],
                position=registrant['position'],
                company=registrant['company'],
                meals=registrant['meals'],
                billing_firstname=registrant['billing_firstname'],
                billing_lastname=registrant['billing_lastname'],
                card_type=registrant['card_type'],
                card_number=registrant['card_number'],
                card_csv=registrant['card_csv'],
                exp_year=registrant['exp_year'],
                exp_month=registrant['exp_month'],
                session1=registrant['session1'],
                session2=registrant['session2'],
                session3=registrant['session3']
            )
            person.save()
            count = count + 1
        print(str(count) + " registrants added to the database.")
except IOError as e:
    print("Unable to open file " + dataPath)
    quit(1)

