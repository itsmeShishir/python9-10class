from django.urls import path
from .views import About, home, HomeTemplate
urlpatterns = [
    path('', home, name='home'),
    path('about/', About, name='about'),
    path("template/", HomeTemplate, name="template")
]




