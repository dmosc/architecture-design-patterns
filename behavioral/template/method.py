from abc import ABCMeta, abstractmethod


class BeveragePrepare(metaclass=ABCMeta):
    @abstractmethod
    def add_flavour(self):
        pass

    @abstractmethod
    def get_ingredients(self):
        pass

    @abstractmethod
    def prepare(self):
        pass

    def boil_water(self):
        print("1 - Boil water")

    def finish(self):
        print("5 - Wrap up")

    def template_method(self):
        self.boil_water()
        self.get_ingredients()
        self.prepare()
        self.add_flavour()
        self.finish()


class CoffeePrepare(BeveragePrepare):
    def add_flavour(self):
        print("4 - Add milk and sugar")

    def get_ingredients(self):
        print("2 - Brew coffee beans")

    def prepare(self):
        print("3 - Add ingredients in cup")


class TeaPrepare(BeveragePrepare):
    def add_flavour(self):
        print("4 - Add sugar and zest")

    def get_ingredients(self):
        print("2 - Prepare tea leaves")

    def prepare(self):
        print("3 - Add ingredients to cup")


cafe = CoffeePrepare()
te = TeaPrepare()

cafe.template_method()
te.template_method()
