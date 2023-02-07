import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://livability.com/best-places/2022-top-100-best-places-to-live-in-the-us/")

i = 0

while i < 10:
	driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
	driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_UP)
	driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_UP)
	time.sleep(1)
	i = i + 1
time.sleep(2)
items = driver.find_elements(By.CLASS_NAME, "ohl-text")

for item in items:
	h2 = item.find_element(By.TAG_NAME, "h2")
	print(h2.text)
