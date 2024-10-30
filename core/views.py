from rest_framework import generics
from .models import User, FoodItem, Transaction, PickUpSchedule
from .serializers import UserSerializer, FoodItemSerializer, TransactionSerializer, PickUpScheduleSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FoodItemListCreateView(generics.ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class FoodItemRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class PickUpScheduleListCreateView(generics.ListCreateAPIView):
    queryset = PickUpSchedule.objects.all()
    serializer_class = PickUpScheduleSerializer

class PickUpScheduleRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PickUpSchedule.objects.all()
    serializer_class = PickUpScheduleSerializer


class AutoAssignVolunteerView(APIView):
    def post(self, request, transaction_id):
        try:
            transaction = Transaction.objects.get(id=transaction_id)
            # Logic to find nearest available volunteer based on transaction details
            volunteer = User.objects.filter(user_type="volunteer", is_active=True).first()  # Replace with your custom logic
            
            if not volunteer:
                return Response({"error": "No available volunteer found"}, status=status.HTTP_404_NOT_FOUND)
            
            # Create a new PickUpSchedule with the assigned volunteer
            pickup_schedule = PickUpSchedule.objects.create(
                transaction=transaction,
                volunteer=volunteer,
                pickup_time=timezone.now()  # Set to actual time as needed
            )
            serializer = PickUpScheduleSerializer(pickup_schedule)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)
