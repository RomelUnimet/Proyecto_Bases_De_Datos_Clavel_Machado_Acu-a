from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView
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


class EmployeeListView(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
class ProductListView(ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
class ProductBatchListView(ListAPIView):
    queryset=ProductBatch.objects.all()
    serializer_class=ProductBatchSerializer
class CategoryListView(ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
class CurrencyExchangeListView(ListAPIView):
    queryset=CurrencyExchange.objects.all()
    serializer_class=CurrencyExchangeSerializer
class BillListView(ListAPIView):
    queryset=Bill.objects.all()
    serializer_class=BillSerializer
class BillProductListView(ListAPIView):
    queryset=BillProduct.objects.all()
    serializer_class=BillProductSerializer
class PaymentListView(ListAPIView):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
class Payment_BillListView(ListAPIView):
    queryset=Payment_Bill.objects.all()
    serializer_class=Payment_BillSerializer
class PickUpListView(ListAPIView):
    queryset=PickUp.objects.all()
    serializer_class=PickUpSerializer
class LocalListView(ListAPIView):
    queryset=Local.objects.all()
    serializer_class=LocalSerializer
class DeliveryListView(ListAPIView):
    queryset=Delivery.objects.all()
    serializer_class=DeliverySerializer
class ClientListView(ListAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer
class ProviderListView(ListAPIView):
    queryset=Provider.objects.all()
    serializer_class=ProviderSerializer
class MembershipListView(ListAPIView):
    queryset=Membership.objects.all()
    serializer_class=MembershipSerializer
class MonthEmployeeListView(ListAPIView):
    queryset=MonthEmployee.objects.all()
    serializer_class=MonthEmployeeSerializer
class ZoneListView(ListAPIView):
    queryset=Zone.objects.all()
    serializer_class=ZoneSerializer





##Detail  Views

class EmployeeDetailView(RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
class ProductDetailView(RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
class ProductBatchDetailView(RetrieveAPIView):
    queryset=ProductBatch.objects.all()
    serializer_class=ProductBatchSerializer
class CategoryDetailView(RetrieveAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
class CurrencyExchangeDetailView(RetrieveAPIView):
    queryset=CurrencyExchange.objects.all()
    serializer_class=CurrencyExchangeSerializer
class BillDetailView(RetrieveAPIView):
    queryset=Bill.objects.all()
    serializer_class=BillSerializer
class BillProductDetailView(RetrieveAPIView):
    queryset=BillProduct.objects.all()
    serializer_class=BillProductSerializer
class PaymentDetailView(RetrieveAPIView):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
class Payment_BillDetailView(RetrieveAPIView):
    queryset=Payment_Bill.objects.all()
    serializer_class=Payment_BillSerializer
class PickUpDetailView(RetrieveAPIView):
    queryset=PickUp.objects.all()
    serializer_class=PickUpSerializer
class LocalDetailView(RetrieveAPIView):
    queryset=Local.objects.all()
    serializer_class=LocalSerializer
class DeliveryDetailView(RetrieveAPIView):
    queryset=Delivery.objects.all()
    serializer_class=DeliverySerializer
class ClientDetailView(RetrieveAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer
class ProviderDetailView(RetrieveAPIView):
    queryset=Provider.objects.all()
    serializer_class=ProviderSerializer
class MembershipDetailView(RetrieveAPIView):
    queryset=Membership.objects.all()
    serializer_class=MembershipSerializer
class MonthEmployeeDetailView(RetrieveAPIView):
    queryset=MonthEmployee.objects.all()
    serializer_class=MonthEmployeeSerializer
class ZoneDetailView(RetrieveAPIView):
    queryset=Zone.objects.all()
    serializer_class=ZoneSerializer





                    
                    
                   
                
                   
                  



