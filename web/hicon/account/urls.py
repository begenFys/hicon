from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.account, name='account'),
    path('complete/<int:pk>/<int:index>', views.CompleteHomework.as_view(), name='complete'),
    path('change/<int:pk>/<int:index>', views.ChangeHomework.as_view(), name='change'),
    path('exit/', authViews.LogoutView.as_view(next_page='promo'), name='exit')
]