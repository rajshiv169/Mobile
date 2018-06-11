from django.shortcuts import render, get_list_or_404, get_object_or_404
from .forms import RegisterForm
from .models import Mobile
from .filters import MobileFilter

def home(request):
    queryset = Mobile.objects.all()
    object_list = queryset 
    context = {
        "object_list": queryset,
        "title" : "list"
    }
    return render(request,"home.html", context)

def register(request):
    form = RegisterForm(request.POST or None)
    context = {
        "title": "Register",
        "form": form
    }
    if request.method == "POST" and form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        context = {
            "title" : "Thank You",
        }
    return render(request, "register.html", context)

def mob_details(request,id=None):
    instance = get_object_or_404(Mobile,id=id)
    context = {
        "title" : instance.model_name,
        "instance" : instance
    }
    return render(request,"details.html",context)

def search(request):
    object_list = Mobile.objects.all()
    mobile_filter = MobileFilter(request.GET, queryset=object_list)
    return render(request, 'search.html',{'filter':mobile_filter})