from django.urls import path
from .views import (
    OrderDetailView,
    OrderListView,
    OrderCreateView,
    OrderUpdateView
)

urlpatterns = [
    path('', OrderListView.as_view(), name='list-order'),
    path('create/', OrderCreateView.as_view(), name='order-create'),
    path('<int:pk>/detail/', OrderDetailView.as_view(), name='order-detail'),
    path('<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
 
]
