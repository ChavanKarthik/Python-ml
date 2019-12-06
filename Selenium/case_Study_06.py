# importing required libraries
from selenium import webdriver

# open firefox browser
browser = webdriver.Firefox()


def open_browser(url):
    # open required url
    browser.get(url)


def close_browser():
    browser.close()


beesheets = 'http://192.168.5.214:8081/beesheets/html/Admin/admin.html'


def case_study_06():
    open_browser(beesheets)

    # login
    username = 'admin1'
    password = 'beehyv'
    browser.find_element_by_xpath('//input[@name="j_username"]').send_keys(username)
    browser.find_element_by_xpath("//input[@name='j_password']").send_keys(password)
    browser.find_element_by_xpath('//*[@id="form"]/form/input[3]').click()

    # navigate to admin tab
    browser.find_element_by_id("admin-tab").click()

    # navigate to employee management
    browser.find_element_by_xpath("//a[@id='employee-Management-ref']").click()

    # enter the employee name to be searched
    browser.find_element_by_xpath("//div[@id='employeeTable_filter']//input").send_keys("Dhiraj Kumar")

    browser.implicitly_wait(2)

    exp_emp_after_search = 'Dhiraj Kumar'
    act_emp_after_search = browser.find_element_by_xpath("//td[contains(text(),'Dhiraj Kumar')]").text

    assert exp_emp_after_search == act_emp_after_search

    print("All asserts passed successfully")

    # logout
    browser.find_element_by_xpath('//a[contains(text(),"Logout")]').click()

    close_browser()


case_study_06()
