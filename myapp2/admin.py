from django.contrib import admin
from .models import User, Product, Order


class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'email', 'phone_number', 'date_registration']
    ordering = ['-pk']
    search_fields = ['name', 'email', 'phone_number']
    search_help_text = 'Поиск по имени, почте, номеру телефона'
    fields = ['name', 'email', 'date_registration', 'phone_number']
    readonly_fields = ['name', 'phone_number', 'date_registration']


@admin.action(description='вайп цен')
def reset_price(modeladmin, request, queryset):
    queryset.update(price=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity_product']
    # fields = ['name', 'description', 'category', 'date_added','rating']
    readonly_fields = ['quantity_product']
    actions = [reset_price]
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['description'],
            },
        ),
        (
            'Цена',
            {
                'fields': ['price', 'quantity_product'],
            }
        )]


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
