from cart.utils.cart import Cart
from shop.models import Category

# Функция, возвращающая словарь количества элементо в корзине пользователя
def return_cart(request):
    # Создание экземпляра класса Cart и преобразование его в список
    cart = len(list(Cart(request)))
    return {'cart_count': cart}

# Функция, возвращающая словарь с категориями
def return_categories(request):
    # Получение всех категорий из базы
    categories = Category.objects.all()
    return {'categories': categories}