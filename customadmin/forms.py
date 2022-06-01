from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account
from store.models import Product
from category.models import category

class ProductUpdate(forms.ModelForm):
    image = forms.ImageField(required=False,error_messages={'invalid':("Please upload a valid image")}, widget= forms.FileInput)

    class Meta:
        model = Product
        fields = ['product_name', 'price', 'image','stock','is_available','category']
        
    def __init__(self, *args, **kwargs):
        super(ProductUpdate, self).__init__(*args, **kwargs )
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class AddProduct(forms.ModelForm):
    image = forms.ImageField(required=False,error_messages={'invalid':("Please upload a valid image")}, widget= forms.FileInput)

    class Meta:
        model = Product
        fields=["product_name","description","category","stock","price","slug","image"]
        
            
    def __init__(self, *args, **kwargs):
        super(AddProduct, self).__init__(*args, **kwargs )
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

        
class AddCategoryForm(forms.ModelForm):
    cat_image = forms.ImageField(required=False,error_messages={'invalid':("Please upload a valid image")}, widget= forms.FileInput)

    class Meta:
        model = category
        fields = ["category_name","description","cat_image",]
        
    def __init__(self, *args, **kwargs):
        super(AddCategoryForm, self).__init__(*args, **kwargs )
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

        
class EditCategoryForm(forms.ModelForm):
    cat_image = forms.ImageField(required=False,error_messages={'invalid':("Please upload a valid image")}, widget= forms.FileInput)

    class Meta:
        model = category
        fields=["category_name","description","cat_image"]   
        
    def __init__(self, *args, **kwargs):
        super(EditCategoryForm, self).__init__(*args, **kwargs )
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

