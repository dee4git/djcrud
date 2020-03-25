

from django.urls import path, include
from . import views
urlpatterns = [

    path('view/<int:id>', views.view, name="viewProduct"),
    path('update/<int:id>', views.update, name="updateProduct"),
    path('create/<int:id>', views.create, name="createProduct"),
    path('delete/<int:id>', views.delete, name="deleteProduct"),

]
