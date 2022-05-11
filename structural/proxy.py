from abc import ABC, abstractmethod


class Requester(ABC):
    @abstractmethod
    def request(self, query: str):
        ...


class ConcreteRequester(Requester):
    def __init__(self):
        print(self.__class__)

    def request(self, query: str):
        print(f"Long request time: {query}")


class CachedRequester(Requester):
    cached_call: str
    requester: Requester

    def __init__(self, _requester: Requester):
        self.cached_call = ""
        self.requester = _requester
        print(self.__class__)

    def request(self, query: str):
        if self.cached_call == query:
            print(f"Fast request time (cached) {query}")
        else:
            self.cached_call = query
            self.requester.request(query)


class RequesterManager:
    requester: Requester

    def __init__(self, _requester: Requester):
        self.requester = _requester

    def request(self, query: str):
        self.requester.request(query)


requester = ConcreteRequester()
cached_requester = CachedRequester(requester)
manager = RequesterManager(cached_requester)
manager.request("SELECT * FROM Test")
manager.request("SELECT * FROM Test1")
manager.request("SELECT * FROM Test")
manager.request("SELECT * FROM Test")
manager.request("SELECT * FROM Test")
