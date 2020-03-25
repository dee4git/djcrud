from django.shortcuts import render, redirect
from . import forms
from stores.models import Store
from .models import Product


def create(request,shop):
    print("Called")
    top = "Add your product"
    confirm = "Confirm"
    confirmation = "Add product?"
    cancel = "Cancel"
    store=Store.objects.get(pk=shop)
    if request.method == "POST":
        form = forms.Form(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.store = store
            instance.save()
            return redirect("/")
    else:
        form = forms.Form()
    return render(request, 'create.html',
                  {"form": form,
                   "top": top,
                   "cancel": cancel,
                   "confirm": confirm,
                   "confmsg": confirmation,
                   },
                  )


def update(request,id):
    top = "Edit your product"
    confirm = "Confirm"
    confirmation = "Update Product?"
    cancel = "Cancel"
    up = Product.objects.get(pk=id)
    if request.method == "POST":
        form = forms.Form(request.POST or None, request.FILES, instance=up)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = forms.Form(instance=up)
    return render(request, 'create.html',
                  {"form": form,
                   "top": top,
                   "cancel": cancel,
                   "confirm": confirm,
                   "confmsg": confirmation,
                   },
                  )


def view(request,id):
    status = 0
    detail = Product.objects.get(pk=id)
    if detail.store.owner == request.user:
        status = 1

    return render(request, "detailproduct.html", {"detail": detail,
                                           "s": status,
                                           })


def delete(request):
    Product.objects.get(pk=id).delete()
    return render("/")
