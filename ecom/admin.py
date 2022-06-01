from django.contrib import admin
from.models import Cart, Category,Product,Bill,UserBill

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Bill)
admin.site.register(UserBill)