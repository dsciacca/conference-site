from django.shortcuts import render
from awardnominee.models import AwardNominee
from registrant.forms import RegistrationForm
from workshops.models import Workshop


def index(request):
    return render(request, 'index.html')


def activities(request):
    return render(request, 'activities.html')


def meals(request):
    return render(request, 'meals.html')


def keynote(request):
    return render(request, 'keynote.html')


def thankyou(request):
    return render(request, 'thankyou.html')


def workshopschedule(request):
    return render(request, 'workshopschedule.html', {'allWorkshops': Workshop.objects.all()})


def awards(request):
    if request.method == 'POST':
        if bool(request.POST.get('poll')):
            vote = request.POST.get('poll')
            count = AwardNominee.objects.get(name=vote)
            count.currvotes = count.currvotes + 1
            count.save()
    return render(request, 'awards.html', {'allAwards': AwardNominee.objects.all()})


def registration(request):
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save(commit=True)
            new_registrant = registration_form.cleaned_data
            return render(request, 'thankyou.html', {'new_registrant': new_registrant})
    else:
        registration_form = RegistrationForm()
        return render(request, 'registration.html', {'registration_form': registration_form})


def poll(request):
    return render(request, 'poll.html')
