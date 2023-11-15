from django.shortcuts import render ,get_object_or_404 , redirect
from django.http import HttpResponse
from .models import *
from decimal import Decimal
from django.contrib import messages

# Create your views here.
def homepage (request):
    return render(request ,"store/homepage.html" )

discount=0.5
# Create your views here.

def pro(request):
    Tshirts_cat=Product.objects.filter(category="T-shirts")
    Hodes_cat=Product.objects.filter(category="Hoodies")
    Pants_cat=Product.objects.filter(category="Pants")

    
    
    for c in Pants_cat:
            if c.oldPrice==0:
              c.oldPrice=c.price
              c.price=float(c.price)*discount
              c.save()
    
    

    return render (request, "store/productPage.html",
                   { 
                    "Tshirts_cat":Tshirts_cat,
                    "Hodes_cat":Hodes_cat,
                    "Pants_cat":Pants_cat,
                    
                    })

def viewpro(request , product_name):##حقت رغد
    prod = Product.objects.get(name=product_name)
    return render (request, "store/viewProuduct.html", {
        "product" : prod
    })

def viewBasket(request):
    try:
        basket = Basket.objects.filter(user=request.user)
        tot=0
        for i in basket:
            tot+=i.total
        return render(request , "store/cart.html", {
            'cart': basket ,"total": tot})
    except:
        return render(request , 'User/loginp.html' , {'show': True})

def add_to_basket(request):
    try:
        if request.method == 'POST':
         pid = request.POST['pname']
         prod = Product.objects.get(pk=pid)
         price = request.POST['price']
         qty = request.POST['qty']
        # size =request.POST['size']
        #ممكن نشيلها
        # total = int(qty) *float( price)
         user = request.user
        # uid = user.id
        # created = Basket.objects.get_or_create(user=user, product=prod , quantity=qty , total=total)
         basket , created = Basket.objects.get_or_create(product=prod , user = user)
         if not created:
            #already mojod
             basket.quantity += int(qty)
             total = int(qty) *float( price)
             basket.total+=Decimal(total)
             basket.save()
         else:
             basket.quantity=int(qty)
             total = int(qty) *float( price)
             basket.total=Decimal(total)
             basket.save()
        
        
        # basket.save()
         return render(request , 'store/homepage.html' ,{'showm': True})
    except:    
        return render(request , 'User/loginp.html' , {'show': True})


def delete_all(request):
    # Clear the user's basket
    user = request.user
    Basket.objects.filter(user=user).delete()

    # Redirect to the basket page or another page
    return render(request , 'store/cart.html')

#t3del noura
def checkout(request):
    user = request.user
    bask =  Basket.objects.filter(user=user)
    order = Order(userid=user)
    order.save()
    for basket in bask:
        order.order_item.add(basket.product)
    order.save()
    bask.delete()
    return render(request , 'store/checkout.html')

def search(request):
    if request.method =='POST':
        sname= request.POST['search']
        try:
            prod = Product.objects.get(name=sname)
            return render (request, "store/viewProuduct.html", {
                "product" : prod})
        except:
            return render(request, "store/ltf.html")