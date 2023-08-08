# Это файл-плагин для pytest. Сюда я буду помещать текстуры.
# Затем в консоли проверяю установлены ли библиотеки.
# Перехожу к .\venv\Scripts\activate
# Теперь любая установка будет падать именно в окружение.
# Удостоверюсь, что pytest не установлен с помощью pytest --version
# Установлю командой pip install pytest
# Установлю так же Selenium pip install selenium
# И pip install webdriver-manager
import pytest
# Импортирую WebDriver из библиотеки, которую установил выше
from selenium import webdriver
# Импортирую сервис для управления хромом
from selenium.webdriver.chrome.service import Service
# Импортирую Chrome DriverManager
from webdriver_manager.chrome import ChromeDriverManager


# Напишу декоратор, он позволит задавать что-то до начала и после конца функции, и функцию driver
@pytest.fixture()
def driver():
    # Подключаю сервис для хрома и передаю в него ChromeDriverManager
    driver_service = Service(ChromeDriverManager().install())
    # Тут я создаю драйвер с настройками и передаю в него сервисы
    driver = webdriver.Chrome(service=driver_service)
    # Добавлю метод открытия окна браузера на весь экран
    driver.maximize_window()
    # Все что выше yield будет выполнятся до начала теста
    yield driver
    # После этого выхожу из драйвера
    driver.quit()
