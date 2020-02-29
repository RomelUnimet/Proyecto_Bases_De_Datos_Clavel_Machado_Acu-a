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


from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 10
        model = Employee
        fields= '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 10
        model = Product
        fields= '__all__'
        
class ProductBatchSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 10
        model = ProductBatch
        fields= '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 10
        model = Category
        fields= '__all__'
class CurrencyExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 10
        model = CurrencyExchange
        fields= '__all__'
class BillSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 10
        model = Bill
        fields= '__all__'
class BillProductSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 10
        model = BillProduct
        fields= '__all__'
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 10
        model = Payment
        fields= '__all__'
class Payment_BillSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 10
        model = Payment_Bill
        fields= '__all__'
class PickUpSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 10
        model = PickUp
        fields= '__all__'
class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 10
        model = Local
        fields= '__all__'
class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 10
        model = Delivery
        fields= '__all__'
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 10
        model = Client
        fields= '__all__'
class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 10
        model = Provider
        fields= '__all__'
class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 10
        model = Membership
        fields= '__all__'
class MonthEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 10
        model = MonthEmployee
        fields= '__all__'
class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 10
        model = Zone
        fields= '__all__'
        



   