from django.shortcuts import render
from registrant.forms import RegistrationForm


# Create your views here.
def index(request):
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save(commit=True)
            new_registrant = registration_form.cleaned_data
            return render(request, 'thankyou.html', {'new_registrant': new_registrant})
    else:
        registration_form = RegistrationForm()
        return render(request, 'registration.html', {'registration_form': registration_form})
