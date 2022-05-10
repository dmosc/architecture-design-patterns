from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    @abstractmethod
    def handle(self):
        pass


class ConcreteStateA(State):
    def handle(self):
        print(f'A: {type(self).__name__}')


class ConcreteStateB(State):
    def handle(self):
        print(f'B: {type(self).__name__}')


class Context(State):
    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def handle(self):
        self.state.handle()


context = Context()
stateA = ConcreteStateA()
stateB = ConcreteStateB()
context.set_state(stateA)
context.handle()
context.set_state(stateB)
context.handle()
