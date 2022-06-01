from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.admin_home, name='admin_home'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('users/', views.users, name='users'),
    path('blockuser/<int:id>',views.blockuser,name='blockuser'),
    path('unblock/<int:id>',views.unblock,name='unblock'),
    path('deleteuser/<int:id>',views.deleteuser,name='deleteuser'),
    
    path('admin_products/', views.admin_products, name='admin_products'),
    path('product_edit/<int:id>', views.product_edit, name='product_edit'),
    path('add_product/', views.add_product, name='add_product'),
    path('product_delete/<int:id>', views.product_delete, name='product_delete'),
    
    
    
    path('admin_category/', views.admin_category, name='admin_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:id>', views.edit_category, name='edit_category'),
    path('delete_category/<int:id>', views.delete_category, name='delete_category'),

    
    
    
    
    path('admin_order/', views.admin_order, name='admin_order'),

]
