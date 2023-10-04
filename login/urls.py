from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.log_in, name='login'),
    path('data/', views.data, name='data'),
    path('delete/<int:id>', views.deleteData, name='deleteData'),
]
