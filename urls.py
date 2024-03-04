from django.contrib import admin
from django.urls import path
from triumph import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing),
    path('index',views.index)
]
