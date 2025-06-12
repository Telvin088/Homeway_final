import os
import django

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homeway.settings')

# Set up Django
django.setup()

# Now you can safely import models
from authentication.models import CustomUser

# Example logic
user = CustomUser.objects.get(username='WorkTests')
print(user.username, user.email, user.phone, user.is_superuser, user.is_staff)
