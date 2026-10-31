import allure
import requests


BASE_URL = 'https://petstore.swagger.rv-school.ru/api/v3'


@allure.feature('Pet')
class TestPet:
    @allure.story("Удаление питомца")
    @allure.title("Попытка удалить несуществующего питомца")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_nonexistent_pet(self):
        with allure.step('Отправка запроса на удаление несуществующего питомца'):
            response = requests.delete(url=f"{BASE_URL}/pet/9999")
            with allure.step('Проверка статуса ответа'):
                assert response.status_code == 200, "Статус код != 200"
            with allure.step('Проверка текстового содержимого ответа'):
                assert response.text == 'Pet deleted', "Текст ошибки не совпал с ожидаемым"