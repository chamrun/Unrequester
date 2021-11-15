import configparser
from time import sleep

from selenium import webdriver

# based on your internet speed, you can change time unit
TIME_UNIT = 2

if __name__ == '__main__':

    config = configparser.ConfigParser()
    config.read('login_data.ini')

    my_username = config['instagram']['username']
    my_password = config['instagram']['password']

    # driver = webdriver.Firefox()

    driver = webdriver.Chrome()
    login_url = 'https://www.instagram.com/accounts/login/'
    driver.get(login_url)

    username_field_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
    username_field = driver.find_element_by_xpath(username_field_xpath)
    username_field.send_keys(my_username)

    password_field_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
    password_field = driver.find_element_by_xpath(password_field_xpath)
    password_field.send_keys(my_password)

    login_button_xpath = '//*[@id="loginForm"]/div/div[3]'
    login_button = driver.find_element_by_xpath(login_button_xpath)
    login_button.click()

    sleep(TIME_UNIT * 2)

    follow_requests_url = 'https://www.instagram.com/accounts/access_tool/current_follow_requests'
    driver.get(follow_requests_url)

    sleep(TIME_UNIT * 2)

    view_more_xpath = '/html/body/div[1]/section/main/div/article/main/button'
    view_more_button = driver.find_element_by_xpath(view_more_xpath)
    view_more_button.click()

    sleep(TIME_UNIT)

    for i in range(30):
        print(str(i) + "th click on view more button...")
        view_more_xpath = '//*[@id="react-root"]/section/main/div/article/main/button'
        view_more_button = driver.find_element_by_xpath(view_more_xpath)
        view_more_button.click()



