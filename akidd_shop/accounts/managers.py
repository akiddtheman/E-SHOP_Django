from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    # Сохранение нового пользователя
    def create_user(self, email, full_name, password):
        if not email:
            raise ValueError('Email is required!')
        if not full_name:
            raise ValueError('full name is required!')
        # Создание нового экземпляра модели пользователя
        user = self.model(email=self.normalize_email(email), full_name=full_name)
        # Установление пароля
        user.set_password(password)
        # Сохранение пользователя в базе данных
        user.save(using=self.db)
        # Возвращение созданного юзера
        return user

    # Создание нового суперюзера
    def create_superuser(self, email, full_name, password):
        user = self.create_user(email, full_name, password)
        # Указание, что пользователь является супером
        user.is_admin = True
        user.save(using=self.db)
        return user