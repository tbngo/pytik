from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def generate_driver(url: str):
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("--log-level=3")
    options.add_argument("--silent")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(url)
    return driver


def description(url: str):
    driver = generate_driver(url)
    description = driver.find_element(By.CLASS_NAME, "tt-video-meta-caption")
    return description.text


def user(url: str):
    driver = generate_driver(url)
    description = driver.find_element(By.CLASS_NAME, "author-uniqueId")
    return description.text
