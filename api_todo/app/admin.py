from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'done',
        'created_at',
    )