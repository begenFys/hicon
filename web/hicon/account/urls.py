from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.account, name='account'),
    path('hw/<int:pk>/<int:index>', views.CompleteHomework.as_view(), name='complete'),
    path('exit/', authViews.LogoutView.as_view(next_page='promo'), name='exit')
]