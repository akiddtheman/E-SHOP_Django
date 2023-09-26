from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import UserRegistrationForm, UserLoginForm, ManagerLoginForm, EditProfileForm
from accounts.models import User

def create_manager():
    # Проверяем, существует ли уже пользователь с email "manager@example.com"
    if not User.objects.filter(email="manager@example.com").first():
        # Если пользователь не существует, создаем нового пользователя с ролью "shop manager"
        user = User.objects.create_user(
            "manager@example.com", 'shop manager' ,'managerpass1234'
        )
        # Присваиваем пользователю роль менеджера
        user.is_manager = True
        user.save()

def manager_login(request):
    if request.method == 'POST':
        form = ManagerLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Аутентифицируем пользователя с помощью email и пароля
            user = authenticate(
                request, email=data['email'], password=data['password']
            )
            # Проверяем, что пользователь существует и имеет роль менеджера
            if user is not None and user.is_manager:
                # Если пользователь существует и является менеджером, выполняем вход
                login(request, user)
                return redirect('dashboard:products')
            else:
                # Если пользователь не существует или не является менеджером, выводим сообщение об ошибке
                messages.error(
                    request, 'username or password is wrong', 'danger'
                )
                return redirect('accounts:manager_login')
    else:
        form = ManagerLoginForm()
    context = {'form': form}
    return render(request, 'manager_login.html', context)

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Создаем нового пользователя с помощью данных из формы регистрации
            user = User.objects.create_user(
                data['email'], data['full_name'], data['password']
            )
            return redirect('accounts:user_login')
    else:
        form = UserRegistrationForm()
    context = {'title':'Signup', 'form':form}
    return render(request, 'register.html', context)

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Аутентифицируем пользователя с помощью email и пароля
            user = authenticate(
                request, email=data['email'], password=data['password']
            )
            # Проверяем, что пользователь существует
            if user is not None:
                # Если пользователь существует, выполняем вход
                login(request, user)
                return redirect('shop:home_page')
            else:
                # Если пользователь не существует, выводим сообщение об ошибке
                messages.error(
                    request, 'username or password is wrong', 'danger'
                )
                return redirect('accounts:user_login')
    else:
        form = UserLoginForm()
    context = {'title':'Login', 'form': form}
    return render(request, 'login.html', context)

def user_logout(request):
    # Выполняем выход пользователя
    logout(request)
    return redirect('accounts:user_login')

def edit_profile(request):
    form = EditProfileForm(request.POST, instance=request.user)
    if form.is_valid():
        # Сохраняем изменения профиля пользователя
        form.save()
        messages.success(request, 'Your profile has been updated', 'success')
        return redirect('accounts:edit_profile')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'title':'Edit Profile', 'form':form}
    return render(request, 'edit_profile.html', context)