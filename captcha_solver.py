# captcha_solver.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import io
import pytesseract
import re

def solve_captcha(driver):
    captcha_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'captcha_img'))
    )

    location = captcha_element.location
    size = captcha_element.size

    captcha_image = driver.get_screenshot_as_png()
    captcha_image = Image.open(io.BytesIO(captcha_image))
    captcha_image = captcha_image.crop((location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height']))

    captcha_image.save('captcha_screenshot.png')

    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

    text = pytesseract.image_to_string(captcha_image)
    numbers = re.findall(r'\d+', text)
    captcha_sum = sum(map(int, numbers))

    return captcha_sum
