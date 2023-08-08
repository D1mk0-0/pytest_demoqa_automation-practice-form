# Эта папка для генерируемых данных
# использую новую фикстуру как dataClass

# импортирую его
from dataclasses import dataclass

@dataclass
# Инициализирую класс который я могу использовать только для переменных
class Person:
    # Для переменных в этом классе обязательная типизация str - строковое значение
    # А так же и дефолтное значение
    first_name: str = None
    last_name: str = None
    email: str = None
    current_address: str = None
    mobile: str = None
    subject: str = None

