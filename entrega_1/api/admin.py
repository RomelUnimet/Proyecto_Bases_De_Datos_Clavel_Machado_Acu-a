from django.contrib import admin
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




admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(ProductBatch)
admin.site.register(Category)
admin.site.register(CurrencyExchange)
admin.site.register(Bill)
admin.site.register(BillProduct)
admin.site.register(PickUp)
admin.site.register(Local)
admin.site.register(Delivery)
admin.site.register(Client)
admin.site.register(Provider)
admin.site.register(Membership)
admin.site.register(MonthEmployee)
admin.site.register(Zone)




