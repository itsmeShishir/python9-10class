from django.urls import path
from .views import categories, contact, getallblogs, home, single
urlpatterns = [
    path('', home, name='home'),
    path('categories/<int:id>', categories, name='categories'),
    path('allblogs', getallblogs, name='allblogs'),
    path('single/<int:id>', single, name='single'),
    path('contact/', contact, name="contact"),

    
    # path('about/', About, name='about'),
    # path("template/", HomeTemplate, name="template")
]




