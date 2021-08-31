from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView
from core.models import Item
from company.models import Company, ContactMessage
from .serializers import ItemSerializers, CompanySerializers, ContactMessageSerializers
# Create your views here.

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers
    filterset_fields = ['status','category']
    search_fields = ['title', 'description']
    ordering_fields = ['status','publish']
    ordering = ['-publish']

class CompanyList(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

class ContactMessageCreate(CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializers