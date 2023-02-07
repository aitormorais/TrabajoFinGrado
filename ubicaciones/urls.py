from django.contrib import admin
from django.urls import path,include
from web import views
from rest_framework import routers


# Api router
router = routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/data/', views.receive_json, name='receive_json'),
    # Api routes
    path('',views.home, name= "base"),
    path('guardar_peticion/', views.guardar_peticion, name='guardar_peticion'),
]
