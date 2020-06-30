from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_main, name='cv_main'),
    path('new_dated/', views.new_dated, name='new_dated'),
    path('new_titled/', views.new_titled, name='new_titled'),
    path('new_text/', views.new_text, name='new_text'),
    path('edit_dated/<int:pk>/', views.edit_dated, name='edit_dated'),
    path('edit_titled/<int:pk>/', views.edit_titled, name='edit_titled'),
    path('edit_text/<int:pk>/', views.edit_text, name='edit_text'),
]
