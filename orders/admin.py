from tkinter import N
from django.contrib import admin
from .models import Payment, NewOrder, OrderProduct

# Register your models here.

class orderProductInline(admin.TabularInline):
    model = OrderProduct
    fields = ('product', 'quantity', 'product_price')
    readonly_fields = ('product', 'quantity', 'product_price')
    can_delete = False
    extra = 0

class  NewOrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'first_name', 'last_name', 'order_total', 'is_ordered', 'tax','created_at']
    list_filter = ['is_ordered', 'status']
    search_fields = ['order_number', 'first_name', 'last_name', 'email', 'phone']
    list_per_page = 20
    inlines = [orderProductInline]
    

admin.site.register(Payment)
admin.site.register(NewOrder,NewOrderAdmin)
admin.site.register(OrderProduct)





