from django.contrib import admin
from contact import models
# Register your models here.

#Importando o model contacts para o admin
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name', 'last_name', 'phone',
    ordering = 'id',
    list_filter = 'created_date',
    search_fields = 'id', 'first_name','last_name',
    list_per_page = 10
    list_max_show_all = 100

@admin.register(models.Category)
class CategoruAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',
