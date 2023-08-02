from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager
from shop.models import Product


class User(AbstractBaseUser):
    # Поле для хранения электронной почты пользователя
    email = models.EmailField(max_length=100, unique=True)
    # Поле для хранения полного имени пользователя
    full_name = models.CharField(max_length=100)
    # Флаг, указывающий, является ли пользователь администратором
    is_admin = models.BooleanField(default=False)
    # Флаг, указывающий, активен ли пользователь
    is_active = models.BooleanField(default=True)
    # Связь "многие ко многим" с моделью Product для хранения понравившихся товаров пользователя
    likes = models.ManyToManyField(Product, blank=True, related_name='likes')
    # Флаг, указывающий, является ли пользователь менеджером магазина
    is_manager = models.BooleanField(default=False)

    # Менеджер объектов для модели User
    objects = UserManager()

    # Поле, используемое для аутентификации пользователя (в данном случае - email)
    USERNAME_FIELD = 'email'
    # Обязательные поля при создании пользователя
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        # Возвращает строковое представление пользователя (его email)
        return self.email

    def has_perm(self, perm, obj=None):
        # Все пользователи имеют все разрешения
        return True

    def has_module_perms(self, app_label):
        # Все пользователи имеют доступ ко всем модулям
        return True

    @property
    def is_staff(self):
        # Проверяет, является ли пользователь администратором
        return self.is_admin

    def get_likes_count(self):
        # Возвращает количество понравившихся товаров пользователя
        return self.likes.count()
