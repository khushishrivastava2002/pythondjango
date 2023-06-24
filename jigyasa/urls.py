from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('saveenquiry/', views.save, name='saveenquiry'),
    
    path('text_search/', views.search_by_text, name='search_by_text'),
    path('<str:prompt>_text_search_result/', views.search_by_text_result,name='search_by_text_result')
    # path('', views.search_by_text, name='search_by_text'),
]