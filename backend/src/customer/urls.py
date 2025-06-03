from django.urls import path
from .views import (
    CustomerProfileDetailUpdateView,
)

urlpatterns = [
    path('', CustomerProfileDetailUpdateView.as_view(), name='customer-profile')
]
