from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

# Create your views here.
class HomeView(ListView):
    model = Item
    paginate_by = 5
    template_name = "shop/home.html"

class ItemDetailView(DetailView):
    model = Item
    template_name = "shop/item_detail.html"