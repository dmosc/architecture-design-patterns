from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def press(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def check(self):
        pass


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class MacButton(Button):
    def __init__(self):
        print(f'Creating {__class__}')

    def press(self):
        print("Pressing a Mac button")


class MacCheckbox(Checkbox):
    def __init__(self):
        print(f'Creating {__class__}')

    def check(self):
        print("Checking a Mac checkbox")


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


class WinButton(Button):
    def __init__(self):
        print(f'Creating {__class__}')

    def press(self):
        print("Pressing a Win button")


class WinCheckbox(Checkbox):
    def __init__(self):
        print(f'Creating {__class__}')

    def check(self):
        print("Checking a Win checkbox")


class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()


class Program:
    def __init__(self, gui_factory: GUIFactory):
        self.gui_factory = gui_factory

    def run(self):
        button = self.gui_factory.create_button()
        check_box = self.gui_factory.create_checkbox()
        button.press()
        check_box.check()


mac_factory = MacFactory()
win_factory = WinFactory()
program = Program(mac_factory)
program.run()
program = Program(win_factory)
program.run()
