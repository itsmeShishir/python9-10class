from django.urls import path
from .views import register, login_user, logout_user, change_password, change_profile
urlpatterns = [
    path('register', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('change_password/', change_password, name='change_password'),
    path('change_profile/', change_profile, name='change_profile'),
]