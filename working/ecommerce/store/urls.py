from django.urls import path
from . import views
app_name='store'
urlpatterns=[
    path('' , views.homepage , name='homepage') ,
    path('product' , views.pro , name='products'),
    #حقت الباث اللي لازم تنحط
    path("<str:product_name>/" , views.viewpro , name='productView'),
    path('add_to_basket', views.add_to_basket, name='add_to_basket'),
    path('viewBasket' , views.viewBasket , name='viewBasket'),
    path('delete_all' , views.delete_all , name='delete_all'),
    path('checkout' , views.checkout , name='checkout'),
    path('search' , views.search , name='search')
]