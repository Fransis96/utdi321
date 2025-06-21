def fill_and_submit_form(service, username, password, screenshot_path="hasil_login.png"):
    config = credentials[service]
    url = config['url']
    username_field = config['username_field']
    password_field = config['password_field']

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Tambahkan jika ingin headless
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

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

        driver.save_screenshot(screenshot_path)
        return True, screenshot_path

    except Exception as e:
        return False, str(e)

    finally:
        driver.quit()
