from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    
    path('user/', include('users.urls')),
    path('customer/', include('customer.urls')),
    path('orders/', include('orders.urls')),
    path('shop/', include('shop.urls')),
    path('shop/products/', include('products.urls')),

]