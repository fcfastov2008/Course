from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

username = "guest"
password = "welcome2qauto"


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:

    login_url = f"https://{username}:{password}@qauto2.forstudy.space/"
    driver.get(login_url)


    wait = WebDriverWait(driver, 10)


    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']")))
    print("Авторизація пройшла успішно!")


    vehicles_header = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Your Vehicles')]")))
    print("Знайдено заголовок:", vehicles_header.text)


    add_vehicle_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-add-vehicle")))
    add_vehicle_button.click()
    print("Натиснуто кнопку 'Add Vehicle'")


    name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='name']")))
    name_input.send_keys("Ford")

    license_input = driver.find_element(By.CSS_SELECTOR, "input[name='license']")
    license_input.send_keys("AA1234BB")


    save_button = driver.find_element(By.XPATH, "//button[text()='Save']")
    save_button.click()
    print("Додано новий автомобіль!")

finally:

    driver.quit()