import email
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from store.models import Product,ReviewRating

# Create your views here.

def home(request):
        
        products = Product.objects.all().filter(is_available=True).order_by('-created_date')
        for product in products:
                reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
        context = {
                'products': products,
                'reviews': reviews,
        }
        
        return render(request, 'home.html', context)

        


        




