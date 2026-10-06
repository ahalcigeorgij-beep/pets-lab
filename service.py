from models import Owner, Animal, Dog, Cat, Vet, Appointment
from exceptions import NotFoundError, ValidationError


class PetsService:
    def __init__(self):
        self.owners = {}
        self.animals = {}
        self.vets = {}
        self.appointments = {}

    def _add(self, storage, obj, label):
        if obj.id in storage:
            raise ValidationError(f"{label} с ID {obj.id} уже есть")
        storage[obj.id] = obj

    def _get(self, storage, obj_id, label):
        if obj_id not in storage:
            raise NotFoundError(f"{label} с ID {obj_id} не найден")
        return storage[obj_id]

    def _delete(self, storage, obj_id, label):
        self._get(storage, obj_id, label)
        del storage[obj_id]

    # Публичные обёртки CRUD
    def add_owner(self, o):
        self._add(self.owners, o, "Владелец")

    def get_owner(self, i):
        return self._get(self.owners, i, "Владелец")

    def del_owner(self, i):
        self._delete(self.owners, i, "Владелец")

    def add_animal(self, a):
        self._add(self.animals, a, "Животное")

    def get_animal(self, i):
        return self._get(self.animals, i, "Животное")

    def del_animal(self, i):
        self._delete(self.animals, i, "Животное")

    def add_vet(self, v):
        self._add(self.vets, v, "Ветеринар")

    def get_vet(self, i):
        return self._get(self.vets, i, "Ветеринар")

    def del_vet(self, i):
        self._delete(self.vets, i, "Ветеринар")

    def add_appt(self, p):
        self._add(self.appointments, p, "Приём")

    def del_appt(self, i):
        self._delete(self.appointments, i, "Приём")

    # ---------- JSON ----------
    def to_dict(self):
        animals = []
        for a in self.animals.values():
            d = a.__dict__.copy()
            d["type"] = a.__class__.__name__
            animals.append(d)
        return {
            "owners": [o.__dict__ for o in self.owners.values()],
            "animals": animals,
            "vets": [v.__dict__ for v in self.vets.values()],
            "appointments": [p.__dict__ for p in self.appointments.values()],
        }

    def from_dict(self, data):
        self.owners = {o["id"]: Owner(**o) for o in data.get("owners", [])}
        self.vets = {v["id"]: Vet(**v) for v in data.get("vets", [])}
        self.appointments = {p["id"]: Appointment(**p) for p in data.get("appointments", [])}
        self.animals = {}
        for a in data.get("animals", []):
            cls = {"Dog": Dog, "Cat": Cat}.get(a.pop("type", "Animal"), Animal)
            obj = cls(**a)
            self.animals[obj.id] = obj
