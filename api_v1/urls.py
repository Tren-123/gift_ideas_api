from django.urls import path
from . import views

urlpatterns = [
    path('gifts_list/', views.gift_list, name='gifts_list'),
]