from dataclasses import dataclass, asdict


@dataclass
class Common:
    @property
    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Document(Common):
    @classmethod
    def get_validator(cls) -> dict:
        raise NotImplementedError

    @classmethod
    def create_index(cls, collection):
        raise NotImplementedError

    @classmethod
    def create_collection(cls, db, key):
        db.create_collection(key, validator=cls.get_validator())
        cls.create_index(db[key])


@dataclass
class EmbeddedDocument(Common):
    @classmethod
    def get_sub_validator(cls) -> dict:
        raise NotImplementedError
