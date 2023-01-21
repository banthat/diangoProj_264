from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('personal', views.personal, name='personal'),
    path('educational', views.educational, name='educational'),
    path('interests', views.interests, name='interests'),
    path('sell', views.sell, name='sell'),
    path('rolemodel', views.rolemodel, name='rolemodel'),
    path('showMydata', views.showMyData, name='showMyData'),
]
