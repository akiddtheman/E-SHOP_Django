from django.apps import AppConfig

# Класс представляющий конфигурацию приложения accounts
class AccountsConfig(AppConfig):
    # Указание BigAutoField в качестве типа автоинкрементного поля для моделей в accounts
    default_auto_field = 'django.db.models.BigAutoField'
    # Указание, что имя приложения - accounts
    name = 'accounts'