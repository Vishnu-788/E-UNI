from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  

    path('products/', include('products.urls')),
    path('user/', include('users.urls')),
    path('user/order/', include('orders.urls')),
    path('customer/', include('customer.urls')),
    path('shop/', include('shop.urls'))

]