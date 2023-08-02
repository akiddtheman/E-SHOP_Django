from shop.models import Product

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.add_cart_session()

    def __iter__(self):
        # Получаем все ключи (идентификаторы продуктов) из корзины
        product_ids = self.cart.keys()
        # Фильтруем продукты по их идентификаторам
        products = Product.objects.filter(id__in=product_ids)
        # Создаем копию корзины
        cart = self.cart.copy()
        for product in products:
            # Добавляем объект продукта в каждый элемент корзины
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            # Вычисляем общую стоимость каждого элемента
            item['total_price'] = int(item['price']) * int(
                item['quantity'])
            yield item  # Возвращаем элементы корзины по одному

    def add_cart_session(self):
        # Получаем корзину из сессии
        cart = self.session.get(CART_SESSION_ID)
        # Если корзина не существует, создаем пустую корзину в сессии
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        return cart  # Возвращаем корзину

    def add(self, product, quantity):
        # Преобразуем идентификатор продукта в строку
        product_id = str(product.id)

        if product_id not in self.cart:  # Если продукт не находится в корзине
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}  # Добавляем его в корзину с начальными значениями

        # Увеличиваем количество продукта в корзине
        self.cart.get(product_id)['quantity'] += quantity
        self.save()  # Сохраняем изменения в сессии

    def remove(self, product):
        # Преобразуем идентификатор продукта в строку
        product_id = str(product.id)
        if product_id in self.cart:  # Если продукт находится в корзине
            del self.cart[product_id]  # Удаляем его из корзины
            self.save()  # Сохраняем изменения в сессии

    def save(self):
        self.session.modified = True  # Устанавливаем флаг модификации сессии

    def get_total_price(self):
        return sum(int(item['price']) * item['quantity'] for item in
                   self.cart.values())  # Вычисляем общую стоимость всех элементов корзины

    def clear(self):
        # Удаляем корзину из сессии
        del self.session[CART_SESSION_ID]
        self.save()  # Сохраняем изменения в сессии