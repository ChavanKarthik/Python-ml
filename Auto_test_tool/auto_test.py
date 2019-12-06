# importing required libraries
import csv
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# open firefox browser in headless mode
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)


# Open browser function
def open_browser(url):
    # open required url
    browser.get(url)
    time.sleep(1)


# Close browser function
def close_browser():
    browser.close()


# URL of application to be tested
url = 'https://www.healthy-india.org/bmi_calculator.php'

# test data input file path
# file_path = os.getcwd() + "/auto_test.csv"
file_path = input("Enter the test data complete file path")

# opening the test data file
with open(file_path, newline='') as test_data_file:
    read_values = list(csv.reader(test_data_file))


# execute tests with the given inputs in test data file
def test_runner(input_1, input_2):
    # xpath for first input
    xpath_input_1 = "//input[@id='txtweight']"
    # xpath for second input
    xpath_input_2 = "//input[@id='txtheight']"
    # xpath for submit button
    xpath_submit = "//input[@name='submit']"
    # xpath for result extraction
    xpath_act_result = "//span[contains(text(), 'BMI')]"

    # navigate browser to first input xpath and pass input1 values
    browser.find_element_by_xpath(xpath_input_1).send_keys(input_1)
    # navigate browser to second input xpath and pass input2 values
    browser.find_element_by_xpath(xpath_input_2).send_keys(input_2)
    # click on submit button
    browser.find_element_by_xpath(xpath_submit).click()
    # get the result after clicking submit button
    act_result = browser.find_element_by_xpath(xpath_act_result).text
    # store actual results
    return act_result


# function to get the expected result data and validate with actual result
def get_data_and_test(read_values):
    for i in range(1, len(read_values)):
        # load input1 values to pass in the app url
        input_1 = read_values[i][0]
        for j in range(1, 2):
            # load input2 values to pass in the app url
            input_2 = read_values[j][1]
            # start the test execution and pass two input variables
            output = test_runner(input_1, input_2)
            # take down the result and add it to the respective test-case data
            read_values[i].append(output)
            # validate the expected result with actual result
            if read_values[i][2] == read_values[i][3]:
                read_values[i].append("Test passed")
            else:
                read_values[i].append("Test Failed")
    return read_values


# write the results to a CSV file
def write_to_external_csv(read_values):
    df = pd.DataFrame(read_values)
    df.to_csv('auto_tested.csv', index=False, header=False)


if __name__ == "__main__":
    open_browser(url)
    get_data_and_test(read_values)
    write_to_external_csv(read_values)
    close_browser()
    print("Test execution is completed check auto_tested.csv for results")
