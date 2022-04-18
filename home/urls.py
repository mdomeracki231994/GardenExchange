from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home_page'),
    path('about/', about, name='about' )
]