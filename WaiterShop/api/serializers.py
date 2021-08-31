from rest_framework import serializers
from core.models import Item
from company.models import Company, ContactMessage



class ItemSerializers(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = "__all__"

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class ContactMessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        exclude = ['readed']