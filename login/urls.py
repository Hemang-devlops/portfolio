from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('changepwd/', views.change_pwd, name='changepwd'),
    path('changepass/', views.change_pwd1, name='changepass'),
    path('data/', views.data, name='data'),
    path('delete/<int:id>', views.deleteData, name='deleteData'),
]
