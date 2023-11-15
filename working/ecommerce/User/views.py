from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate , login
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
from django.urls import reverse

# Create your views here.


    
def signup(request):
    if request.method == 'POST':
        fname= request.POST["fname"]
        username=request.POST['username']
        email =request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        # ترا ماسوينا تشييك اذا الايميل موجود او لا
        # creating user
        user=User.objects.create_user(username , email , password)
        user.save()
        # creating profile 
        userprofile =Profile(user=user, address=address)
        userprofile.save()
       # messages.success(request , 'Account created successfully')
        # messages.success(request, 'Account created successfully')
        return render(request , 'store/homepage.html' ,{'showalert': True})
    return render(request , 'User/signup.html')
        
# def index(request):
#     if not request.user.is_authenticated:
#         #if something wrong check here ------------------------------------------------------
#         return HttpResponseRedirect(reverse("login_view"))
#     return render(request , 'store/homepage.html')
def login_view (request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username , password=password)
        if user:
            login(request , user)   
            return render(request , 'store/homepage.html' , {'show_alert': True})
        else:
            messages.success(request, 'Login failed')
            return render(request , "User/loginp.html", {
                "message":"Invalid Credentials"
                    })
    return render(request , "User/loginp.html")