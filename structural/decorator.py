from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def write_data(self, data: str) -> None:
        pass

    @abstractmethod
    def read_data(self) -> None:
        pass


class FileDataSource(DataSource):
    filename: str

    def __init__(self, _file_name: str):
        self.filename = _file_name

    def write_data(self, data: str) -> None:
        print("Writing data")

    def read_data(self) -> None:
        print("Reading data")


class DataSourceDecorator(DataSource):
    data_source: DataSource

    def __init__(self, _data_source):
        self.data_source = _data_source

    @abstractmethod
    def write_data(self, data: str) -> None:
        self.data_source.write_data(data)

    @abstractmethod
    def read_data(self) -> None:
        self.data_source.read_data()


class DataSourceEncryptionDecorator(DataSourceDecorator):
    def write_data(self, data: str) -> None:
        print("Encrypting data")
        super().write_data(data)

    def read_data(self) -> None:
        print("Decrypting data")
        super().read_data()


class DataSourceCompressionDecorator(DataSourceDecorator):
    def write_data(self, data: str) -> None:
        print("Compressing data")
        super().write_data(data)

    def read_data(self) -> None:
        print("Decompressing data")
        super().read_data()


def program(_data_source: DataSource):
    _data_source.write_data("Hello world!")
    _data_source.read_data()


data_source = FileDataSource(_file_name="test.txt")
data_source_with_encryption = DataSourceEncryptionDecorator(data_source)
data_source_with_compression = DataSourceCompressionDecorator(data_source_with_encryption)
program(data_source_with_compression)
