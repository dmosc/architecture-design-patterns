from abc import ABC


class File(ABC):
    filename: str
    format: str

    def __init__(self, _filename: str, _format: str):
        self.filename = _filename
        self.format = _format


class VideoFile(File):
    pass


class VideoConverter:
    @staticmethod
    def convert(_file: File) -> File:
        print("Doing a lot of complex things and referencing other libraries.")
        print(f"Converting {_file.filename} to {_file.format}")
        return File(_file.filename, _file.format)


converter = VideoConverter()
file = VideoFile("test.mov", "mp4")
file = converter.convert(file)
print(file)
