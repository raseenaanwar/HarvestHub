
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPES = (('donor', 'Donor'), ('recipient', 'Recipient'), ('volunteer', 'Volunteer'))
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

class FoodItem(models.Model):
    FOOD_CONDITIONS = (('fresh', 'Fresh'), ('near_expiry', 'Near Expiry'), ('preserved', 'Preserved'))
    type = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expiration_date = models.DateField()
    location = models.CharField(max_length=100)
    condition = models.CharField(max_length=20, choices=FOOD_CONDITIONS, default='fresh')
    category = models.CharField(max_length=100, blank=True, null=True)
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
