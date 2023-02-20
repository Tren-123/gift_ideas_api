from django.urls import path
from . import views

urlpatterns = [
    path('giftsManyFilters/', views.GiftsFilterByManyCategories.as_view(), name='gifts_filter_many_categories'),
    path('giftsOneFilter/', views.GiftsFilterByOneCategory.as_view(), name='gifts_filter_one_category'),
]