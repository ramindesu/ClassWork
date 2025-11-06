from django.contrib import admin
from .models import Pet, Owner


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "species", "age", "availability")
    list_filter = ("species", "availability")  
    search_fields = ("name", "species") 


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "pet", "request_time")
    search_fields = ("first_name", "last_name")