from abc import ABC


class Singleton(ABC):
    def __init__(self, _private=False):
        assert _private, "Can't instantiate singleton"


class Database(Singleton):
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = Database(_private=True)
        return cls._instance

    @classmethod
    def query(cls, query: str) -> None:
        print(f'Running {query} from {cls._instance}')


a, b = Database.get_instance(), Database.get_instance()
assert a == b, "Instances are not equal"
a.query("SELECT * FROM ...")
b.query("SELECT * FROM ...")
