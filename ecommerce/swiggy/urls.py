from django.urls import path
from . import views
urlpatterns=[
    path('home/',views.home),
    path('photography/',views.photography),
    path('epanchayath/',views.epanchayath)


]