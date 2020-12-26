from django.urls import path
from .views import *


urlpatterns = [
    path('', promo, name='promo')
]