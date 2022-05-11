from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def request(self):
        ...


class RealSubject(Subject):
    def request(self):
        print("Real subject request")


class RealSubjectProxy(Subject):
    real_subject: Subject

    def __init__(self):
        self.real_subject = RealSubject()

    def request(self):
        print("Proxying RealSubject call")
        self.real_subject.request()


subject = RealSubject()
subject.request()
subject_proxy = RealSubjectProxy()
subject_proxy.request()
