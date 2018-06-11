from django.contrib import admin
from .models import Mobile
from .forms import RegisterForm

class RegisterMobile(admin.ModelAdmin):
    list_display = [ "__str__","model_name", "company_name", "price","os", "processor", "data_transfer", "processor_speed"]
    form = RegisterForm

admin.site.register(Mobile,RegisterMobile)