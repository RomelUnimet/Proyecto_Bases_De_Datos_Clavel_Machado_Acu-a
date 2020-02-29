from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django.views.generic import View
from django.db.models import Sum, Count


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
    

    #No se si aqui se puede poner cualquier tipo de query y la vista se encarga de hacerla
    #No se si se pueden hacer queries antes y despues se lo igualamos a query set
    queryset=Employee.objects.all()  
    #Podemos crear objetos con objects.create antes de hacer el queryset??
    #Abajo se pueden poner funciones y como accedemos a ellas si solo usamos un view??







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




#views de querys
class Product_Category(viewsets.ModelViewSet):
    
#     ##Category.objects.create(name="Algo") 
    
    serializer_class=ProductBatchSerializer
    filter_backends=[SearchFilter]
    search_fields=['elaboration_date']

    ##para esto s epone el q del video que viste
    def get_queryset(request, *args, **kwargs):

        queryset=ProductBatch.objects.all()

        return queryset



def get_data(request):

    algo={}
    lista = []

    q=Product.objects.values("product_name", "id", "category__name",'hall')

    #te retorna algo como el json que vas a utilizar el primer campo suele ser el id y los otros dependen de el
    for l in q:

        #algo.append(l[{'id', 'product_name', 'category__name'} ])
        algo.update({l["id"]:{
            "product_name":l["product_name"],
            "category_name":l["category__name"],
            'hall':l['hall']

        }})

        #esto sustituye el valor
        #algo.update({l["id"]:l[ "category__name" ]})
    

    print("-----------------------------------------------------------------------------------------------------------------")
    print(algo)

    
    
    return JsonResponse(algo)



def data_2(request):

    l=[]
    s=[]

    q=Product.objects.values('category__name').annotate(j=Count('category'))[0:5]


    for x in q:
        l.append(x['category__name'])
        s.append(x['j'])

    data={

        'CatName':l,
        'Cant':s

    }

    return JsonResponse(data)
