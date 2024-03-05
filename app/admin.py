from django.contrib import admin

# Register your models here.

from app.models import *

admin.site.register(ProductCatagory)

admin.site.register(Product)