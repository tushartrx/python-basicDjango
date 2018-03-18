from django.contrib import admin
from django.urls import path
from . import views
app_name = 'books'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index' ),
    path('<int:pk>/', views.DetailsView.as_view(), name='details' ),
    path('books/add/',views.BookCreate.as_view(),name='book-add'),
]