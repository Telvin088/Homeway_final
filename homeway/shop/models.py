from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.category.name} - {self.name}"

class Product(models.Model):
    SECTION_CHOICES = [
        ('new_arrivals', 'New Arrivals'),
        ('featured', 'Featured Products'),
        ('best_sellers', 'Best Sellers'),
    ]
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    ratings = models.FloatField(default=0)
    discount_percentage = models.PositiveIntegerField(default=0)
    products_remaining = models.PositiveIntegerField(default=0)
    section = models.CharField(max_length=20, choices=SECTION_CHOICES, default='new_arrivals')

    def discounted_price(self):
        if self.price is None or self.discount_percentage is None:
            return None
        from decimal import Decimal
        discount_factor = Decimal('1') - (Decimal(str(self.discount_percentage)) / Decimal('100'))
        return round(self.price * discount_factor, 2)
    discounted_price.short_description = "Discounted Price"


    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} by {self.user}"
