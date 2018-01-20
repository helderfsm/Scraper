from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 
url = 'https://www.daftlogic.com/sandbox-google-maps-find-altitude.htm'

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

driver.get(url)


coords = '41.586412,-8.582760'
form_elem = driver.find_element_by_name('goto')
form_elem.clear()
form_elem.send_keys(coords)
form_elem.send_keys(Keys.RETURN)

#time.sleep(0.1)
wait.until(EC.visibility_of_element_located((By.ID, 'outputDiv')))
sol_elem = driver.find_element_by_id('outputDiv')
sol = sol_elem.text

file_name = 'altitude.txt'
with open(file_name, 'a') as f:
    f.write(sol)
print (sol)
driver.quit()