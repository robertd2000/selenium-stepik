import time
from math import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
from selenium import webdriver

#
# link = 'http://suninjuly.github.io/execute_script.html'
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
# num = browser.find_element_by_id('input_value').text
# res = log(abs(12 * sin(int(num))))
#     print(res)
#     input_field = browser.find_element_by_id('answer')
#     browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)
#
#     input_field.send_keys(str(res))
#     robotCheckbox = browser.find_element_by_id('robotCheckbox').click()
#     robotsRule = browser.find_element_by_id('robotsRule').click()
#
#     button = browser.find_element_by_class_name('btn')
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     button.click()
# except Exception as ex:
#     print(ex)
#
# finally:
#     time.sleep(10)
#     browser.quit()


# link = 'http://suninjuly.github.io/file_input.html'
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     browser.find_element_by_name('firstname').send_keys('firstname')
#     browser.find_element_by_name('lastname').send_keys('lastname')
#     browser.find_element_by_name('email').send_keys('email')
#
#     file_path = os.path.join(current_dir, 'file.txt')
#     browser.find_element_by_id('file').send_keys(file_path)
#     browser.find_element_by_class_name('btn').click()
#
# except Exception as ex:
#     print(ex)
#
# finally:
#     time.sleep(10)
#     browser.quit()
#
# link = 'http://suninjuly.github.io/redirect_accept.html'
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     browser.find_element_by_tag_name('button').click()
#     # browser.switch_to.alert.accept()
#     browser.switch_to.window(browser.window_handles[1])
#     num = browser.find_element_by_id('input_value').text
#     res = log(abs(12 * sin(int(num))))
#     browser.find_element_by_id('answer').send_keys(str(res))
#     browser.find_element_by_class_name('btn').click()
# except Exception as ex:
#     print(ex)
#
# finally:
#     time.sleep(10)
#     browser.quit()

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_id('book')
    text = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button.click()
    num = browser.find_element_by_id('input_value').text
    res = log(abs(12 * sin(int(num))))
    browser.find_element_by_id('answer').send_keys(str(res))
    button = browser.find_element_by_id('solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
except Exception as ex:
    print(ex)

finally:
    time.sleep(10)
    browser.quit()
