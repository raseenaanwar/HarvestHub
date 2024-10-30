from django.urls import path

from django.urls import path
from .views import (
    UserListCreateView, UserRetrieveUpdateDeleteView,
    FoodItemListCreateView, FoodItemRetrieveUpdateDeleteView,
    TransactionListCreateView, TransactionRetrieveUpdateDeleteView,
    PickUpScheduleListCreateView, PickUpScheduleRetrieveUpdateDeleteView,
    AutoAssignVolunteerView
)



urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDeleteView.as_view(), name='user-detail'),
    path('food-items/', FoodItemListCreateView.as_view(), name='fooditem-list-create'),
    path('food-items/<int:pk>/', FoodItemRetrieveUpdateDeleteView.as_view(), name='fooditem-detail'),
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionRetrieveUpdateDeleteView.as_view(), name='transaction-detail'),
    path('pickup-schedules/', PickUpScheduleListCreateView.as_view(), name='pickupschedule-list-create'),
    path('pickup-schedules/<int:pk>/', PickUpScheduleRetrieveUpdateDeleteView.as_view(), name='pickupschedule-detail'),
    path('auto-assign-volunteer/<int:transaction_id>/', AutoAssignVolunteerView.as_view(), name='auto-assign-volunteer'),
]
