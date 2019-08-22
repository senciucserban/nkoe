import dataclasses
from typing import List


@dataclasses.dataclass
class Cat:
    _id: int
    name: str
    age: int
    breed: str
    medial_history: List[str] = dataclasses.field(default_factory=list)


cats = [
    Cat(_id=1, name='Oliver', age=3, breed='British Shorthair', medial_history=['FIE']),
    Cat(_id=2, name='Leo', age=16, breed='British Shorthair', medial_history=['FIE']),
    Cat(_id=3, name='Charlie', age=7, breed='British Shorthair', medial_history=['FCV']),
    Cat(_id=4, name='Milo', age=1, breed='Ragdoll', medial_history=[]),
    Cat(_id=5, name='Luna', age=10, breed='Russian Blue', medial_history=['FHV-1']),
    Cat(_id=6, name='Chloe', age=20, breed='Scottish Fold', medial_history=['FIE', 'FeLV', 'FCV']),
    Cat(_id=7, name='Bella', age=6, breed='Scottish Fold', medial_history=['FeLV', 'FIE']),
    Cat(_id=8, name='Lucy', age=4, breed='Ragdoll', medial_history=['FHW-1', 'FIE'])
]
