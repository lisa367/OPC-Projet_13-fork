from django.contrib import admin

# Register your models here.
from .models import Address, Letting


admin.site.register(Letting)
admin.site.register(Address)
