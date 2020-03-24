

from django.urls import path, include
from . import views
urlpatterns = [
    path('view', views.storeView, name="viewStore"),
    path('update', views.storeUpdate, name="updateStore"),
    path('create', views.storeCreate, name="createStore"),
    path('delete', views.storeDelete, name="deleteStore"),
    

]
