from django.shortcuts import redirect, render
from stores.models import Store
def home(reqeust):
    stores=Store.objects.all()
    return render (reqeust,"home.html",{
        "stores":stores,
    })
