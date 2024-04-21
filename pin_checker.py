# pin_checker.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from captcha_solver import solve_captcha
from web_driver import create_web_driver
import time

class PinChecker:
    def __init__(self, chromedriver_path):
        self.driver = create_web_driver(chromedriver_path)

    def process_pin(self, pin):
        self.driver.get('https://itax.kra.go.ke/KRA-Portal/pinChecker.htm')

        try:
            pin_input = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, 'vo.pinNo'))
            )
            pin_input.send_keys(pin)
            time.sleep(2)

            captcha_sum = solve_captcha(self.driver)

            captcha_input = self.driver.find_element(By.NAME, 'captcahText')
            captcha_input.send_keys(str(captcha_sum))

            self.driver.execute_script("ajaxCaptchaLoad()")
            time.sleep(2)

            captcha_sum = solve_captcha(self.driver)

            captcha_input.clear()
            captcha_input.send_keys(str(captcha_sum))

            time.sleep(5)

        finally:
            self.driver.quit()
