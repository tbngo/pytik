from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os


def generate_driver(url: str):
    os.environ["WDM_LOG_LEVEL"] = "0"  # Supress ChromeDriverManager logs

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


description("https://www.tiktok.com/@foodies/video/6869148881230318853?lang=en")
