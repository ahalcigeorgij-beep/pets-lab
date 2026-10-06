from exceptions import PetsError
from models import Owner, Dog, Cat, Vet, Appointment
from service import PetsService
from storage import save_json, load_json

PATH = "data/data.json"


def main():
    s = PetsService()
    while True:
        print("\n1+собака 2+кошка 3+владелец 4+ветеринар 5+приём "
              "6-показать 7-сохранить 8-загрузить 9-удалить 0-выход")
        try:
            c = input("> ").strip()

            if c == "1":
                s.add_animal(Dog(int(input("ID: ")), input("Кличка: "),
                                 int(input("Возраст: ")), float(input("Вес: ")),
                                 input("Порода: ")))
            elif c == "2":
                s.add_animal(Cat(int(input("ID: ")), input("Кличка: "),
                                 int(input("Возраст: ")), float(input("Вес: ")),
                                 input("Домашняя? y/n: ").lower() == "y"))
            elif c == "3":
                s.add_owner(Owner(int(input("ID: ")), input("ФИО: "), input("Телефон: ")))
            elif c == "4":
                s.add_vet(Vet(int(input("ID: ")), input("ФИО: "), input("Спец: ")))
            elif c == "5":
                s.add_appt(Appointment(int(input("ID: ")), int(input("ID животного: ")),
                                       int(input("ID вета: ")), input("Дата: "), input("Причина: ")))
            elif c == "6":
                for a in s.animals.values():
                    print(a.describe())
                for o in s.owners.values():
                    print(f"Владелец: {o.full_name}, {o.phone}")
            elif c == "7":
                save_json(s.to_dict(), PATH)
                print("Сохранено")
            elif c == "8":
                s.from_dict(load_json(PATH))
                print("Загружено")
            elif c == "9":
                s.del_animal(int(input("ID животного: ")))
                print("Удалено")
            elif c == "0":
                break

        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except PetsError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Непредвиденная: {e}")


if __name__ == "__main__":
    main()
