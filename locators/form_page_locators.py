from selenium.webdriver.common.by import By
# Импортирую рандом, что бы использовать случайные числа
from random import randint
# Тут я создам локаторы
class FormPageLocators:
    # Теперь разберусь с тем, какие поля и формы есть на странице и буду их находить с помощью css-селектора
    # Локаторы чаще всего пишут с UPERCASE
    FIRST_NAME = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME = (By.CSS_SELECTOR, '#lastName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    # Пол будет выбираться случайным образом с помощью f{randint(1,3)}
    GENDER = (By.CSS_SELECTOR, f'label[for="gender-radio-{randint(1,3)}"]')
    MOBILE = (By.CSS_SELECTOR, '#userNumber')
    SUBJECT = (By.CSS_SELECTOR, '#subjectsInput')
    HOBBIES = (By.CSS_SELECTOR, f'label[for="hobbies-checkbox-{randint(1,3)}"]')
    # Благодоря значению атрибута type="file" можно не открывая окно выбора сразу отправить файл
    FILE_INPUT = (By.CSS_SELECTOR, '#uploadPicture')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    SUBMIT = (By.CSS_SELECTOR, '#submit')

    # Таблица с результатами, которые появляются после submit
    # В ней я желаю получить с value - значения таблицы и буду получать с помощью xpath
    # С помощью //td[2] я буду находить значение
    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')