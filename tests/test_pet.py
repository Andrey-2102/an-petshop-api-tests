import allure
import requests


# BASE_URL = 'https://petstore.swagger.rv-school.ru/'  // Неразрешённый метод (405)
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
                # assert response.status_code == 201, "Статус код != 200" # Проверка с ошибкой
                print(response.status_code)  # Вывод: 200
                print(response.text)  # Вывод: Pet deleted
                print(response.headers["Content-Type"])  # Вывод: application/json
                print(response.url)  # Вывод: https://petstore.swagger.rv-school.ru/api/v3/pet/9999
                print(response.request.method)  # Вывод: DELETE
                assert response.status_code == 200, "Статус код != 200"
            with allure.step('Проверка текстового содержимого ответа'):
                # assert response.text == 'Pet delete d', "Текст ошибки не совпал с ожидаемым" # Проверка с ошибкой
                assert response.text == 'Pet deleted', "Текст ошибки не совпал с ожидаемым"


# response.headers["Content-Type"]:
# {'Server': 'nginx/1.26.3', 'Date': 'Wed, 28 Oct 2026 16:52:49 GMT',
#  'Content-Type': 'application/json', 'Content-Length': '11'...
#  'Access-Control-Allow-Headers': 'Content-Type, api_key, Authorization',
#  'Access-Control-Expose-Headers': 'Content-Disposition'}