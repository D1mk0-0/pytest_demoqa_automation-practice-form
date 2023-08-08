# На этой странице открывать и запускать тесты
from pages.form_page import FormPage


class TestFormPage:
    # Создам в нем функцию в которой буду использовать фикстуры
    def test_form(self, driver):
        # Обращаемся к методу класса/объекта, в котором уже написаны driver и url
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        # На этом этапе можно в тестовых рамках запустить автотест.
        # Запускать следует из самой старшей папки

        # Теперь можно запустить уже написанную функцию
        # Приравняю к ней переменные
        person = form_page.fill_fields_and_submit()
        result = form_page.form_result()

        # В тестовых рамках, для просмотра результата
        # print(person)
        # print(result)

        # Теперь я использую ключевое слово assert для сравнения разультата переменной и массива
        # Стоит понимать, что массив с результатами возвращается в другом формате, нежели те перменные, что у меня записаны
        # Т.е. в result_list у меня лежит переменная 'Hello world', а в переменных иначе
        # Так же добавлю сообщение если что то не так
        assert f'{person.first_name} {person.last_name}' == result[0], 'the form has not been filled'
        # Еще один для email
        assert person.email == result[1], 'the form has not been filled'
