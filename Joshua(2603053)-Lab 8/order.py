from product import Product
from order_line import OrderLine

class Order:
    def __init__(self, order_id: int):
        self.__order_id: int =order_id
        self.__order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity:int) -> None:
        order_line=OrderLine(product,quantity)
        self.__order_lines.append(order_line)

    def remove_order_line(self, product_id:int) -> bool:
        for line in self.__order_lines:
            if line.get_product().get_product_id()== product_id:
                self.__order_lines.remove(line)
                return True
        return False

    def calculate_total(self) -> float:
        total = 0.0
        for line in self.__order_lines:
            total += line.calculate_subtotal()
        return total

    def display_order(self) -> None:
        print("========ORDER=========")
        for line in self.__order_lines:
            line.display_line()
        print("Total: ", self.calculate_total())

    def get_order_lines(self)-> list[OrderLine]:
        return self.__order_lines
    