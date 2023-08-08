# Тут будут генерироваться данные
# Для генерации данных потребуется новая библиотека. Установлю с помощью pip install faker
import random

# Импортирую только что созданный Person
from data.data import Person
# И библиотеку что генерирует данные
from faker import Faker

# Указываю ей язык для генерации
faker_en = Faker('En')

# И создаю класс с возвращаемыми значениями
def generated_person():
    # Возвращаю его же, но уже с сгенерированными данными
    return Person(
        # Заполняю поля
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        mobile=faker_en.msisdn(),
        subject='English'
    )

# Теперь нужно создать сам генерируемый файл
def generated_file():
    # Теперь нужен абсолютный путь к файлу генерации
    # Использую r и f для указания random в пути
    path = rf'C:\Проекты\Demoqa_test_python\test{random.randint(10,100)}.txt'
    # Теперь указываю переменную файла и где он будет создан
    # Так же, в соответствии с документацией использую метод W
    file = open(path, 'w')
    # Далее определяюсь с тем что буду класть в файл
    file.write(f'Helloworld{random.randint(23, 100)}')
    # Закрываю файл после этого
    # И возвращаю путь
    return path



