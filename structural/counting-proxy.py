from abc import ABC, abstractmethod


class Service(ABC):
    @abstractmethod
    def run(self) -> None:
        pass


class ConcreteService(Service):
    def run(self) -> None:
        print("Running a service...")


class ServiceWithCounter(Service):
    calls: int
    service: Service

    def __init__(self, _service: Service):
        self.calls = 0
        self.service = _service

    def run(self) -> None:
        self.service.run()
        self.calls += 1

    def get_calls(self) -> int:
        return self.calls


service = ConcreteService()
service_with_counter = ServiceWithCounter(service)
service_with_counter.run()
service_with_counter.run()
service_with_counter.run()
assert service_with_counter.get_calls() == 3, "Calls don't match"
