from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
from math import log, sin


link = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(log(abs(12*sin(int(x)))))



try:

    price = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element_by_id("book").click()
    
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    
    answer = browser.find_element_by_id("answer").send_keys(y)
    button = browser.find_element_by_id("solve").click()
    print(browser.switch_to.alert.text.split(':')[-1])
    


finally:
    #time.sleep(15)
    browser.quit()
