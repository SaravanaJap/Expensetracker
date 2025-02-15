from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('edit/<int:id>/',views.edit,name='edit'),
    path('', views.index,name='index' ),
    path('delete/<int:id>/',views.delete,name='delete'),
]