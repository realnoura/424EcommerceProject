from django.contrib import admin
from .models import *
from User.models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Basket)
admin.site.register(Profile)