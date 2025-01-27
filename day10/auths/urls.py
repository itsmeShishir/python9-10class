from django.urls import path
from .views import UserList, UserRegister
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('users/', UserList.as_view() , name="users" ),
    path('register/', UserRegister.as_view() , name="register" ),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
