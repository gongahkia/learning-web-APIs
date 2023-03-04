import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chromehand = webdriver.Chrome('../../../chromedriver.exe')
chromehand.get("https://lichess.org/login?referrer=/")
assert "lichess" in chromehand.title

# ----------

# (1) Logging in

login_username = chromehand.find_element(By.NAME, "username")
login_password = chromehand.find_element(By.NAME, "password")
submit_button = chromehand.find_element(By.XPATH, '//button[text()="Sign in"]')

# remember to hash out my actual username and password before pushing this to Git for the FINAL time
login_username.send_keys("angryapplegravy@gmail.com")
login_password.send_keys("mihri0-saMheh-gywcef")
submit_button.click()

time.sleep(40)

# ------------

# (2) try implementing pyautogui to click stuff

chromehand.close()