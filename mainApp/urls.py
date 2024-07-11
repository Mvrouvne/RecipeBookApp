from django.urls import path
from .views import HomePage, DetailsPage, CreateBook, DeleteBook

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('details/<int:pk>/', DetailsPage.as_view(), name='detail'),
    path('create/', CreateBook.as_view(), name='create'),
    path('delete/<int:pk>/', DeleteBook.as_view(), name='delete'),
]
