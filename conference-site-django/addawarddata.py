from awardnominee.models import AwardNominee
import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'conference-site-django.settings'
django.setup()

nominee1 = AwardNominee(
    name="Jane Doe",
    description="Jane Doe works in the Marketing department and has improved our companies online presence 3 fold "
                "since beginning her career with us 5 years ago. Her coworkers describe her as dedicated, resourceful, "
                "thoughtful, creative, and someone who is easy to get along with.",
    imgname="img/janedoe.jpg",
    currvotes=0
)
nominee1.save()

nominee2 = AwardNominee(
    name="Joe Shmoe",
    description="Joe Shmoe works in the IT department and has contributed greatly to our computer network as well as "
                "our company website. Joe has been with us for 7 years now, and his coworkers describe him as "
                "knowledgeable, hard-working, friendly, and an overall pleasure to be around.",
    imgname="img/joeshmoe.jpg",
    currvotes=0
)
nominee2.save()

nominee3 = AwardNominee(
    name="Ronda Rae",
    description="Ronda Rae is a key part of our companies sales team, coming out on top in sales numbers for the last "
                "3 quarters in a row. Ronda has been with us for 7 years now, and her fellow sales people describe her "
                "as driven, sociable, committed, and someone who rarely, if ever, takes no for an answer..",
    imgname="img/rondarae.jpg",
    currvotes=0
)
nominee3.save()
