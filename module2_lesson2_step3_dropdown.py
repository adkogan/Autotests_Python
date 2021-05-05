from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

   
    num1 =browser.find_element_by_id('num1').text
    print(num1)
    
    num2= browser.find_element_by_id('num2').text
    print(num2)
    
    sum = int(num1)+int(num2)
    print(sum)
  
    
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector(f"[value= '{sum}']").click()
  



    button = browser.find_element_by_class_name("btn")
    button.click()

finally:

    time.sleep(30)
    browser.quit()
