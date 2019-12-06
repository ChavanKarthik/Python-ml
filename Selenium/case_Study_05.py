# importing required libraries
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# open firefox browser
browser = webdriver.Firefox()


def open_browser(url):
    # open required url
    browser.get(url)


def close_browser():
    browser.close()


beesheets = 'http://192.168.5.214:8081/beesheets/html/Admin/admin.html'


def case_study_05():
    open_browser(beesheets)

    # login
    username = 'admin1'
    password = 'beehyv'
    browser.find_element_by_xpath('//input[@name="j_username"]').send_keys(username)
    browser.find_element_by_xpath("//input[@name='j_password']").send_keys(password)
    browser.find_element_by_xpath('//*[@id="form"]/form/input[3]').click()
    time.sleep(0.5)

    # navigate to admin tab
    browser.find_element_by_id("admin-tab").click()

    # increase the number of entries
    browser.find_element_by_xpath("//option[contains(text(),'50')]").click()

    total_projects = browser.find_element_by_xpath("//div[@id='projectTable_info']").text
    # total_projects = "Showing 1 to 50 of 152 entries"
    expected_projects_count = int(total_projects[-11:-8])

    # expected "first" button status with class name
    expected_first_button_class = "first paginate_button paginate_button_disabled"
    # get actual "first" button status with class name
    first_button_status_in_page1 = browser.find_element_by_xpath("//a[@id='projectTable_first']").get_attribute("class")
    assert expected_first_button_class == first_button_status_in_page1

    # expected "previous" button status with class name
    expected_previous_button_class = 'previous paginate_button paginate_button_disabled'
    # get actual "previous" button status with class name
    previous_button_status_in_page1 = browser.find_element_by_xpath("//a[@id='projectTable_previous']").get_attribute(
        "class")
    assert expected_previous_button_class == previous_button_status_in_page1

    # test next button functionality
    browser.find_element_by_xpath("//a[@id='projectTable_next']").click()
    # get page number
    page_after_next_button = int(browser.find_element_by_xpath("//a[@class='paginate_active']").text)
    # Verify pagination functionality for Next Button
    assert page_after_next_button == 2

    # test "first" button functionality
    browser.find_element_by_xpath("//a[@id='projectTable_first']").click()
    # get page number
    page_after_first_button = int(browser.find_element_by_xpath("//a[@class='paginate_active']").text)
    # Verify pagination functionality for First Button
    assert page_after_first_button == 1

    # test "last" button functionality
    browser.find_element_by_xpath("//a[@id='projectTable_last']").click()
    # get page number
    page_after_last_button = int(browser.find_element_by_xpath("//a[@class='paginate_active']").text)
    # Verify pagination functionality for Last Button
    assert page_after_last_button == 4

    # expected "next" button status with class name
    expected_next_button_class = "next paginate_button paginate_button_disabled"
    # get actual "next" button status with class name
    next_button_status_in_last_page = browser.find_element_by_xpath("//a[@id='projectTable_next']").get_attribute(
        "class")
    assert expected_next_button_class == next_button_status_in_last_page

    # expected "last" button status with class name
    expected_last_button_class = 'last paginate_button paginate_button_disabled'
    # get actual "last" button status with class name
    last_button_status_in_last_page = browser.find_element_by_xpath("//a[@id='projectTable_last']").get_attribute(
        "class")
    assert expected_last_button_class == last_button_status_in_last_page

    # test "previous" button functionality
    browser.find_element_by_xpath("//a[@id='projectTable_last']").click()
    # get page number
    page_after_previous_button = int(browser.find_element_by_xpath("//*[@id='projectTable_paginate']/span/a[3]").text)
    # Verify pagination functionality for Previous Button
    assert page_after_previous_button == 3

    project_xpath1 = "//tbody//tr["
    project_xpath2 = "]//td[1]"

    def get_projects(projects_list):
        for i in range(1, 51):
            time.sleep(0.2)
            element = browser.find_element_by_xpath(project_xpath1 + str(i) + project_xpath2).text
            projects_list.append(element)
        return projects_list

    def get_all_projects():
        browser.find_element_by_xpath("//a[@id='projectTable_first']").click()
        projects_list = []
        try:
            get_projects(projects_list)
            for j in range(1, 4):
                browser.find_element_by_xpath("//a[@id='projectTable_next']").click()
                get_projects(projects_list)
        except NoSuchElementException:
            pass
        finally:
            return projects_list

    actual_projects_counts = len(get_all_projects())
    assert expected_projects_count == actual_projects_counts

    # Assert page active number after clicking on each page button
    # navigate to page 1 using page number
    browser.find_element_by_xpath("//a[contains(text(),'1')]").click()
    # get page number after clicking on page 1
    page_after_page1_number = int(browser.find_element_by_xpath("//a[@class='paginate_active']").text)
    assert page_after_page1_number == 1

    # To verify that button gets highlighted after clicking
    exp_page1_number_status = 'paginate_active'
    act_page1_number_status = browser.find_element_by_xpath("//a[@class='paginate_active']").get_attribute("class")
    assert exp_page1_number_status == act_page1_number_status

    print("All asserts passed successfully")

    # logout
    browser.find_element_by_xpath('//a[contains(text(),"Logout")]').click()

    close_browser()


case_study_05()
