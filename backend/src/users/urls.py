from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView

# Common urls for all users(Customers, Shops)
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
]
