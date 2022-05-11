from abc import ABC, abstractmethod


class Device(ABC):
    enabled: bool
    volume: int
    channel: int

    @abstractmethod
    def is_enabled(self):
        ...

    @abstractmethod
    def enable(self):
        ...

    @abstractmethod
    def disable(self):
        ...

    @abstractmethod
    def get_volume(self):
        ...

    @abstractmethod
    def set_volume(self, _volume: int):
        ...

    @abstractmethod
    def get_channel(self):
        ...

    @abstractmethod
    def set_channel(self, _channel: int):
        ...


class Radio(Device):
    def __init__(self):
        self.enabled = False
        self.volume = 75
        self.channel = 0
        print(f'Working with: {self.__class__}')

    def is_enabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def get_volume(self):
        return self.volume

    def set_volume(self, _volume: int):
        self.volume = _volume

    def get_channel(self):
        return self.channel

    def set_channel(self, _channel: int):
        self.channel = _channel


class TV(Device):
    def __init__(self):
        self.enabled = False
        self.volume = 50
        self.channel = 0
        print(f'Working with: {self.__class__}')

    def is_enabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def get_volume(self):
        return self.volume

    def set_volume(self, _volume: int):
        self.volume = _volume

    def get_channel(self):
        return self.channel

    def set_channel(self, _channel: int):
        self.channel = _channel


class Remote:
    device: Device

    def __init__(self, _device: Device):
        self.device = _device
        print(f'Working with: {self.__class__}')

    def toggle_power(self) -> None:
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_down(self) -> None:
        volume = self.device.get_volume()
        self.device.set_volume(volume - 1)

    def volume_up(self) -> None:
        volume = self.device.get_volume()
        self.device.set_volume(volume + 1)

    def channel_down(self) -> None:
        channel = self.device.get_channel()
        self.device.set_channel(channel - 1)

    def channel_up(self) -> None:
        channel = self.device.get_channel()
        self.device.set_channel(channel + 1)


class AdvancedRemote(Remote):
    def mute(self):
        self.device.set_volume(0)


tv = TV()
remote = Remote(tv)

radio = Radio()
advanced_remote = AdvancedRemote(radio)
