# importing required libraries
import time
from random import randint

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


beesheets = 'http://192.168.5.214:8081/beesheets/html/Admin/admin.html'


def case_study_13():
    open_browser(beesheets)

    # login
    username = 'admin1'
    password = 'beehyv'
    browser.find_element_by_xpath('//input[@name="j_username"]').send_keys(username)
    browser.find_element_by_xpath("//input[@name='j_password']").send_keys(password)
    browser.find_element_by_xpath('//*[@id="form"]/form/input[3]').click()

    # navigate to admin tab
    browser.find_element_by_xpath("//a[contains(text(),'Admin')]").click()

    # navigate to employee - Management tab
    browser.find_element_by_xpath("//a[@id='employee-Management-ref']").click()

    # add employee
    browser.find_element_by_xpath("//button[@id='addNewEmployee']//span[@class="
                                  "'ui-button-text'][contains(text(),'Add')]").click()
    # test users naming convention
    beehyv_id = randint(12345678, 888888888)
    employee_name = 'beehyv_test_employee_' + str(beehyv_id)

    # fill create employee form
    browser.find_element_by_xpath("//input[@id='firstNameEM']").send_keys(employee_name)

    # Navigate to designation drop down menu
    N = 3  # number of times to press TAB
    actions_to_navigate_to_designation = ActionChains(browser)
    for _ in range(N):
        actions_to_navigate_to_designation = actions_to_navigate_to_designation.send_keys(Keys.TAB)
    actions_to_navigate_to_designation.perform()

    # select Designation
    actions_to_select_designation = ActionChains(browser)
    actions_to_select_designation.send_keys(Keys.PAGE_DOWN).perform()

    # Navigate to role drop down menu
    actions_to_navigate_to_role = ActionChains(browser)
    actions_to_navigate_to_role.send_keys(Keys.TAB).perform()

    # select role
    actions_to_select_role = ActionChains(browser)
    actions_to_select_role.send_keys(Keys.ARROW_DOWN).perform()
    actions_to_select_role.send_keys(Keys.ENTER).perform()

    # select date of joining
    browser.find_element_by_xpath("//input[@id='dojEM']").send_keys(Keys.ENTER)

    # select date of birth
    date_of_birth = '1993-05-08'
    browser.find_element_by_xpath("//input[@id='dobEM']").send_keys(date_of_birth)

    # select date of appraisal
    date_of_appraisal = "2020-06-17"
    browser.find_element_by_xpath("// input[ @ id = 'appraisalDateEM']").send_keys(date_of_appraisal)
    browser.find_element_by_xpath("// input[ @ id = 'appraisalDateEM']").send_keys(Keys.ENTER)
    time.sleep(1)

    # enter user name and password
    emp_user_name = beehyv_id
    emp_password = 'beehyv123'
    browser.find_element_by_xpath("//input[@id='userNameEM']").send_keys(emp_user_name)
    browser.find_element_by_xpath("//input[@id='passwordEM']").send_keys(emp_password)

    # enter email id and beehyv_id
    emp_email_id = str(beehyv_id) + '@beehyv.com'
    browser.find_element_by_xpath("//input[@id='emailEM']").send_keys(emp_email_id)
    browser.find_element_by_xpath("//input[@id='beehyvId']").send_keys(beehyv_id)

    # create the employee
    browser.find_element_by_xpath("//span[contains(text(),'Save')]").click()

    # search created employee to validate
    browser.find_element_by_xpath("//div[@id='employeeTable_filter']//input").send_keys(employee_name)
    time.sleep(1)

    search_result = browser.find_element_by_xpath("//table[@id='employeeTable']/tbody/tr/td").text
    print('search_result : ' + search_result)

    assert employee_name in search_result
    print("Employee created and searchable with : " + employee_name)

    # logout
    browser.find_element_by_xpath('//a[contains(text(),"Logout")]').click()

    # Close browser
    actions_to_close_browser = ActionChains(browser)
    actions_to_close_browser.send_keys(Keys.ALT).send_keys(Keys.F4).perform()
    close_browser()


case_study_13()
