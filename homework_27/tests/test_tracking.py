import pytest

@pytest.mark.usefixtures("tracking_page")
def test_tracking_status(tracking_page):
    # Вхідні дані для тесту
    tracking_number = "12345678000123"
    expected_status = ("Ми не знайшли посилку за таким номером. Можливо, вона ще не "
                       "передана для відправлення, або номер некоректний. Перевірте, чи "
                       "відповідає вказаний номер можливому формату: 59500000031324 або AENM0002497278NPI.")

    # Виконання дій
    tracking_page.enter_tracking_number(tracking_number)
    tracking_page.click_search()
    actual_status = tracking_page.get_status()

    # Перевірка результату
    assert actual_status == expected_status, f"Очікувалося: {expected_status}, отримано: {actual_status}"