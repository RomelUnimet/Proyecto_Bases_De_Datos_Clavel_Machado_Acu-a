from django.db import models

# Create your models here.

#-----------------------------------------------------------------------------

class Product(models.Model):
    provider=models.ForeignKey('Provider', on_delete=models.CASCADE)
    product_name=models.CharField(max_length=60)
    category=models.ForeignKey('Category', on_delete=models.CASCADE)
    hall=models.IntegerField()

    # atributo de si se toma en cuenta en la base de datos
    availible=models.BooleanField(default=True)    
    

    def __str__(self):
        return self.product_name

#-----------------------------------------------------------------------------

class ProductBatch(models.Model):
    product=models.ForeignKey('Product', on_delete=models.CASCADE)
    expiration_date=models.DateField(default='1999-03-12')
    elaboration_date=models.DateField(default='1999-03-12')
    actual_quantity=models.BigIntegerField()
    quantity_sold=models.BigIntegerField(default=0)
    cost=models.FloatField()
    discount=models.IntegerField()
    price=models.FloatField()
    point_cost=models.IntegerField() #funcion de dolar por punto y eso
    local=models.ForeignKey('Local', on_delete=models.CASCADE, default=1)

    # atributo de si se toma en cuenta en la base de datos
    availible=models.BooleanField(default=True)

    

#-----------------------------------------------------------------------------

class Category(models.Model):
    name=models.CharField(max_length=60)

    # atributo de si se toma en cuenta en la base de datos
    availible=models.BooleanField(default=True)
    def __str__(self):
        return self.name

#-----------------------------------------------------------------------------

class CurrencyExchange(models.Model):
    bs_exchange= models.FloatField()
    euro_exchange= models.FloatField()
    date=models.DateField(default='1999-03-12')
    # atributo de si se toma en cuenta en la base de datos
    availible=models.BooleanField(default=True)

#-----------------------------------------------------------------------------

class Bill(models.Model):
    
    METHOD=(
        ('Efectivo','Efectivo'),
        ('Online','Online'),
    )

    CURRENCIES=(
        ('Dolares','Dolares'),
        ('Bolivares','Bolivares'),
        ('Euros','Euros'),
    )

    client=models.ForeignKey('Client', on_delete=models.CASCADE)
    is_delivery=models.BooleanField()
    date_time=models.DateTimeField()
    subtotal=models.FloatField()


    ##tax=models.FloatField(default=1.12)
    ##paument_method=models.CharField(max_length=60, choices=METHOD)
    ##currency=models.CharField(max_length=60,choices=CURRENCIES)
    ##total=models.FloatField()

    # atributo de si se toma en cuenta en la base de datos
    availible=models.BooleanField(default=True)

    

#-----------------------------------------------------------------------------

class BillProduct(models.Model):
    bill_id=models.ForeignKey('Bill', on_delete=models.CASCADE)
    batch=models.ForeignKey('ProductBatch', on_delete=models.CASCADE)
    quantity= models.IntegerField()
    discount=models.FloatField()
    # atributo de si se toma en cuenta en la base de datos
    availible=models.BooleanField(default=True)


#-----------------------------------------------------------------------------
class Payment(models.Model):
    
    METHOD=(
        ('Efectivo','Efectivo'),
        ('Online','Online'),
    )

    CURRENCIES=(
        ('Dolares','Dolares'),
        ('Bolivares','Bolivares'),
        ('Euros','Euros'),
    )

    payment_method=models.CharField(max_length=60, choices=METHOD)
    currency=models.CharField(max_length=60,choices=CURRENCIES)
    total=models.FloatField()
    account_n=models.BigIntegerField()

    # atributo de si se toma en cuenta en la base de datos
    availible=models.BooleanField(default=True)

#-----------------------------------------------------------------------------
class Payment_Bill(models.Model):

    bill=models.ForeignKey('Bill', on_delete=models.CASCADE)
    payment=models.ForeignKey('Payment', on_delete=models.CASCADE)

    # atributo de si se toma en cuenta en la base de datos
    availible=models.BooleanField(default=True)

#-----------------------------------------------------------------------------

