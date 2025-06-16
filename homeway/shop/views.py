from django.shortcuts import render, redirect
from .models import Category, Product  # Import Category and Product models

def home(request):
    user = request.user
    categories = Category.objects.prefetch_related('subcategories').all()  # Fetch categories with subcategories
    
    # Fetch products for each section (limit to 6 items each)
    new_arrivals = Product.objects.filter(section='new_arrivals')[:6]
    featured_products = Product.objects.filter(section='featured')[:6]
    best_sellers = Product.objects.filter(section='best_sellers')[:6]

    context = {
        'user_id': user.id,
        'username': user.username,
        'categories': categories,  # Add categories to context
        'new_arrivals': new_arrivals,
        'featured_products': featured_products,
        'best_sellers': best_sellers,
    }
    return render(request, 'shop/home.html', context)
