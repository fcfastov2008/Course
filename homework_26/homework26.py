from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


secrets = {
    "frame1": "Frame1_Secret",
    "frame2": "Frame2_Secret"
}


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:

    driver.get("http://localhost:8000/dz.html")

    wait = WebDriverWait(driver, 10)

    for frame_id, secret_text in secrets.items():

        driver.switch_to.frame(driver.find_element(By.ID, frame_id))


        input_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'input')]")))
        input_field.send_keys(secret_text)


        verify_button = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
        verify_button.click()


        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        if alert_text == "Верифікація пройшла успішно!":
            print(f"{frame_id}: Верифікація успішна!")
        else:
            print(f"{frame_id}: Помилка верифікації!")


        alert.accept()


        driver.switch_to.default_content()

finally:

    time.sleep(3)
    driver.quit()