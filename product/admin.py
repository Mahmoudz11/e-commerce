from django.contrib import admin

from .models import Category, LocalCategory, Types, Product

class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug':('name',)}
    list_display_links = ('name',)
admin.site.register(Category, AdminCategory)

class AdminLocalCategory(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'category']
    prepopulated_fields = {'slug':('name',)}
    list_display_links = ('name',)
admin.site.register(LocalCategory, AdminLocalCategory)

class AdminLocalTypes(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'category']
    prepopulated_fields = {'slug':('name',)}
    list_display_links = ('name',)
admin.site.register(Types, AdminLocalTypes)

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'category']
    prepopulated_fields = {'slug':('name',)}
    list_display_links = ('name',)
admin.site.register(Product, AdminProduct)
