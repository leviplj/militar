from django.conf.urls import include, url
from django.contrib import admin
from aditamento.militaries.views import military_list

urlpatterns = [
    url(r'^$', military_list, name='list'),    
]
