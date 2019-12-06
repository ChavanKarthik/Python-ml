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


def case_study_11():
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
    appraisal_title = "appraisal_test_426508"

    # search the appraisal name to be deleted
    browser.find_element_by_xpath("//div[@id='appraisalPeriodsList_filter']//input").send_keys(appraisal_title)

    # click on delete icon
    browser.find_element_by_xpath("//img[@class='delete-icon']").click()
    time.sleep(1)

    # confirm two dialog boxs
    browser.switch_to.alert.accept()
    browser.switch_to.alert.accept()

    # Validate appraisal deleted successfully
    browser.find_element_by_xpath("//div[@id='appraisalPeriodsList_filter']//input").send_keys(appraisal_title)

    act_appraisal_list_after_del = browser.find_element_by_xpath("//div[@id='appraisalPeriodsList_info']").text
    act_appraisal_after_del_count = int(act_appraisal_list_after_del[8:9])
    exp_appraisals_count = 0
    assert exp_appraisals_count == act_appraisal_after_del_count

    print("All Asserts passed Successfully")

    # logout
    browser.find_element_by_xpath('//a[contains(text(),"Logout")]').click()

    close_browser()


case_study_11()
