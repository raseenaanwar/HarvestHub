from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    USER_TYPES = (('donor', 'Donor'), ('recipient', 'Recipient'), ('volunteer', 'Volunteer'))
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    
    # Adding custom related_name to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Avoids clash with auth.User.groups
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Avoids clash with auth.User.user_permissions
        blank=True
    )


class FoodItem(models.Model):
    FOOD_CONDITIONS = (('fresh', 'Fresh'), ('near_expiry', 'Near Expiry'), ('preserved', 'Preserved'))
    FOOD_TYPES = (
        ('vegetable', 'Vegetable'),
        ('fruit', 'Fruit'),
        ('grain', 'Grain'),
        ('dairy', 'Dairy'),
        ('meat', 'Meat'),
        ('juice', 'Juice'),  # Replaced Beverage with Juice
        # Add more as needed
    )

    food_type = models.CharField(max_length=50, choices=FOOD_TYPES)
    quantity = models.IntegerField()
    expiration_date = models.DateField()
    location = models.CharField(max_length=100)
    condition = models.CharField(max_length=20, choices=FOOD_CONDITIONS, default='fresh')
    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="donations")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Transaction(models.Model):
    STATUS_CHOICES = (('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed'))
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receipts")
    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="donor_transactions")
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

class PickUpSchedule(models.Model):
    STATUS_CHOICES = (('scheduled', 'Scheduled'), ('picked_up', 'Picked Up'), ('delivered', 'Delivered'))
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    pickup_time = models.DateTimeField()
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pickups")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    location = models.CharField(max_length=100)
