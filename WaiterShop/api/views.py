from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from core.models import Item, OrderItem, Order, Address
from company.models import Company, ContactMessage
from .serializers import ItemSerializers, CompanySerializers, ContactMessageSerializers, MyOrderSerializers, AddressSerializers
from django.utils import timezone
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


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])   
def add_to_cart(request, slug):
    try:
        item = get_object_or_404(Item, slug=slug)
        order_item, created = OrderItem.objects.get_or_create(
            item=item,
            user=request.user,
            ordered=False
        )
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            # check if the order item is in the order
            if order.items.filter(item__slug=item.slug).exists():
                order_item.quantity += 1
                order_item.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                order.items.add(order_item)
                return Response(status=status.HTTP_201_CREATED)
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(
                user=request.user, ordered_date=ordered_date)
            order.items.add(order_item)
            return Response(status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])   
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
            return Response(status=status.HTTP_400_BAD_REQUEST) 

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])   
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                return Response(status=status.HTTP_200_OK)
            else:
                order.items.remove(order_item)
                order_item.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




class OrderSummary(ListModelMixin, GenericAPIView):
    serializer_class = MyOrderSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user, ordered = False)
        return queryset
    
    def get(self, request, *args, **kwargs):
        return self.list(request,*args, **kwargs )


class CheckoutAPIView(CreateModelMixin,GenericAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializers
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)