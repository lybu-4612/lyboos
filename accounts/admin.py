from django.contrib import admin
from .models import Account,UserProfile
from django.utils.html import format_html

# Register your models here.



admin.site.register(Account)
admin.site.register(UserProfile)

