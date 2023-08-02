from django.contrib import admin
from .models import User

# Регистрация юзера для админки
admin.site.register(User)