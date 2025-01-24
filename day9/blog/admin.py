from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Review)
admin.site.register(Contact)

#pyton manage.py createsuperuser
# username-> admin
# email-> admin@admin.com
# password-> admin
# confirm password-> admin
# y