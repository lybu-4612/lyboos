
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages

from accounts.models import Account
from orders.models import NewOrder
from store.models import Product
from category.models import category
from .forms import ProductUpdate,AddProduct,AddCategoryForm,EditCategoryForm


# Create your views here.


def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_home')
    else:
        print('inside else')
        if request.method == 'POST':
            print('inside post')
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            #print(user.is_admin)
            if user is not None:
                if user.is_superadmin:
                    auth.login(request, user)
                    return redirect('admin_home')
                else:
                    messages.info(request, 'no admin previlages')
                    return redirect('admin_login')
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('admin_login')
        else:
            
            return render(request, 'customadmin/admin_login.html')
    #return render(request, 'customadmin/login.html')


def admin_home(request):
    if request.user.is_authenticated:
        user = Account.objects.all()
        print(user)
        context = {'user':user}
        return render(request, 'customadmin/admin_home.html',context)
    else:
        return redirect('admin_login')


def admin_logout(request):
    auth.logout(request)
    return redirect('admin_home')

def users(request):
    user = Account.objects.all()
    context = {'user':user}
    return render(request, 'customadmin/users.html', context)

def blockuser(request,id):
    user = Account.objects.get(id=id)
    user.is_active = False
    user.save()
    return redirect('admin_home')


def unblock(request,id):
    user = Account.objects.get(id=id)
    user.is_active = True
    user.save()
    return redirect('admin_home')
    

def deleteuser(request,id):
    user =Account.objects.get(id=id)
    user.delete()
    return redirect('admin_home')


#product views

def admin_products(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'customadmin/admin_products.html', context)  

def product_edit(request,id):
    
    form=ProductUpdate(request.POST)
    product=Product.objects.get(id=id)
    form=ProductUpdate(instance=product)
    context = {
        'form': form,
        'id' : id,
        'product':product
        
    }
    if request.method == 'POST':
        form = ProductUpdate(request.POST, request.FILES, instance=product)
    
    if form.is_valid():
        
        form.save()
        messages.success(request, 'Product updated successfully')

        return redirect('admin_products')


    return render(request, 'customadmin/product_edit.html',context)


def add_product(request):
        form=AddProduct()
        context={
            'form':form
        }
        if request.method == 'POST':
            form=AddProduct(request.POST,request.FILES)
            if form.is_valid():
                print('Product added successfully')
                form.save()
                return redirect('admin_products')
            else:
                messages.error(request, "product invalid")
                return redirect('add_product')
        return render(request, 'customadmin/add_product.html',context)
    
def product_delete(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('admin_products')
    
        

#admin_category views

def admin_category(request):
    
    categ = category.objects.all()
    context = {
        'category':categ
    }
    return render(request, 'customadmin/admin_category.html', context)

def add_category(request):
    form=AddCategoryForm()
    context={
        'form':form
    }
    if request.method == 'POST':
        form=AddCategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('admin_category')
        else:
            messages.error(request, "product invalid")
            return redirect('add_category')
    return render(request, 'customadmin/add_category.html',context)

def edit_category(request,id):
    form=EditCategoryForm(request.POST)
    cate=category.objects.get(id=id)
    form=EditCategoryForm(instance=category)
    context = {
        'form': form,
        'id' : id,
        'cate': cate
        
    }
    if request.method == 'POST':
        form = EditCategoryForm(request.POST, instance=category)
        
        if form.is_valid():
            
            form.save()
            return redirect('admin_category')

    return render(request, 'customadmin/edit_category.html',context)

def delete_category(request,id):
    product=category.objects.get(id=id)
    product.delete()
    return redirect('admin_category')








def admin_order(request):
    orders = NewOrder.objects.all()
    context = { 'orders':orders}
    return render(request, 'customadmin/admin_order.html', context)

    

