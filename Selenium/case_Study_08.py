# importing required libraries
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# open firefox browser
browser = webdriver.Firefox()


def open_browser(url):
    # open required url
    browser.get(url)


def close_browser():
    browser.close()


beesheets = 'http://192.168.5.214:8081/beesheets/html/Admin/admin.html'


def case_study_08():
    open_browser(beesheets)

    # login
    username = 'admin1'
    password = 'beehyv'
    browser.find_element_by_xpath('//input[@name="j_username"]').send_keys(username)
    browser.find_element_by_xpath("//input[@name='j_password']").send_keys(password)
    browser.find_element_by_xpath('//*[@id="form"]/form/input[3]').click()

    # navigate to admin tab
    browser.find_element_by_id("admin-tab").click()
    time.sleep(1)

    # click on edit project (project : Apollo Domain Services)
    browser.find_element_by_xpath("//tr[8]//td[4]//img[1]").click()
    time.sleep(1)

    # click on add employee
    browser.find_element_by_xpath("//a[@id='edit-employee-link']").click()
    emp_name = "sumanth"
    # enter the employee name to be added and select the emp
    browser.find_element_by_xpath("//input[@id='tagname2']").send_keys(emp_name)
    browser.find_element_by_xpath("//input[@id='tagname2']").send_keys(Keys.PAGE_DOWN)
    browser.find_element_by_xpath("//input[@id='tagname2']").send_keys(Keys.ARROW_DOWN)
    browser.find_element_by_xpath("//input[@id='tagname2']").send_keys(Keys.ENTER)

    # enter the start date of project
    browser.find_element_by_xpath("//input[@id='startDateSelection']").send_keys("2019-05-17")

    # add employee to project
    browser.find_element_by_xpath("//button[contains(text(),'+')]").click()
    # time.sleep(10)

    browser.find_element_by_xpath("//span[contains(text(),'Save')]").click()

    # navigate to employee management
    browser.find_element_by_xpath("//a[@id='employee-Management-ref']").click()
    # search for employee and open his details
    browser.find_element_by_xpath("//div[@id='employeeTable_filter']//input").send_keys(emp_name)
    time.sleep(1)
    browser.find_element_by_xpath("//table[@id='employeeTable']//img[@class='editAndDelete']").click()

    # search whether the project is listed in emp details
    xpath_get_projects1 = "//table[@id='listofUserProjectsTable']//td[contains(text(),'"
    xpath_get_projects2 = "')]"
    project_name = 'Apollo Domain Services'
    act_emp_projects = browser.find_element_by_xpath(
        xpath_get_projects1 + project_name + xpath_get_projects2).text.strip()

    assert act_emp_projects == project_name

    # click on save to close employee details window
    browser.find_element_by_xpath("//span[contains(text(),'Save')]").click()

    print("Assert passed")

    # logout
    browser.find_element_by_xpath('//a[contains(text(),"Logout")]').click()

    close_browser()


case_study_08()
