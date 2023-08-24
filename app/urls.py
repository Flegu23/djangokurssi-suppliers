from django.urls import path

from .views import landingview, productlistview, supplierlistview

urlpatterns = [
    path('', landingview),

    path('products/', productlistview),

    path('suppliers/', supplierlistview),

]
