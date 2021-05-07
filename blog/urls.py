from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
path('post/new/', views.post_new, name='post_new'),
path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
path('dance/', views.dance),
path('static/blog/a2ec8c82a0b3d1c2393ebe4f919e9d43.gif', views.dance),
]