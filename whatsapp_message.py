#!pip install selenium
#chrome driver: https://chromedriver.storage.googleapis.com/index.html?path=2.36/
#chromium download:
#	linux: sudo apt-get install chromium-browser
#	mac or windows: https://www.chromium.org/getting-involved/download-chromium

from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
  
# Set Driver and open WhatsApp Web in Chrome
driver = webdriver.Chrome('full_path_driver/chromedriver')   
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 500) 
  
# Define Friend and Message
target = '"Friend\'s Name"'
string = "Message 1"

# Find Friend Contact
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg))) 
group_title.click()

# Find Message Input Field
inp_xpath = '//div[@class="_1awRl copyable-text selectable-text"][@data-tab="6"]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

# Send Message
for i in range(1):
	input_box.send_keys(string + Keys.ENTER)
	time.sleep(1)
