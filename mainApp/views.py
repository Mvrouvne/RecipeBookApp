from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy

from .models import Books

class   HomePage(ListView):
    model = Books
    context_object_name = 'home'
    template_name = 'home.html'

class   DetailsPage(DetailView):
    model = Books
    context_object_name = 'details'
    template_name = 'details.html'

class   CreateBook(CreateView):
    model = Books
    context_object_name = 'create'
    template_name = 'create.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

class DeleteBook(DeleteView):
    model = Books
    context_object_name = 'delete'
    template_name = 'delete.html'
    success_url = reverse_lazy('home')