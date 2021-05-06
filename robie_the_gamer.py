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
seconds = 300

# While loop
while I_want_to_play:
	current_time = time.time()
	elapsed_time = current_time - start_time

	# stoping after 5 minutes.
	if elapsed_time > seconds:
		I_want_to_play = False
		print(f"The time I have played is {round(elapsed_time,2)} seconds")
	else:
		cookie = driver.find_element_by_id("cookie")
		cookie.click()
