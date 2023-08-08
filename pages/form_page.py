# Тут я создам класс с медодами для работы со страничками
import os
import time

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from pages.base_page import BasePage
# Так же нужно добавить локаторы, что бы использовать их из этого файла. Так же добавлю ему псевдоним,
# что бы выглядел покрасивее
from locators.form_page_locators import FormPageLocators as Locators

class FormPage(BasePage):
    # Первый метод, что я создам будет связан с методом заполнения полей и отправкой
    def fill_fields_and_submit(self):


        # Укажу переменные с данными, что бы потом сравнить их с результатом
        # first_name = 'Hello'
        # last_name = 'World'
        # email = 'hello@world.com'

        # Теперь объявляю класс с сгенерированными данными
        person = generated_person()
        # И указываю path
        path = generated_file()

        # Добавляю метод - удаляющий рекламу
        self.remove_footer()

        # В начале нужно все эти поля найти и ожидать их видимость
        # Копировать помогает ctrl + d
        # Для заполнения поля использую метод sendKeys и помещаю туда переменную, обращаясь к методу person
        self.element_is_visivle(Locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visivle(Locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visivle(Locators.EMAIL).send_keys(person.email)
        # Тут я использую click потому-что это кнопка radio и рандом с помощью локатора
        self.element_is_visivle(Locators.GENDER).click()
        self.element_is_visivle(Locators.MOBILE).send_keys(person.mobile)
        # Поскольку это поле имеет падающий список, лучше использовать каждый пункт поочередно
        # Один из вариантов найти ВЕСЬ список это перейти в DevTools > Приложение > Фреймы > bundle.js и найти в нем весь список
        # Но я установлю только English и запишу его в переменную, т.к. на него еще надо нажать
        subject = self.element_is_visivle(Locators.SUBJECT)
        subject.send_keys(person.subject)
        # Что-бы подтвердить выбор в падающем списке использую enter
        subject.send_keys(Keys.RETURN)
        self.element_is_visivle(Locators.SUBJECT).send_keys()
        self.element_is_visivle(Locators.HOBBIES).click()
        # Для передачи файла нужен абсолютный путь к нему и можно использовать все тот же sendKeys
        # Для отмены экранирования символов использую r в начале
        self.element_is_visivle(Locators.FILE_INPUT).send_keys(path)
        # Удаляю сгенерированный файл
        os.remove(path)
        self.element_is_visivle(Locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visivle(Locators.SUBMIT).click()
        # Возвращаю то, что я буду сравнивать с результатом
        return person

    # Теперь напишу метод, что будет возвращать результат таблицы из demoqa
    def form_result(self):
        # Теперь ожидаю появление всех элементов и помещаю их в переменную
        result_list = self.elements_are_visible(Locators.RESULT_TABLE)
        # Далее есть два метода нахождения каждого элемента

        # Первый - с помощью цикла:
        #result_text = []
        #for i in result_list:
        #    # Беру каждый элемент, извлекаю из него текст и помещаю в массив
        #    result_text.append(i.text)

        # Второй метод
        result_text = [i.text for i in result_list]

        # Возвращаемое значение для обоих методов одинаковое
        return result_text

        # Что бы накликать в много мест можно использовать ALT


