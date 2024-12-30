import os
import logging
from datetime import datetime
import pytest
import requests
from requests.auth import HTTPBasicAuth


log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_search.log')
print(f"Шлях до лог файлу: {log_file_path}")

try:
    with open(log_file_path, 'a') as f:
        f.write('')
    print(f"Лог створено: {log_file_path}")
except Exception as e:
    print(f"Не вдалось створитилог файл: {e}")


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

for handler in logger.handlers[:]:
    logger.removeHandler(handler)

file_handler = logging.FileHandler(log_file_path, mode='a', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.debug("Повідомлення для дебагу")
logger.info("Інформаційне повідомлення")
logger.warning("Попереджувальне повідомлення")



class TestCarsAPI:
    BASE_URL = 'http://127.0.0.1:8080'

    @pytest.fixture(scope='class')
    def auth_session(self):
        logger.info("=" * 50)
        logger.info("Початок процесу аутентифікації")
        session = requests.Session()

        try:
            auth_url = f"{self.BASE_URL}/auth"
            logger.info(f"Спроба аутентифікації: {auth_url}")

            response = session.post(
                auth_url,
                auth=HTTPBasicAuth('test_user', 'test_pass')
            )
            response.raise_for_status()

            token = response.json()['access_token']
            session.headers.update({'Authorization': f'Bearer {token}'})
            logger.info("Аутентифікація успішна. Токен отримано.")
        except Exception as e:
            logger.error(f"Помилка під час аутентифікації: {e}")
            pytest.fail("Не вдалося аутентифікуватися")

        return session

    @pytest.mark.parametrize("sort_by, limit", [
        ("price", 5),
        ("year", 3),
        ("engine_volume", 7),
        ("brand", 10),
        (None, None),
    ])
    def test_search_cars(self, auth_session, sort_by, limit):
        logger.info("=" * 50)
        logger.info(f"Запуск тесту: sort_by={sort_by}, limit={limit}")
        params = {}
        if sort_by:
            params["sort_by"] = sort_by
        if limit:
            params["limit"] = limit

        try:
            response = auth_session.get(f"{self.BASE_URL}/cars", params=params)
            response.raise_for_status()
            cars = response.json()

            logger.info(f"Успішно отримано {len(cars)} автомобілів")
            assert isinstance(cars, list), "Відповідь повинна бути списком"
            if limit:
                assert len(cars) <= limit, "Кількість записів перевищує зазначений limit"
            if sort_by:
                assert cars == sorted(cars, key=lambda x: x.get(sort_by)), f"Сортування за {sort_by} некоректне"
        except Exception as e:
            logger.error(f"Помилка під час виконання тесту: {e}")
            pytest.fail("Запит до API завершився невдачею")