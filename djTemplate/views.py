from django.shortcuts import redirect, render


def home(reqeust):
    return render (reqeust,"home.html",{
    })
