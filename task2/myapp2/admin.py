from django.contrib import admin
from .models import Client, Product, Order
# Register your models here.

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'price', 'quantity', 'added_date', 'photo')
#     search_fields = ['name', 'description']
#     list_filter = ('added_date',)
#     readonly_fields = ('added_date',)
    

# admin.site.register(Product, ProductAdmin)




# Регистрация моделей в административной панели

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'address', 'registration_date')
    search_fields = ('name', 'email')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'quantity', 'added_date')
    search_fields = ('name', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total_amount', 'order_date')
    search_fields = ('client__name', 'total_amount')
