from django.contrib import admin
from .models import User,Profile,Seller,Product
# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Seller)
admin.site.register(Product)