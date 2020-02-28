from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets

from .models import  (Employee,
                     Product,
                     ProductBatch,
                     Category,
                     CurrencyExchange,
                     Bill, 
                     BillProduct,
                     Payment,
                     Payment_Bill,
                     PickUp,
                     Local,
                     Delivery,
                     Client,
                     Provider,
                     Membership,
                     MonthEmployee,
                     Zone)
from .serializers import  (EmployeeSerializer,
                           ProductSerializer,
                           ProductBatchSerializer,
                           CategorySerializer,
                           CurrencyExchangeSerializer,
                           BillSerializer, 
                           BillProductSerializer,
                           PaymentSerializer,
                           Payment_BillSerializer,
                           PickUpSerializer,
                           LocalSerializer,
                           DeliverySerializer,
                           ClientSerializer,
                           ProviderSerializer,
                           MembershipSerializer,
                           MonthEmployeeSerializer,
                           ZoneSerializer)            

# Create your views here.


##@api_view(('GET',))
##def api_detail(request):
  ##  emp=Employee.objects.all()

    ##serializer=EmployeeSerializer(emp, many=True)

    ##return Response(serializer.data)


class EmployeeView(viewsets.ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()  
class ProductView(viewsets.ModelViewSet):    
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
class ProductBatchView(viewsets.ModelViewSet):
    queryset=ProductBatch.objects.all()
    serializer_class=ProductBatchSerializer
class CategoryView(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
class CurrencyExchangeView(viewsets.ModelViewSet):
    queryset=CurrencyExchange.objects.all()
    serializer_class=CurrencyExchangeSerializer
class BillView(viewsets.ModelViewSet):
    queryset=Bill.objects.all()
    serializer_class=BillSerializer
class BillProductView(viewsets.ModelViewSet):
    queryset=BillProduct.objects.all()
    serializer_class=BillProductSerializer
class PaymentView(viewsets.ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
class Payment_BillView(viewsets.ModelViewSet):
    queryset=Payment_Bill.objects.all()
    serializer_class=Payment_BillSerializer
class PickUpView(viewsets.ModelViewSet):
    queryset=PickUp.objects.all()
    serializer_class=PickUpSerializer
class LocalView(viewsets.ModelViewSet):
    queryset=Local.objects.all()
    serializer_class=LocalSerializer
class DeliveryView(viewsets.ModelViewSet):
    queryset=Delivery.objects.all()
    serializer_class=DeliverySerializer
class ClientView(viewsets.ModelViewSet):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer
class ProviderView(viewsets.ModelViewSet):
    queryset=Provider.objects.all()
    serializer_class=ProviderSerializer
class MembershipView(viewsets.ModelViewSet):
    queryset=Membership.objects.all()
    serializer_class=MembershipSerializer
class MonthEmployeeView(viewsets.ModelViewSet):
    queryset=MonthEmployee.objects.all()
    serializer_class=MonthEmployeeSerializer
class ZoneView(viewsets.ModelViewSet):
    queryset=Zone.objects.all()
    serializer_class=ZoneSerializer








                    
                    
                   
                
                   
                  



