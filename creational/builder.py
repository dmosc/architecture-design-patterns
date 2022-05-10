class House:
    windows: int
    bathrooms: int

    def __init__(self):
        pass


class HouseBuilder:
    house: House = None

    def reset(self) -> None:
        self.house = House()

    def add_windows(self, _windows: int) -> None:
        self.house.windows = _windows

    def add_bathrooms(self, _bathrooms: int) -> None:
        self.house.bathrooms = _bathrooms

    def get_house(self) -> House:
        return self.house


class HouseBuilderDirector:
    house_builder: HouseBuilder

    def __init__(self, _house_builder: HouseBuilder):
        self.house_builder = _house_builder

    def set_builder(self, _house_builder: HouseBuilder):
        self.house_builder = _house_builder

    def build_small_house(self):
        self.house_builder.reset()
        self.house_builder.add_bathrooms(1)
        self.house_builder.add_windows(4)

    def build_medium_house(self):
        self.house_builder.reset()
        self.house_builder.add_bathrooms(3)
        self.house_builder.add_windows(8)

    def build_large_house(self):
        self.house_builder.reset()
        self.house_builder.add_bathrooms(5)
        self.house_builder.add_windows(15)


house_builder = HouseBuilder()
director = HouseBuilderDirector(house_builder)

director.build_small_house()
house = house_builder.get_house()
print(house.windows, house.bathrooms)

director.build_medium_house()
house = house_builder.get_house()
print(house.windows, house.bathrooms)

director.build_large_house()
house = house_builder.get_house()
print(house.windows, house.bathrooms)
