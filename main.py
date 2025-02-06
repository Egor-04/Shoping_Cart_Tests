class CommandProcessing:
    process_continue = True
    add_product_commands = {"add", "ad", "adp", "add prod", "addprod", "addproduct", "add_product", "add_prod", "add product"}
    remove_commands = {"r", "rem", "rmv", "remove", "remv", "rmove", "rm"}
    check_total_cost_commands = {"c", "cs", "cst", "total", "cost", "check cost", "cart_cost", "crt cst", "cartcost", "cart cost"}

    def __init__(self, cart):
        self.cart = cart

    def check_command(self, command):
        self.process_continue = True
        if command.strip().lower() in self.remove_commands:
            while self.process_continue:
                try:
                    user_input = input("Введите ID продукта для удаления: ")

                    if user_input.strip() == "":  # Проверка на пустой ввод
                        self.process_continue = False
                        break

                    selected_prod = int(user_input)
                    if self.cart.get_cart_size() == 0:
                        self.cart.list_products()
                        self.cart.total_cost()
                        self.process_continue = False
                        break

                    self.cart.remove_product(selected_prod)
                    self.cart.list_products()
                    self.cart.total_cost()
                except ValueError:
                    print("Введите корректный ID!")
                except Exception as e:
                    print(f"Ошибка: {e}")

        elif command.strip().lower() in self.add_product_commands:
            while self.process_continue:
                try:
                    user_input = input("Введите ID от 0-2 товара и он добавится в корзину! Если вы закончили то просто нажмите Enter\n")

                    if user_input.strip() == "":  # Проверка на пустой ввод
                        self.process_continue = False
                        break

                    selected_prod = int(user_input)
                    found_product = self.cart.find_product(selected_prod)

                    if found_product:
                        self.cart.add_to_cart(found_product)
                        self.cart.list_products()
                        self.cart.total_cost()
                    else:
                        print("Продукт не был найден\n\n_________________Попробуйте снова_______________")


                except ValueError:
                    print("Пожалуйста, используйте только целые числа!\n\n_________________Попробуйте снова_______________")

                except Exception as e:
                    print(f"Ошибка: {e}")
        elif command.strip().lower() in self.check_total_cost_commands:
            while self.process_continue:
                try:
                    self.cart.list_products()
                    self.cart.total_cost()
                    self.process_continue = False
                except TypeError as er: print(f"Ошибка: {er}")


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class ShoppingCart:
    __products_at_shop = []
    __items = []

    def __init__(self):
        self.__items = []

    def create_products(self, products):
        self.__products_at_shop = products

    def find_product(self, selected_product_number):
        for i in range(len(self.__products_at_shop)):
            if selected_product_number == self.__products_at_shop[i].id:
                return self.__products_at_shop[i]

    def add_to_cart(self, product):
        self.__items.append(product)

    def remove_product(self, product_id):
        for item in self.__items:
            if item.id == product_id:
                self.__items.remove(item)
                break

    def total_cost(self):
        if len(self.__items) <= 0:
            print("[[ Сумма текущей корзины: 0$ ]]\n")

        print("[[ Сумма текущей корзины: ", sum(product.price for product in self.__items), "$ ]]\n")
        return sum(product.price for product in self.__items)

    def list_products(self):
        if len(self.__items) <= 0:
            return print("Ваша корзина пуста!")
        print("В вашей корозине сейчас есть:\n", "\n".join(str(product.name) for product in self.__items))
        return (str(product.name) for product in self.__items)

    def get_cart_size(self):
        return len(self.__items)

def init():
    # Корзина
    cart = ShoppingCart()

    # Продукты
    cart.create_products([Product(0, 'Арбуз', 100), Product(1, 'Мандарин', 200), Product(2, 'Банан', 300)])

    # Обработчик команд
    command_core = CommandProcessing(cart)

    while True:
        print(
            "Добавление: add, addprod, add_prod, ad\nУдаление: r, rem, remove, rmv\nПросмотр стоимости корзины и ее содержимого: c, cs, cst, total, cost, check cost\n")
        command = input('Введите команду: ')
        command_core.check_command(command)

if __name__ == "__main__":
    init()