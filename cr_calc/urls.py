from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('calc/', calculate, name='calc'),
    path('login/', login, name='login'),
]
