import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get("https://userinyerface.com/game.html")

wait = WebDriverWait(driver, 10)

# Locate the elements
eleCookiesDiv = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.cookies')))
background_color = eleCookiesDiv.value_of_css_property("background-color")
height = float(eleCookiesDiv.size['height'])
print(background_color == "rgba(255, 0, 0, 1)")
print(height == 155.2)

eleCookiesDiv2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.logo__icon')))
width = eleCookiesDiv2.value_of_css_property("width")
height = float(eleCookiesDiv2.size['height'])  # Convert height to float
print(width == '300px')
print(height == 175)

eleCookiesDiv3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.login-form__container')))
background_color = eleCookiesDiv3.value_of_css_property("background-color")
print(background_color == "rgba(0, 0, 0, 0)")

eleCookiesDiv4 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.input.input--blue.input--gray')))
width = eleCookiesDiv4.value_of_css_property("width")
height = eleCookiesDiv4.value_of_css_property("height")
print(width == '372px')
print(height == '40px')
