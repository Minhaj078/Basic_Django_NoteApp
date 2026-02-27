from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('help/', views.help_page, name='help'),
    path('note/create/', views.create_note, name='create_note'),
    path('note/edit/<int:pk>/', views.edit_note, name='edit_note'),
    path('note/delete/<int:pk>/', views.delete_note, name='delete_note'),
]
