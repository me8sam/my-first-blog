from django.urls import re_path
from . import views


urlpatterns = [
     re_path('', views.post_list, name = 'post_list'),
     re_path('post/<int:pk>/', views.post_detail, name='post_detail'),
]