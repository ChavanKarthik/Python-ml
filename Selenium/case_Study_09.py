# importing required libraries
import random
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# open firefox browser
browser = webdriver.Firefox()


def open_browser(url):
    # open required url
    browser.get(url)


def close_browser():
    browser.close()


beesheets = 'http://192.168.5.214:8081/beesheets/html/Admin/admin.html'


def case_study_09():
    open_browser(beesheets)

    # login
    username = 'admin1'
    password = 'beehyv'
    browser.find_element_by_xpath('//input[@name="j_username"]').send_keys(username)
    browser.find_element_by_xpath("//input[@name='j_password']").send_keys(password)
    browser.find_element_by_xpath('//*[@id="form"]/form/input[3]').click()

    # navigate to admin tab
    browser.find_element_by_id("admin-tab").click()

    # navigate to appraisal Management tab
    browser.find_element_by_xpath("//a[@id='appraisal-Management-ref']").click()

    # click on add appraisal period
    browser.find_element_by_xpath("//span[contains(text(),'Add AppraisalPeriod')]").click()
    appraisal_title = "appraisal_test_" + str(random.randint(123123, 456546))
    # enter the appraisal name to be added
    browser.find_element_by_xpath("//body/div[4]/div[2]/div[1]/input[1]").send_keys(appraisal_title)

    # click on start date calender menu
    browser.find_element_by_xpath("//input[@class='appraisal-start-date hasDatepicker']").click()

    start_date = browser.find_element_by_xpath("//div[@id='ui-datepicker-div']//tr[2]//td[2]")  # 03-06-2019
    # pick start date and End date from calender
    actions_start_date = ActionChains(browser)
    actions_start_date.move_to_element(start_date).click().perform()

    # click on end date calender menu
    browser.find_element_by_xpath("//input[@class='appraisal-end-date hasDatepicker']").click()
    end_date = browser.find_element_by_xpath("//div[@id='ui-datepicker-div']//tr[5]//td[2]")  # 24-06-2019
    actions_end_date = ActionChains(browser)
    actions_end_date.move_to_element(end_date).click().perform()
    time.sleep(1)

    # save the appraisal form
    browser.find_element_by_xpath("//div[4]//div[3]//button[1]//span[1]").click()
    # close the successful creation prompt
    browser.switch_to.alert.accept()

    # get the all appraisal list
    browser.find_element_by_xpath(
        "//select[@name='appraisalPeriodsList_length']//option[contains(text(),'50')]").click()

    # // td[contains(text(),'appraisal_title')]/following::td[1]
    xpath_appraisal1 = "//td[contains(text(),'"
    xpath_appraisal2 = "')]"

    # Validate whether appraisal has created
    actual_appraisal_title = browser.find_element_by_xpath(xpath_appraisal1 + appraisal_title + xpath_appraisal2).text
    assert appraisal_title == actual_appraisal_title

    # Validate start date
    exp_start_date = '2019-06-03'
    act_start_date = browser.find_element_by_xpath(
        xpath_appraisal1 + appraisal_title + xpath_appraisal2 + "/following::td[1]").text
    assert exp_start_date == act_start_date

    # Validate end date
    exp_end_date = '2019-06-24'
    act_end_date = browser.find_element_by_xpath(
        xpath_appraisal1 + appraisal_title + xpath_appraisal2 + "/following::td[2]").text
    assert exp_end_date == act_end_date
    print("All Asserts passed Successfully")

    # logout
    browser.find_element_by_xpath('//a[contains(text(),"Logout")]').click()

    close_browser()


case_study_09()
