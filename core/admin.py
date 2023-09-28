from django.contrib import admin
from .models import customerData


class customerAdmiin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')


admin.site.register(customerData, customerAdmiin)
