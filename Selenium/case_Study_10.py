# importing required libraries
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# create a firefox browser profile to handle save alert on clicking any download button
profile = FirefoxProfile()
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.openxmlformats-officedocument"
                                                                 ".spreadsheetml.sheet")
# open firefox browser
browser = webdriver.Firefox(firefox_profile=profile)


def open_browser(url):
    # open required url
    browser.get(url)


def close_browser():
    browser.close()


beesheets = 'http://192.168.5.214:8081/beesheets/html/Admin/admin.html'


def case_study_10():
    open_browser(beesheets)

    # login
    username = 'admin1'
    password = 'beehyv'
    browser.find_element_by_xpath('//input[@name="j_username"]').send_keys(username)
    browser.find_element_by_xpath("//input[@name='j_password']").send_keys(password)
    browser.find_element_by_xpath('//*[@id="form"]/form/input[3]').click()

    # navigate to admin tab
    browser.find_element_by_id("admin-tab").click()

    # navigate to reports tab
    browser.find_element_by_xpath("//a[@id='export-CSV-ref']").click()

    file = "/atish_appraisalAndAttrWorkbook.xlsx"
    path = os.getcwd() + file

    # select the file to be uploaded
    file_upload = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "filebox")))
    file_upload.send_keys(path)

    # click on upload button
    browser.find_element_by_xpath("//span[contains(text(),'Import')]").click()
    browser.implicitly_wait(2000)

    # handle the alert after upload
    browser.switch_to.alert.accept()
    print("Importing Assert passed")

    # enter the employee name to download tasks
    emp_name = 'Atish '
    browser.find_element_by_xpath("//input[@id='xlEmployeeAllTags']").send_keys(emp_name)
    browser.find_element_by_xpath("//input[@id='xlEmployeeAllTags']").send_keys(Keys.PAGE_DOWN)
    browser.find_element_by_xpath("//input[@id='xlEmployeeAllTags']").send_keys(Keys.ARROW_DOWN)
    browser.find_element_by_xpath("//input[@id='xlEmployeeAllTags']").send_keys(Keys.ENTER)

    # download the excel file
    browser.find_element_by_xpath("//span[contains(text(),'Export as Excel Spreadsheet')]").click()

    # time.sleep(1)

    def getDownLoadedFileName(waitTime):
        browser.execute_script("window.open()")
        WebDriverWait(browser, 10).until(EC.new_window_is_opened)
        browser.switch_to.window(browser.window_handles[-1])
        browser.get("about:downloads")

        endTime = time.time() + waitTime
        while True:
            try:
                fileName = browser.execute_script(
                    "return document.querySelector('#contentAreaDownloadsView .downloadMainArea .downloadContainer "
                    "description:nth-of-type(1)').value")
                if fileName:
                    return fileName
            except:
                pass
            time.sleep(1)
            if time.time() > endTime:
                break

    # check whether the file is downloaded
    latestDownloadedFileName = getDownLoadedFileName(30)  # waiting 3 minutes to complete the download
    exp_file_name = 'atish_appraisalAndAttrWorkbook'

    # Validate whether the correct file is downloaded
    assert exp_file_name in latestDownloadedFileName
    print("Exporting Assert passed")

    # close the downloads window
    close_browser()

    # change the driver focus to beesheets primary window
    browser.switch_to.window(browser.window_handles[0])

    # logout
    browser.find_element_by_xpath('//a[contains(text(),"Logout")]').click()

    # close the beesheets primary window
    close_browser()


case_study_10()
