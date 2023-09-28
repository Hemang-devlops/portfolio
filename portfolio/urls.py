from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('contact/', views.contact, name='contact'),
    path('serv/', include('serv.urls')),
    path('edu/', include('edu.urls')),
    path('save/', views.saveCustomerData, name='save'),
]
