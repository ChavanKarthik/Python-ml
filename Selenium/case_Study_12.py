# importing required libraries
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# open firefox browser
browser = webdriver.Firefox()


def open_browser(url):
    # open required url
    browser.get(url)


def close_browser():
    browser.close()


guru99 = 'http://demo.guru99.com/payment-gateway/purchasetoy.php'


def case_study_12_scenario1():
    open_browser(guru99)

    # click on generate card number button, opens a new tab
    browser.find_element_by_xpath("//nav[@id='nav']//a[contains(text(),'Generate Card Number')]").click()
    browser.implicitly_wait(2000)

    # change focus to new tab
    window_after = browser.window_handles[1]
    browser.switch_to_window(window_after)

    # scroll-down till buy now button
    actions = ActionChains(browser)
    actions.send_keys(Keys.PAGE_DOWN).perform()

    act_card_number = browser.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/h4[1]").text
    exp_card_number = 'Card Number:-'
    act_cvv_number = browser.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/h4[2]").text
    exp_cvv_number = 'CVV:-'
    time.sleep(2)

    # close the new window
    close_browser()
    time.sleep(2)

    # Validate that tab has been closed successfully
    try:
        browser.switch_to_window(window_after)
    except Exception:
        print("New tab has been successfully close")

    # Validate credit card number and cvv number
    assert exp_card_number in act_card_number
    assert exp_cvv_number in act_cvv_number

    print("All Asserts of case_study_12_scenario1 has passed")

    browser.quit()


beesheets = 'http://192.168.5.214:8081/beesheets/html/Admin/admin.html'


def case_study_12_scenario2():
    open_browser(beesheets)

    # login
    username = 'admin1'
    password = 'beehyv'
    browser.find_element_by_xpath('//input[@name="j_username"]').send_keys(username)
    browser.find_element_by_xpath("//input[@name='j_password']").send_keys(password)
    browser.find_element_by_xpath('//*[@id="form"]/form/input[3]').click()

    # navigate to admin tab
    browser.find_element_by_id("admin-tab").click()

    # navigate to back page
    browser.back()
    exp_url_after_back_button = 'http://192.168.5.214:8081/beesheets/html/profiles.html'
    act_url_after_back_button = browser.current_url
    # Validate url after going to back button
    assert exp_url_after_back_button == act_url_after_back_button

    # navigate to forward page
    browser.forward()
    exp_url_after_forward_button = 'http://192.168.5.214:8081/beesheets/html/Admin/admin.html'
    act_url_after_forward_button = browser.current_url
    # Validate url after going to forward button
    assert exp_url_after_forward_button == act_url_after_forward_button

    # Refresh the current page
    browser.refresh()
    exp_url_after_page_refresh = 'http://192.168.5.214:8081/beesheets/html/Admin/admin.html'
    act_url_after_page_refresh = browser.current_url
    # Validate url after going to refresh button
    assert exp_url_after_page_refresh == act_url_after_page_refresh

    print("All Asserts of case_study_12_scenario2 has passed")

    browser.close()


case_study_12_scenario1()

# Re-open firefox browser
browser = webdriver.Firefox()
case_study_12_scenario2()
