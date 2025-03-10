"""
URL configuration for LifeLink project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from LifeLinkApp import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='homepage'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup, name='signup'),
    path('donate/',views.blood_donation, name='blood_donation'),
    path('donor_details/',views.donor_details, name='donor_details'),
    path('view_donors/',views.view_donors,name='view_donors'),

    path('recipient_details/',views.recipient_details, name='recipient_details'),
    path('view_recipients/', views.view_recipients, name='view_recipients'),
    path('clients/', views.contact_us, name='contact_us'),
    path('view_clients/', views.view_clients, name='view_clients'),
    path('organ_transplant/', views.organ_transplant, name='organ_transplant'),
    path('organ_donor_details/', views.organ_donors_details,name='organ_donor_details'),
    path('view_organ_donors/', views.view_organ_donors, name='view_organ_donors'),
    path('organ_recipient_details/',views.organ_recipient_details, name='organ_recipient_details'),
    path('view_organ_recipients/',views.view_organ_recipients,name='view_organ_recipients')

]
