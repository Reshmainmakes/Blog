from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_view, name='search_view'),
    path('add/', views.add_blog, name='add_blog'),
]
