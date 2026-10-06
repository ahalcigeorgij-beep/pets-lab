from dataclasses import dataclass
from exceptions import ValidationError


@dataclass
class Owner:
    """Владелец. Здесь есть аннотации типов."""
    id: int
    full_name: str
    phone: str

    def __post_init__(self) -> None:
        if not self.full_name.strip():
            raise ValidationError("Имя пустое")
        if len(self.phone) < 5:
            raise ValidationError("Телефон короткий")


@dataclass
class Animal:
    id: int
    name: str
    age: int
    weight: float = 0.0

    def __post_init__(self):
        if not self.name.strip():
            raise ValidationError("Кличка пустая")
        if self.age < 0 or self.weight < 0:
            raise ValidationError("Возраст/вес отрицательные")

    def describe(self):
        return f"{self.name}, {self.age} лет, {self.weight} кг"


@dataclass
class Dog(Animal):
    breed: str = "?"

    def describe(self):
        return f"Собака {self.name}, порода {self.breed}"


@dataclass
class Cat(Animal):
    indoor: bool = True

    def describe(self):
        return f"Кошка {self.name}, {'домашняя' if self.indoor else 'уличная'}"


@dataclass
class Vet:
    id: int
    full_name: str
    specialization: str = "терапевт"


@dataclass
class Appointment:
    id: int
    animal_id: int
    vet_id: int
    date: str
    reason: str = ""
