from django.contrib import admin
from .models import Tag, LicenseType, ProductType, Product


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Admin configuration for the :model:`shop.Tag` model.

    **Attributes:**

    - ``list_display``: Displays the "name" field in the admin list view.
    """

    list_display = ("name",)


@admin.register(LicenseType)
class LicenseTypeAdmin(admin.ModelAdmin):
    """
    Admin configuration for the :model:`shop.LicenseType` model.

    **Attributes:**

    - ``list_display``: Shows the license name and description.
    - ``search_fields``: Enables search by license name.
    """

    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin configuration for the :model:`shop.Product` model.

    **Attributes:**

    - ``list_display``: Displays key product details.
    - ``search_fields``: Enables searching by title and description.
    - ``list_filter``: Enables filtering by related fields.
    - ``filter_horizontal``: Enables horizontal filter for M2M fields.
    """

    list_display = ("title", "price", "created_at")
    search_fields = ("title", "description")
    list_filter = ("theme", "tags", "product_types", "license_types")
    filter_horizontal = ("tags", "product_types", "license_types")


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    """
    Admin configuration for the :model:`shop.ProductType` model.

    **Attributes:**

    - ``list_display``: Displays the "name" field in the admin list view.
    """

    list_display = ("name",)
