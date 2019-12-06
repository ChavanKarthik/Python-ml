# importing required libraries
import time

from selenium import webdriver

# open firefox browser
browser = webdriver.Firefox()


def open_browser(url):
    # open required url
    browser.get(url)
    time.sleep(0.5)


def close_browser():
    browser.close()


beesheets = 'http://192.168.5.214:8081/beesheets/html/Admin/admin.html'


def case_study_03():
    open_browser(beesheets)

    # login
    username = 'admin1'
    password = 'beehyv'
    browser.find_element_by_xpath('//input[@name="j_username"]').send_keys(username)
    browser.find_element_by_xpath("//input[@name='j_password']").send_keys(password)
    time.sleep(0.5)
    browser.find_element_by_xpath('//*[@id="form"]/form/input[3]').click()
    time.sleep(0.5)

    # navigate to admin tab
    browser.find_element_by_xpath("//a[contains(text(),'Admin')]").click()
    time.sleep(0.5)

    # navigate to employee - Management tab
    browser.find_element_by_xpath("//a[@id='appraisal-Management-ref']").click()
    time.sleep(0.5)

    # select an employee
    browser.find_element_by_xpath("//div[@id='ui-tabs-4']//tr[1]//td[4]//img[1]").click()
    time.sleep(0.5)

    # scroll down till appraiser name is shown
    element = browser.find_element_by_xpath("//*[@id='appraisal_employees_list_chosen']/div/ul/li[48]")
    element.location_once_scrolled_into_view
    time.sleep(0.5)

    # add the appraisers
    browser.find_element_by_xpath("//*[@id='appraisal_employees_list_chosen']/div/ul/li[48]").click()
    time.sleep(0.5)

    # click on pane of appraisers
    browser.find_element_by_xpath("//ul[@class='chosen-choices']")

    # get the selected appraiser after selection
    selected_appraiser = browser.find_element_by_xpath("//span[contains(text(),'Manohar k')]").text
    appraisers = browser.find_element_by_xpath("//ul[@class='chosen-choices']//li[2]").text
    print('Selected appraisers : ' + str(selected_appraiser))

    # check whether the selected appraiser is added
    assert selected_appraiser in appraisers
    print("Employees selected  : " + str(selected_appraiser))

    # cancel the add employee window
    browser.find_element_by_xpath("//span[contains(text(),'Cancel')]").click()
    time.sleep(0.5)

    # logout
    browser.find_element_by_xpath('//a[contains(text(),"Logout")]').click()
    time.sleep(0.5)

    close_browser()


case_study_03()
