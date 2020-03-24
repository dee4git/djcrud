from django.shortcuts import render, redirect
from . import forms


def storeCreate(request):
    print("Called")
    top = "Create your store"
    confirm = "Confirm"
    confirmation = "Create Store?"
    cancel = "Cancel"
    if request.method == "POST":
        form = forms.StoreForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return redirect("/")
    else:
        form = forms.StoreForm()
    return render(request, 'create.html',
                  {"form": form,
                   "top": top,
                   "cancel": cancel,
                   "confirm": confirm,
                   "confmsg": confirmation,
                   },
                  )


def storeUpdate(request):
    pass


def storeView(request):
    pass


def storeDelete(request):
    pass
