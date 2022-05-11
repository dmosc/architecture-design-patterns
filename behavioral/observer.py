from abc import ABC, abstractmethod


class EventListener(ABC):
    @abstractmethod
    def update(self, filename: str):
        ...


class EmailAlertListener(EventListener):
    def update(self, filename: str):
        print(f"Sending email: {filename} was modified")


class LoggingListener(EventListener):
    def update(self, filename: str):
        print(f"Logging: {filename} was modified")


class EventManager:
    listeners: list[EventListener]

    def __init__(self):
        self.listeners = []

    def subscribe(self, listener: EventListener):
        if listener not in self.listeners:
            self.listeners.append(listener)

    def unsubscribe(self, listener):
        self.listeners.remove(listener)

    def notify(self, filename: str):
        for listener in self.listeners:
            listener.update(filename)


class Editor:
    event_manager: EventManager
    filename: str

    def __init__(self):
        self.event_manager = EventManager()
        self.filename = ""

    def open_file(self, _filename: str):
        self.filename = _filename

    def save_file(self):
        self.event_manager.notify(self.filename)


email_listener = EmailAlertListener()
logging_listener = LoggingListener()
editor = Editor()
editor.open_file("text.txt")

editor.event_manager.subscribe(email_listener)
editor.event_manager.subscribe(logging_listener)
editor.save_file()
assert len(editor.event_manager.listeners) == 2, "Email and Logging listeners were added"

editor.event_manager.unsubscribe(email_listener)
editor.save_file()
assert email_listener not in editor.event_manager.listeners, f"{email_listener} listener should be removed"
assert len(editor.event_manager.listeners) == 1, "Email listener should be removed"




