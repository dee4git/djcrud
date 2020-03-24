

from django.urls import path, include
from . import views
urlpatterns = [

    path('view', views.View, name="viewProduct"),
    path('update', views.Update, name="updateProduct"),
    path('create', views.Create, name="createProduct"),
    path('delete', views.Delete, name="deleteProduct"),

]
