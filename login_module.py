from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

# Konfigurasi URL dan field login
credentials = {
    'siakad': {
        'url': 'https://elearning.utdi.ac.id/login',
        'username_field': 'username',
        'password_field': 'password'
    }
}

def fill_and_submit_form(service, username, password, screenshot_path="hasil_login.png"):
    config = credentials[service]
    url = config['url']
    username_field = config['username_field']
    password_field = config['password_field']

    # Konfigurasi opsi Chrome untuk server
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Mode tanpa GUI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = "/usr/bin/chromium"  # Lokasi Chromium di container

    # Gunakan Service object sesuai dengan Selenium 4
    service_obj = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service_obj, options=options)

    try:
        driver.get(url)
        time.sleep(2)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, username_field))
        ).send_keys(username)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, password_field))
        ).send_keys(password)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn"))
        ).click()

        time.sleep(5)

        # Screenshot tampilan setelah login
        driver.save_screenshot(screenshot_path)
        return True, screenshot_path

    except Exception as e:
        return False, str(e)

    finally:
        driver.quit()
