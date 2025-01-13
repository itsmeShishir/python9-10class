from django.urls import path
from .views import categories, contact, home, single
urlpatterns = [
    path('', home, name='home'),
    path('categories/', categories, name='categories'),
    path('single/', single, name='single'),
    path('contact/', contact, name="contact"),

    
    # path('about/', About, name='about'),
    # path("template/", HomeTemplate, name="template")
]




