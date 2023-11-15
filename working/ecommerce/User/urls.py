from django.urls import path
from . import views
app_name= 'User'
urlpatterns=[
    #path('' , views.index , name="index"),
    path('login' , views.login_view , name="login_view"),
    path('signup' , views.signup , name="signup")
]