from django.contrib import admin
from .models import Cart,CartItem

# Register your models here.

class cartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')
    
class cart_ItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'cart','is_active' )
        

admin.site.register(Cart, cartAdmin)

admin.site.register(CartItem , cart_ItemAdmin)

