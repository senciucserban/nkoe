import dataclasses
from typing import List

from jara.types import enforce_types


@enforce_types
@dataclasses.dataclass
class Cat:
    pk: int
    name: str
    age: int
    breed: str
    vaccines: List[str] = dataclasses.field(default_factory=list)

    @property
    def as_dict(self):
        return dataclasses.asdict(self)

    def __eq__(self, other) -> bool:
        return (self.pk == other.pk) or (self.name == other.name and self.breed == other.breed)


cats = [
    Cat(pk=1, name='Oliver', age=3, breed='British Shorthair', vaccines=['FIE']),
    Cat(pk=2, name='Leo', age=16, breed='British Shorthair', vaccines=['FIE']),
    Cat(pk=3, name='Charlie', age=7, breed='British Shorthair', vaccines=['FCV']),
    Cat(pk=4, name='Milo', age=1, breed='Ragdoll'),
    Cat(pk=5, name='Luna', age=10, breed='Russian Blue', vaccines=['FHV-1']),
    Cat(pk=6, name='Chloe', age=20, breed='Scottish Fold', vaccines=['FIE', 'FELV', 'FCV']),
    Cat(pk=7, name='Bella', age=6, breed='Scottish Fold', vaccines=['FELV', 'FIE']),
    Cat(pk=8, name='Lucy', age=4, breed='Ragdoll', vaccines=['FHW-1', 'FIE'])
]
