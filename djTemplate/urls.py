
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from. import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('accounts/', include("accounts.urls")),
    path('store/', include("stores.urls")),
    path('products/', include("products.urls")),
]
urlpatterns = urlpatterns+ static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
urlpatterns = urlpatterns+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()