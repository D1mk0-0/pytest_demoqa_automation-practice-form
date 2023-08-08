# Базовая страница от которой будут наследоваться все остальные страницы
# В нее я положу базовые методы, которые многократно можно использовать

# self - условное обозначение (вместо него можно использовать другое), позволяет выдергивать методы из других классов*
# self - указывает "Ищи эту функцию, параметр внутри этого класса"*

# Импортирую метод ожидания и назову его более понятно
from selenium.webdriver.support.ui import WebDriverWait as Wait

# Импортирую метод выбора чего ожидать и его назову попроще
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    # Создам функцию принимающую 2 основных параметра
    def __init__(self, driver, url):
        # При открытии страницы необходим driver и url
        self.driver = driver
        self.url = url

    # Самое главное - создам функцию открытия страницы
    def open(self):
        self.driver.get(self.url)

    # Напишу несколько оберточных функции, что бы не прописывать каждое действие
    # Первая будет искать толлько тот элемент, который driver видит
    # Передавать в него я буду сам локатор и таймаут что-бы не указывать time.sleep для каждого
    # И теперь ожидание будет идти ровно столько, сколько нужно для появления
    def element_is_visivle(self, locator, timeout=5):
        # Теперь я буду возвращать ожидание
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    # Далее подготавливаю метод выбора нескольких элементов и ожидание их видимости
    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    # Теперь для клика по submit мне мешает реклама, т.к. она перекрывает ее
    # Эту рекламу нужно скрыть при помощи скрипта
    def remove_footer(self):
        # Использую метот, который позволяет выполнять скрипты js
        # Нахожу этот элемент в консоли DevTools
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        # Так же убираю какую-то фигню, что появилась на месте убранной рекламы
        self.driver.execute_script("document.getElementById('close-fixedban').style.display='none';")

