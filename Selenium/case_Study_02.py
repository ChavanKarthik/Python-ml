# importing required libraries
import time
from random import randint

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# open firefox browser
browser = webdriver.Firefox()


def open_browser(url):
    # open required url
    browser.get(url)
    time.sleep(2)


def close_browser():
    browser.close()


beesheets = 'http://192.168.5.214:8081/beesheets/html/Admin/admin.html'


def case_study_02():
    open_browser(beesheets)

    # login
    username = 'admin1'
    password = 'beehyv'
    browser.find_element_by_xpath('//input[@name="j_username"]').send_keys(username)
    browser.find_element_by_xpath("//input[@name='j_password']").send_keys(password)
    browser.find_element_by_xpath('//*[@id="form"]/form/input[3]').click()
    time.sleep(2)

    # navigate to admin tab
    browser.find_element_by_xpath("//a[contains(text(),'Admin')]").click()
    time.sleep(1)

    # navigate to employee - Management tab
    browser.find_element_by_xpath("//a[@id='employee-Management-ref']").click()
    time.sleep(1)

    # add employee
    browser.find_element_by_xpath("//button[@id='addNewEmployee']//span[@class="
                                  "'ui-button-text'][contains(text(),'Add')]").click()
    # test users naming convention
    beehyv_id = randint(12345678, 888888888)
    employee_name = 'beehyv_test_employee_' + str(beehyv_id)

    # fill create employee form
    browser.find_element_by_xpath("//input[@id='firstNameEM']").send_keys(employee_name)
    time.sleep(1)

    # select designation
    select_designation = Select(browser.find_element_by_xpath("//select[@id='designationEM']"))
    select_designation.select_by_value('39')
    time.sleep(1)

    # select date of joining
    today = "2019-06-17"
    browser.find_element_by_xpath("//input[@id='dojEM']").send_keys(today)

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
    time.sleep(2)

    # create the employee
    browser.find_element_by_xpath("//span[contains(text(),'Save')]").click()
    time.sleep(2)

    # search created employee to validate
    browser.find_element_by_xpath("//div[@id='employeeTable_filter']//input").send_keys(employee_name)
    # read_employee_name = '//td[contains(text(),'+employee_name+")]"
    time.sleep(2)

    search_result = browser.find_element_by_xpath("//table[@id='employeeTable']/tbody/tr/td").text
    time.sleep(2)
    print('search_result : ' + search_result)

    assert employee_name in search_result
    print("Employee created and searchable with : " + employee_name)

    # logout
    browser.find_element_by_xpath('//a[contains(text(),"Logout")]').click()
    time.sleep(2)

    close_browser()


case_study_02()
