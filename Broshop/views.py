import email
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from store.models import Product

# Create your views here.

def home(request):
        
        products = Product.objects.all().filter(is_available=True)
        
        context = {
                'products': products,
        }
        
        return render(request, 'home.html', context)

        


        




