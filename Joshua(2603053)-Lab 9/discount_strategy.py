from abc import ABC, abstractmethod

class discount_strategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass

class NoDiscount(discount_strategy):
    def apply(self,total:float)-> float:
        return total

class PercentageDiscount(discount_strategy):
    def __init__(self,percentage:float):
        self.__percentage: float=percentage

    def apply(self,total:float)-> float:
        return total*(1- self.__percentage/100)

class BulkDiscount(discount_strategy):
    def __init__(self, threshold: float, amount: float):
        self.__threshold: float = threshold
        self.__amount: float = amount

    def apply(self, total: float) -> float:
        if total >= self.__threshold:
            return total - self.__amount
        return total

class StudentDiscount(discount_strategy):
    def apply(self, total: float) -> float:
        return total * 0.95