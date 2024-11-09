from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category','index','colour','sold','amount','sold_at',)
    search_fields = ('category__name','colour__name',)
    list_filter = ('category','colour',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Colour)
class ColourAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','phone_number','country','city','region','address','registered_at',)
    search_fields = ('first_name','last_name','email','phone_number','country','city','region','address','registered_at',)

@admin.register(Sklad)
class SkladAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(SkladProducts)
class SkladProductsAdmin(admin.ModelAdmin):
    list_display = ('sklad','shoes',)