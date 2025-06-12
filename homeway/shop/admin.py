from django.contrib import admin
from .models import Category, SubCategory, Product, Review

# Inline admin for reviews inside Product admin
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1  # How many empty review forms to show

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subcategory', 'price', 'discount_percentage', 'ratings', 'products_remaining')
    list_filter = ('category', 'subcategory', 'discount_percentage')
    search_fields = ('name', 'description')
    
    # Show Reviews inline inside Product admin page
    inlines = [ReviewInline]
    
    # Optional: Make discounted price read-only in admin detail page
    readonly_fields = ('discounted_price',)

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
