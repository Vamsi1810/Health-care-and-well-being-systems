from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.CustomerHome,name="cushome"),
    path('orders/',views.CusOrders,name="cusorders"),
    path('cart/',views.Cuscart,name="cuscart"),
    path('hospitals/',views.HospitalsList,name="hospitalslist"),
    path('payment/',views.Payment,name="payment"),
    path('cusults/',views.ConsultsPage,name="consult"),
    path('consultDoctor/<email>/<date>',views.ConsultDoctor,name="consultdoctor"),
    path('updateconsultDoctor/',views.UpdateProbleToConsultation,name="updateconsultdoctor"),
    path('contact/',views.ContactPage,name="cuscontact"),
    path('about/',views.AboutPage,name="cusabout"),
    path('appointment/<str:name>',views.Appointmentpage,name="appointment"),
    path('logout/',views.LogoutDoctello,name="cuslogout"),
    path('medicines/',views.MedicinesPage,name="medicines"),
    path('healthtips/',views.HealthTipsPage,name="cushealthtips"),
    path('profile',views.ProfilePage,name="cusprofile"),
    path('allconsultations/',views.AllconsultationsPage,name="allconsultations"),
    path('placeorder/',views.Placeorder,name="placeorder")
]