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


def case_study_07():
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

    # for 10 employees list view
    browser.find_element_by_xpath("//select[@name='employeeTable_length']//option[contains(text(),'10')]").click()

    total_emp_when_10 = browser.find_element_by_xpath("//div[@id='employeeTable_info']").text
    # total_emp = "Showing 1 to 10 of 152 entries" sample result
    exp_projects_count_with_10_entries = 10
    act_projects_count_with_10_entries = int(total_emp_when_10[13:15])
    # Validate the number of employees shown
    assert exp_projects_count_with_10_entries == act_projects_count_with_10_entries

    # change the number of entries to 25
    browser.find_element_by_xpath("//select[@name='employeeTable_length']//option[contains(text(),'25')]").click()

    # for 25 employees list view
    total_emp_when_25 = browser.find_element_by_xpath("//div[@id='employeeTable_info']").text

    exp_projects_count_with_25_entries = 25
    act_projects_count_with_25_entries = int(total_emp_when_25[13:15])

    # Validate the number of employees shown
    assert exp_projects_count_with_25_entries == act_projects_count_with_25_entries

    # change the number of entries to 50
    browser.find_element_by_xpath("//select[@name='employeeTable_length']//option[contains(text(),'50')]").click()

    # for 50 employees list view
    total_emp_when_50 = browser.find_element_by_xpath("//div[@id='employeeTable_info']").text

    exp_projects_count_with_50_entries = 50
    act_projects_count_with_50_entries = int(total_emp_when_50[13:15])

    # Validate the number of employees shown
    assert exp_projects_count_with_50_entries == act_projects_count_with_50_entries

    # change the number of entries to 100
    browser.find_element_by_xpath("//select[@name='employeeTable_length']//option[contains(text(),'100')]").click()

    # for 100 employees list view
    total_emp_when_100 = browser.find_element_by_xpath("//div[@id='employeeTable_info']").text

    exp_projects_count_with_100_entries = 100
    act_projects_count_with_100_entries = int(total_emp_when_100[13:16])

    # Validate the number of employees shown
    assert exp_projects_count_with_100_entries == act_projects_count_with_100_entries

    print("All asserts passed successfully")

    # logout
    browser.find_element_by_xpath('//a[contains(text(),"Logout")]').click()

    close_browser()


case_study_07()
