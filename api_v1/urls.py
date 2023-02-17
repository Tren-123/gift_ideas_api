from django.urls import path
from . import views

urlpatterns = [
    path('gifts_list_many_categories/', views.GiftsListByManyCategories.as_view(), name='gifts_list_many_categories'),
    path('gifts_list_one_category/', views.GiftsListByOneCategory.as_view(), name='gifts_list_one_category'),
]