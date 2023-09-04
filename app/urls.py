from django.urls import path

from .views import landingview, productlistview, supplierlistview, addsupplier, addproduct

urlpatterns = [
    path('', landingview),

    path('products/', productlistview),
    path('add-product/', addproduct),

    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),

]
