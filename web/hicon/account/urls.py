from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.account, name='account'),
    path('exit/', authViews.LogoutView.as_view(next_page='promo'), name='exit')
]