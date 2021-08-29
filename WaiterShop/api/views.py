from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from core.models import Item
from .serializers import ItemSerializers
# Create your views here.

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers
    filterset_fields = ['status']
    search_fields = ['title', 'description']
    ordering_fields = ['status','publish']
    ordering = ['-publish']