from abc import ABC, abstractmethod


class Receiver:
    def action(self):
        print("Receive an action")


class Command(ABC):
    _receiver: Receiver

    def __init__(self, receiver: Receiver):
        self._receiver = receiver

    @abstractmethod
    def execute(self):
        ...


class ConcreteCommand(Command):
    def execute(self):
        self._receiver.action()


class Sender:
    _command: Command

    def command(self, command: Command):
        self._command = command

    def execute(self):
        self._command.execute()


receiver = Receiver()
cmd = ConcreteCommand(receiver)
sender = Sender()
sender.command(cmd)
sender.execute()
