from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('makanan/', include('makanan.urls')),
    path('minuman/', include('minuman.urls')),
    path('camilan/', include('camilan.urls')),
]
