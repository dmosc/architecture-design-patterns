from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def deliver(self) -> None:
        pass


class Truck(Transport):
    def deliver(self) -> None:
        print("Delivering by land in a box.")


class Ship(Transport):
    def deliver(self) -> None:
        print("Delivering by sea in a container.")


class TransportCreator(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass


class TruckCreator(TransportCreator):
    def create_transport(self) -> Transport:
        return Truck()


class ShipCreator(TransportCreator):
    def create_transport(self) -> Transport:
        return Ship()


def program(transport_creator: TransportCreator) -> None:
    transport = transport_creator.create_transport()
    transport.deliver()


creator = TruckCreator()
program(creator)
creator = ShipCreator()
program(creator)
