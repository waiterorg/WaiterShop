from rest_framework import serializers
from core.models import Item, Order, OrderItem, Item
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


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'title',
            'price',
            'discount_price',
            'description',
            'image',
            'publish',
            'status',

        )



class MyOrderItemSerializer(serializers.ModelSerializer):    
    item = ItemSerializer()

    class Meta:
        model = OrderItem
        exclude = ['user']

class MyOrderSerializers(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'