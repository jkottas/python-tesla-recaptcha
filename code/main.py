from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions
import time
import pyautogui

# declare and initialize driver variable
driver=webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
try:
  base_url="https://www.omaze.com/products/custom-tesla-model-x"
  print("Base URL is " + base_url)
  # browser should be loaded in maximized window
  driver.maximize_window()
  # driver should wait implicitly for a given duration, for the element under consideration to load.
  # to enforce this setting we will use builtin implicitly_wait() function of our 'driver' object.
  driver.implicitly_wait(10) #10 is in seconds
  # to load a given URL in browser window
  driver.get(base_url)
  entryLink = driver.find_element(By.LINK_TEXT, 'enter without contributing')
  print("entry link is")
  print(entryLink)
  # TODO: wait an arbitrary amount of time
  entryLink.click()
  time.sleep(2)

  #fill in first name
  #fill in last name
  #fill in email address
  #fill in address
  #fill in city
  #fill in country
  #fill in zip
  #click recaptcha
  recaptchaX = 0
  recaptchaY = 0
  recaptchaBox = driver.find_elements_by_xpath("//*[contains(@data-callback, 'iAmNotARobot')]")
  #recaptchaBox = driver.find_elements_by_xpath("//*[contains(@src, 'recaptcha')]") # returns 4 fields - can't figure out which one is our iframe
  #recaptchaBox = driver.find_elements_by_xpath("//*[contains(@class, 'fame-field__input')]") # works - finds many input fields
  print("recaptcha:")
  print(recaptchaBox)
  for i,r in enumerate(recaptchaBox):
    print (i,r.get_property('attributes')[0])  
    print ("location " + str(r.location))
    print ("size " + str(r.size))
  if (len(recaptchaBox) != 1):
      print("Bailing because I couldn't uniquely identify the recaptcha box. There were " + str(len(recaptchaBox)) + " possibilities")
      quit()

  # TODO: now that we've got an iframe size and location, use python to move and click the mouse

  # TODO: if above fails, launch chrome.exe manually, use the scroll wheel to scroll, find the button, position the mouse, make it click, etc.

  # doesn't work - waits 10 seconds and throws an exception because it never becomes clickable/findable
  # if you manually click it, you are presented with dozens of "find the traffic light" prompts
  #element = WebDriverWait(driver, 10).until(ExpectedConditions.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-checkmark")))
  #element.click()


  time.sleep(2)
except (Exception) as py_ex:
  print("Exception: ")
  print (py_ex)
  print(py_ex.args)
finally:
  driver.close()