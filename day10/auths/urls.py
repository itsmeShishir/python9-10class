from django.urls import path
from .views import LoginApi, Profile, UpdateProfile, UserList, UserRegister, changePassword,  logout_user
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('users/', UserList.as_view() , name="users" ),
    path('register/', UserRegister.as_view() , name="register" ),
    path('login', LoginApi.as_view() , name="login" ),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('profile', Profile.as_view() , name="profile" ),
    path('updateprofile', UpdateProfile.as_view() , name="profile" ),
    path("changepassword/", changePassword.as_view() , name="changepassword" ),
    path("logout/", logout_user.as_view() , name="logout" ),
]
