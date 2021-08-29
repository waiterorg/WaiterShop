from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from core.models import Item
from .serializers import ItemSerializers
# Create your views here.

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers
    filterset_fields = ['status', 'author__username','category__slug']
    search_fields = ['title', 'author__username',
                     'description', 'author__first_name', 'author__last_name']
    ordering_fields = ['status', 'is_special']
    ordering = ['-publish']