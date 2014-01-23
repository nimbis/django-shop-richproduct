from django.contrib import admin
from shop_richproduct.models import RichProduct


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(RichProduct, ProductAdmin)
