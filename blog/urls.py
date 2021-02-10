from django.urls import path
from . import views

#check it out joe

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
