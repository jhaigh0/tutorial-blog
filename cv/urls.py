from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_main, name='cv_main'),
]
