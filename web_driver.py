# web_driver.py
from selenium import webdriver

def create_web_driver(chromedriver_path):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    chrome_options.add_argument(f"executable_path={chromedriver_path}")
    return webdriver.Chrome(options=chrome_options)
