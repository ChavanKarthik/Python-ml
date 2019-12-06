# importing required libraries
import time

from selenium import webdriver

# open firefox browser
browser = webdriver.Firefox()


def open_browser(url):
    # open required url
    browser.get(url)
    time.sleep(1)


def close_browser():
    browser.close()


url = 'https://schools.org.in/arunachal-pradesh'


def count_number_of_schools():
    open_browser(url)

    def get_number():

        try:
            summary_text = browser.find_element_by_xpath('//*[@id="container-sidebar"]/div[4]/div[1]/p[1]').text
            get_number = summary_text.split('about ')
            act_number = get_number[1].split(' ')
            number = act_number[0]
            try:
                int(number)
                return int(number)
            except:
                return 0

        except:
            summary_text = browser.find_element_by_xpath('//*[@id="container-sidebar"]/div[3]/div[1]/p[1]').text
            get_number = summary_text.split('about ')
            act_number = get_number[1].split(' ')
            number = act_number[0]
            try:
                int(number)
                return int(number)
            except:
                return 0

    schools_count_list = []
    for district in range(get_number()):
        browser.find_element_by_xpath(
            '//*[@id="container-sidebar"]/table/tbody/tr[' + str(district + 2) + ']/td[2]/a[1]').click()
        time.sleep(0.5)
        for blocks in range(get_number()):
            browser.find_element_by_xpath(
                '//*[@id="container-sidebar"]/table/tbody/tr[' + str(blocks + 2) + ']/td[2]/a[1]').click()
            time.sleep(0.5)
            num_clusters = get_number()
            for clusters in range(get_number()):
                browser.find_element_by_xpath(
                    '//*[@id="container-sidebar"]/table/tbody/tr[' + str(clusters + 2) + ']/td[2]/a[1]').click()
                time.sleep(0.5)
                schools_count = get_number()
                schools_count_list.append(schools_count)
                browser.find_element_by_xpath('//div[1]/div[1]/h2[1]/a[4]').click()

            browser.find_element_by_xpath('//div[1]/div[1]/h2[1]/a[3]').click()
        browser.find_element_by_xpath('//div[1]/div[1]/h2[1]/a[2]').click()

    # create a file and save the results
    with open('school_count_AP.csv', 'w') as file_handle:
        for list_item in schools_count_list:
            file_handle.write('%s\n' % list_item)

    close_browser()


count_number_of_schools()
