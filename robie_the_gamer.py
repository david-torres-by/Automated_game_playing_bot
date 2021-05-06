# Is this web driver, that is going to be driving and doing all of our automated tasks
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path= chrome_driver_path)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Variables to start the game
I_want_to_play = True
start_time = time.time()
seconds = 2400

# While loop
while I_want_to_play:
	current_time = time.time()
	elapsed_time = round(current_time - start_time,0)
	print(elapsed_time)

	# stoping after 5 minutes.
	if elapsed_time > seconds:
		I_want_to_play = False
		print(f"The time I have played is {round(elapsed_time,0)} seconds")
	elif 20 <= elapsed_time <= 23:
		time.sleep(.1)
		cursor = driver.find_element_by_id("buyCursor")
		cursor.click()
		elapsed_time += 1
	elif 200 <= elapsed_time <= 207:
		time.sleep(.1)
		cursor = driver.find_element_by_id("buyGrandma")
		cursor.click()
		elapsed_time += 1
	elif 400 <= elapsed_time <= 407:
		time.sleep(.1)
		cursor = driver.find_element_by_id("buyFactory")
		cursor.click()
		elapsed_time += 1
	elif 600 <= elapsed_time <= 610:
		time.sleep(.1)
		cursor = driver.find_element_by_id("buyCursor")
		cursor.click()
		elapsed_time += 1
	elif 800 <= elapsed_time <= 810:
		time.sleep(.1)
		cursor = driver.find_element_by_id("buyMine")
		cursor.click()
		elapsed_time += 1
	elif 1000 <= elapsed_time <= 1010:
		time.sleep(.1)
		cursor = driver.find_element_by_id("buyAlchemy lab")
		cursor.click()
		elapsed_time += 1
	elif 1200 <= elapsed_time <= 1210:
		time.sleep(.1)
		cursor = driver.find_element_by_id("buyGrandma")
		cursor.click()
		elapsed_time += 1
	elif 1400 <= elapsed_time <= 1410:
		time.sleep(.1)
		cursor = driver.find_element_by_id("buyPortal")
		cursor.click()
		elapsed_time += 1
	elif 1700 <= elapsed_time <= 1710:
		time.sleep(.1)
		cursor = driver.find_element_by_id("buyTime machine")
		cursor.click()
		elapsed_time += 1
	elif 2000 <= elapsed_time <= 2010:
		time.sleep(.1)
		cursor = driver.find_element_by_id("buyAlchemy lab")
		cursor.click()
		elapsed_time += 1
	else:
		cookie = driver.find_element_by_id("cookie")
		cookie.click()
		elapsed_time += 1