class PickUp(models.Model):
    bill_id=models.ForeignKey('Bill', on_delete=models.CASCADE)
    pick_up_time=models.TimeField()
    local=models.ForeignKey('Local',on_delete=models.CASCADE)
    delivered=models.BooleanField()

    # atributo de si se toma en cuenta en la base de datos
    availible=models.BooleanField(default=True)

#-----------------------------------------------------------------------------

class Local(models.Model):
    address=models.CharField(max_length=200)
    opening_time=models.TimeField()
    closing_time=models.TimeField()
    manager=models.ForeignKey('Employee', on_delete=models.CASCADE) #poner un limit
    # atributo de si se toma en cuenta en la base de datos
    availible=models.BooleanField(default=True)

#-----------------------------------------------------------------------------

class Delivery(models.Model):
    bill_id=models.ForeignKey('Bill', on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    min_time=models.TimeField()
    
    delivery_boy=models.ForeignKey('Employee', on_delete=models.CASCADE) #poner un limit
    delivered=models.BooleanField()
    zone=models.ForeignKey('Zone',on_delete=models.CASCADE)
    # atributo de si se toma en cuenta en la base de datos
    availible=models.BooleanField(default=True)

#-----------------------------------------------------------------------------


class Client(models.Model):
    ci=models.CharField(max_length=60)
    name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    is_meber=models.BooleanField()
    zone=models.ForeignKey('Zone',on_delete=models.CASCADE, default=1 )
    # atributo de si se toma en cuenta en la base de datos
    availible=models.BooleanField(default=True)

    def __str__(self):
        return self.name

#-----------------------------------------------------------------------------

class Provider(models.Model):
    name=models.CharField(max_length=60)
    main_phone=models.BigIntegerField()
    phone=models.BigIntegerField()
    address=models.CharField(max_length=200)
    email=models.EmailField()
    # atributo de si se toma en cuenta en la base de datos
    availible=models.BooleanField(default=True)
    def __str__(self):
        return self.name

    

#-----------------------------------------------------------------------------

class Membership(models.Model):

    GENDERS=[
        ('Hombre','Hombre'),
        ('Mujer','Mujer'),
        ('Otro','Otro'),
    ]

    points=models.IntegerField()
    phone=models.BigIntegerField()
    gender=models.CharField(max_length=60, choices=GENDERS)
    address=models.CharField(max_length=200)
    birth_date=models.DateField()
    email=models.EmailField()
    client= models.ForeignKey('Client', on_delete=models.CASCADE)
    date_registered=models.DateField()
    # atributo de si se toma en cuenta en la base de datos
    availible=models.BooleanField(default=True)

    def __str__(self):
        return self.email

#-----------------------------------------------------------------------------

class Employee(models.Model):

    GENDERS=(
        ('Hombre','Hombre'),
        ('Mujer','Mujer'),
        ('Otro','Otro'),
    )

    JOBS=[
        ('Gerente','Gerente'),
        ('Repartidor','Repartidor'),
        ('Cajero','Cajero'),
    ]

    ci=models.CharField(max_length=60)
    name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    phone= models.CharField(max_length=20)
    points= models.IntegerField()
    adress=models.CharField(max_length=200)
    gender=models.CharField(max_length=60,choices=GENDERS)
    birth_date=models.DateField()
    job_id=models.CharField(max_length=60,choices=JOBS)
    email=models.EmailField(default='')
    date_hired=models.DateField(default='1999-03-12')
    # atributo de si se toma en cuenta en la base de datos
    availible=models.BooleanField(default=True)

  

    def __str__(self):
        return self.last_name

#-----------------------------------------------------------------------------

class MonthEmployee(models.Model):
    employee=models.ForeignKey('Employee',on_delete=models.CASCADE)
    month=models.CharField(max_length=20)
    year=models.IntegerField()
    # atributo de si se toma en cuenta en la base de datos
    availible=models.BooleanField(default=True)

#-----------------------------------------------------------------------------


class Zone(models.Model):
    name=models.CharField(max_length=60)
    cost=models.FloatField()
    # atributo de si se toma en cuenta en la base de datos
    availible=models.BooleanField(default=True)

#-----------------------------------------------------------------------------