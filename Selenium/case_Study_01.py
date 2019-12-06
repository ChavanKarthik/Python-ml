# importing required libraries
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# open firefox browser
browser = webdriver.Firefox()

# open required url
browser.get('http://demo.guru99.com/payment-gateway/index.php')
actions = ActionChains(browser)

# scroll-down till buy now button
actions.send_keys(Keys.PAGE_DOWN)
actions.perform()

# xpath for Buy Now button
p_buy_now_button = browser.find_element_by_xpath('//input[@class="button special"]')
# click on buy now button
p_buy_now_button.click()
time.sleep(4)

# xpath for card_number input field
p_card_number = '//input[@id="card_nmuber"]'
card_number_field = browser.find_element_by_xpath(p_card_number)
card_number = '4832451994589738'
card_number_field.send_keys(card_number)

# selecting expiration month
expiration_month = '1'
select_expiration_month = Select(browser.find_element_by_id('month'))
select_expiration_month.select_by_value(expiration_month)

# xpath for expiration_year drop down
expiration_year = '2021'
select_expiration_year = Select(browser.find_element_by_id('year'))
select_expiration_year.select_by_value(expiration_year)

# xpath for cvv code input field
p_cvv_code = '//input[@id="cvv_code"]'
cvv_code = '999'
cvv_code_field = browser.find_element_by_xpath(p_cvv_code)
cvv_code_field.send_keys(cvv_code)

# scroll-down till buy now button
# actions.send_keys(Keys.PAGE_DOWN)
# actions.perform()
time.sleep(2)

# xpath for Submit button
p_submit_button = browser.find_element_by_xpath('//input[@type="submit"][@name="submit"][@class="button special"]')
p_submit_button.click()

# click on buy now button
time.sleep(2)

assert "Payment successfull!" in browser.page_source
assert "Order ID" in browser.page_source
assert "Please Note Down Your OrderID" in browser.page_source
print("Actions from launching browser to booking are successfully completed")

browser.close()
