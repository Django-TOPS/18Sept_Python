from os import abort
from unicodedata import name
from django.contrib import admin
from django.urls import path
from forumapp import views

urlpatterns = [
   path('',views.index),
   path('profile/',views.profile,name='profile'),
   path('userlogout/',views.userlogout),
   path('about/',views.about),
   path('contact/',views.contact),
   path('services/',views.services),
   path('notes/',views.notes,name='notes')
]
