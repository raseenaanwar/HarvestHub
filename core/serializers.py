from rest_framework import serializers
from .models import User, FoodItem, Transaction, PickUpSchedule

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_type', 'contact_number', 'address', 'profile_image']

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ['id', 'type', 'quantity', 'expiration_date', 'location', 'donor', 'condition', 'category', 'created_at', 'updated_at']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'food_item', 'recipient', 'donor', 'timestamp', 'status']

class PickUpScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickUpSchedule
        fields = ['id', 'transaction', 'pickup_time', 'volunteer', 'status', 'location']
