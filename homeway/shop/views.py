from django.shortcuts import render, redirect
from .models import Category  # Import Category model

def home(request):
    user = request.user
    categories = Category.objects.all()  # Fetch all categories

    context = {
        'user_id': user.id,
        'username': user.username,
        'categories': categories,  # Add categories to context
    }
    return render(request, 'shop/home.html', context)
