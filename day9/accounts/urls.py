from django.urls import path
from .views import register, login_user, logout_user, change_password, change_profile, admin, AdminCategory, deletecategory, createcategory, updatecategory, allusers
urlpatterns = [
    path('register', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('change_password/', change_password, name='change_password'),
    path('change_profile/', change_profile, name='change_profile'),
    path("admin-panel/",admin, name="admin-panel"),
    path("admins-category/", AdminCategory, name="admins-category"),
    path("deletecategorys/<int:id>/", deletecategory, name="deletecategorys"),
    path("adminsadd-category/", createcategory, name="createcategory"),
    path("updatecategory/<int:id>/", updatecategory, name="updatecategory"),
    path("allusers/", allusers, name="allusers"),
]