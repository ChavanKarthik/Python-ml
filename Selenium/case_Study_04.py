# importing required libraries
import time

from selenium import webdriver

# open firefox browser
browser = webdriver.Firefox()


def open_browser(url):
    # open required url
    browser.get(url)


def close_browser():
    browser.close()


beesheets = 'http://192.168.5.214:8081/beesheets/html/Admin/admin.html'


def case_study_04():
    open_browser(beesheets)

    # login
    username = 'case04'
    password = 'case04'
    browser.find_element_by_xpath('//input[@name="j_username"]').send_keys(username)
    browser.find_element_by_xpath("//input[@name='j_password']").send_keys(password)
    browser.find_element_by_xpath('//*[@id="form"]/form/input[3]').click()

    # navigate to admin tab
    browser.find_element_by_id("admin-tab").click()

    projects1 = []

    def get_projects():
        project_xpath1 = "//tbody//tr["
        project_xpath2 = "]//td[1]"
        for i in range(1, 5):
            time.sleep(0.5)
            element1 = browser.find_element_by_xpath(project_xpath1 + str(i) + project_xpath2).text
            projects1.append(element1)
        return projects1

    projects_asc_sort = get_projects()

    # check initially projects are shown in asc order
    assert projects_asc_sort == sorted(projects_asc_sort)
    print('Ascending sort works as exp')

    # click desc of sort
    browser.find_element_by_xpath("//th[@class='sorting_asc']").click()

    # get list of projects after clicking on sort
    elements = browser.find_elements_by_xpath("//tbody//td[@class=' sorting_1']")
    projects_after_desc_sort = []
    for element in elements:
        projects_after_desc_sort.append(element.text)

    # descending order sort check
    assert projects_after_desc_sort == sorted(projects_asc_sort, reverse=True)
    print("Descending sort work as expected")

    # number of projects check
    assert len(projects_asc_sort) == len(projects_after_desc_sort)
    print('Number of projects count is same after and before sort')

    # logout
    browser.find_element_by_xpath('//a[contains(text(),"Logout")]').click()

    close_browser()


case_study_04()
