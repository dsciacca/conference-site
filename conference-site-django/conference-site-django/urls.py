"""conference-site-django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from conferencesite import views

urlpatterns = [
    url(r'^awardnominee/', include('awardnominee.urls')),
    url(r'^registrant/', include('registrant.urls')),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', views.index, name='index'),
    url(r'^index/', views.index, name='index'),
    url(r'^activities/', views.activities, name='activities'),
    url(r'^funstufftodo/', views.activities, name='activities'),
    url(r'^meals/', views.meals, name='meals'),
    url(r'^keynote/', views.keynote, name='keynote'),
    url(r'^thankyou/', views.thankyou, name='thankyou'),
    url(r'^workshopschedule/', views.workshopschedule, name='workshopschedule'),
    url(r'^awards/', views.awards, name='awards'),
    url(r'^registration', views.registration, name='registration'),
    url(r'^poll', views.poll, name='poll'),
]
