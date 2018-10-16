from workshops.models import Workshop
import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'conference-site-django.settings'
django.setup()

workshop1 = Workshop(
    title="Microsoft Powerpoint",
    session=1,
    roomnumber=1,
    starttime='9:30AM',
    endtime='12:00PM',
)
workshop1.save()

workshop2 = Workshop(
    title="Microsoft Excel",
    session=1,
    roomnumber=2,
    starttime='9:30AM',
    endtime='12:00PM',
)
workshop2.save()

workshop3 = Workshop(
    title="Microsoft Word",
    session=1,
    roomnumber=3,
    starttime='9:30AM',
    endtime='12:00PM',
)
workshop3.save()

workshop4 = Workshop(
    title="Email Etiquette",
    session=2,
    roomnumber=1,
    starttime='1:30PM',
    endtime='4:00PM',
)
workshop4.save()

workshop5 = Workshop(
    title="One-on-one Meeting Etiquette",
    session=2,
    roomnumber=2,
    starttime='1:30PM',
    endtime='4:00PM',
)
workshop5.save()

workshop6 = Workshop(
    title="One-on-one Meeting Etiquette",
    session=2,
    roomnumber=3,
    starttime='1:30PM',
    endtime='4:00PM',
)
workshop6.save()

workshop7 = Workshop(
    title="Team Building",
    session=3,
    roomnumber=1,
    starttime='1:30PM',
    endtime='4:00PM',
)
workshop7.save()

workshop8 = Workshop(
    title="Strategies to Improve Focus",
    session=3,
    roomnumber=2,
    starttime='1:30PM',
    endtime='4:00PM',
)
workshop8.save()

workshop9 = Workshop(
    title="Effective Communication",
    session=3,
    roomnumber=3,
    starttime='1:30PM',
    endtime='4:00PM',
)
workshop9.save()
