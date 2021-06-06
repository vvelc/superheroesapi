from django.urls import path

from .views import *

urlpatterns = [
    # ex: /polls/
    path('', index, name='index'),
    path('api', api, name='api'),
]