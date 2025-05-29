from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserProfileDetailUpdateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('profile/', UserProfileDetailUpdateView.as_view(), name='user-profile'), # handles noth update and view 
]
