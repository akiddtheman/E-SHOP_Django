from django import forms

from .models import User

# Класс представляющий форму для входа пользователей
class UserLoginForm(forms.Form):
    # Указание на то, что поле должно содержать корректный Email адрес
    email = forms.EmailField(
        # Виджет для определения поля в HTML форме
        widget=forms.EmailInput(
            # Аттрибуты виджета
            attrs={'class': 'form-control', 'placeholder': 'email'}
        )
    )
    # Указание на то, что поле должно содержать текст
    password = forms.CharField(
        # Виджет для ввода пароля
        widget=forms.PasswordInput(
            # Аттрибуты виджета
            attrs={'class': 'form-control', 'placeholder': 'password'}
        )
    )


class UserRegistrationForm(forms.Form):
    # Указание на то, что поле должно содержать корректный Email адрес
    email = forms.EmailField(
        # Виджет для определения поля в HTML форме
        widget=forms.EmailInput(
            # Аттрибуты виджета
            attrs={'class': 'form-control', 'placeholder': 'email'}
        )
    )
    # Указание на то, что поле должно содержать текст
    full_name = forms.CharField(
        # Виджет для ввода текста
        widget=forms.TextInput(
            # Аттрибуты виджета
            attrs={'class': 'form-control', 'placeholder': 'full name'}
        )
    )
    # Указание на то, что поле должно содержать текст
    password = forms.CharField(
        # Виджет для ввода пароля
        widget=forms.PasswordInput(
            # Аттрибуты виджета
            attrs={'class': 'form-control', 'placeholder': 'password'}
        )
    )


class ManagerLoginForm(forms.Form):
    # Указание на то, что поле должно содержать корректный Email адрес
    email = forms.EmailField(
        # Виджет для определения поля в HTML форме
        widget=forms.EmailInput(
            # Аттрибуты виджета
            attrs={'class': 'form-control', 'placeholder': 'email'}
        )
    )
    # Указание на то, что поле должно содержать текст
    password = forms.CharField(
        # Виджет для ввода пароля
        widget=forms.PasswordInput(
            # Аттрибуты виджета
            attrs={'class': 'form-control', 'placeholder': 'password'}
        )
    )

# Класс формы для редактирования профиля пользователя
class EditProfileForm(forms.ModelForm):
    class Meta:
        # EditProfileForm связан с User
        model = User
        # Поля модели, которые будут отображаться в форме
        fields = ['full_name', 'email']