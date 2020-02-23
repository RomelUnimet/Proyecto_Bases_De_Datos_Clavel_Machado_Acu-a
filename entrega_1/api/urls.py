from .views import (EmployeeListView, 
                    ProductListView,
                    ProductBatchListView,
                    CategoryListView,
                    CurrencyExchangeListView,
                    BillListView,
                    BillProductListView,
                    PaymentListView,
                    Payment_BillListView,
                    PickUpListView,
                    LocalListView,
                    DeliveryListView,
                    ClientListView,
                    ProviderListView,
                    MembershipListView,
                    MonthEmployeeListView,
                    ZoneListView,
                    EmployeeDetailView,
                    ProductDetailView,
                    ProductBatchDetailView,
                    CategoryDetailView,
                    CurrencyExchangeDetailView,
                    BillDetailView,
                    BillProductDetailView,
                    PaymentDetailView,
                    Payment_BillDetailView,
                    PickUpDetailView,
                    LocalDetailView,
                    DeliveryDetailView,
                    ClientDetailView,
                    ProviderDetailView,
                    MembershipDetailView,
                    MonthEmployeeDetailView,
                    ZoneDetailView
                    )
from django.urls import path

urlpatterns=[

    path('emp', EmployeeListView.as_view()),
    path('emp/<pk>/', EmployeeDetailView.as_view()),
    
    path('product', ProductListView.as_view()),
    path('product/<pk>/', ProductDetailView.as_view()),

    path('productbatch', ProductBatchListView.as_view()),
    path('productbatch/<pk>/', ProductBatchDetailView.as_view()),

    path('category', CategoryListView.as_view()),
    path('category/<pk>/', CategoryDetailView.as_view()),

    path('currency', CurrencyExchangeListView.as_view()),
    path('currency/<pk>/', CurrencyExchangeDetailView.as_view()),

    path('bill', BillListView.as_view()),
    path('bill/<pk>/', BillDetailView.as_view()),

    path('billp', BillProductListView.as_view()),
    path('billp/<pk>/', BillProductDetailView.as_view()),

    path('payment', PaymentListView.as_view()),
    path('payment/<pk>/', PaymentDetailView.as_view()),

    path('paybill', Payment_BillListView.as_view()),
    path('paybill/<pk>/', Payment_BillDetailView.as_view()),

    path('pickup', PickUpListView.as_view()),
    path('pickup/<pk>/', PickUpDetailView.as_view()),

    path('local', LocalListView.as_view()),
    path('local/<pk>/', LocalDetailView.as_view()),

    path('delivery', DeliveryListView.as_view()),
    path('delivey/<pk>/', DeliveryDetailView.as_view()),

    path('client', ClientListView.as_view()),
    path('client/<pk>/', ClientDetailView.as_view()),

    path('provider', ProviderListView.as_view()),
    path('provider/<pk>/', ProviderDetailView.as_view()),

    path('membership', MembershipListView.as_view()),
    path('membership/<pk>/', MembershipDetailView.as_view()),

    path('monthemp', MonthEmployeeListView.as_view()),
    path('monthemp/<pk>/', MonthEmployeeDetailView.as_view()),
    
    path('zone', ZoneListView.as_view()),
    path('zone/<pk>/', ZoneDetailView.as_view()),
    
]