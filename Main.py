import configparser
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# based on your internet speed, you can change time unit
TIME_UNIT = 1

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('login_data.ini')

    my_username = config['instagram']['username']
    my_password = config['instagram']['password']

    # Choose your favorite browser :)
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver = webdriver.Opera()

    print("Opening instagram...")
    login_url = 'https://www.instagram.com/accounts/login/'
    driver.get(login_url)
    sleep(TIME_UNIT)

    while 'insta' not in driver.current_url:
        print("Driver is still on: " + driver.current_url)
        driver.get(login_url)
        sleep(TIME_UNIT * 2)

    print("Writing username...")
    username_field_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
    username_field = driver.find_element_by_xpath(username_field_xpath)
    username_field.send_keys(my_username)

    print("Writing password...")
    password_field_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
    password_field = driver.find_element_by_xpath(password_field_xpath)
    password_field.send_keys(my_password)

    print("Clicking on login button...")
    login_button_xpath = '//*[@id="loginForm"]/div/div[3]'
    login_button = driver.find_element_by_xpath(login_button_xpath)
    login_button.click()

    while 'login' in driver.current_url:
        sleep(TIME_UNIT)

    print("Opening follow requests...")
    follow_requests_url = 'https://www.instagram.com/accounts/access_tool/current_follow_requests'
    driver.get(follow_requests_url)

    sleep(TIME_UNIT)

    while 'follow' not in driver.current_url:
        print("Driver is still on: " + driver.current_url)
        driver.get(follow_requests_url)
        sleep(TIME_UNIT * 2)

    print("Clicking on view more button...")
    view_more_xpath = '/html/body/div[1]/section/main/div/article/main/button'
    view_more_button = driver.find_element_by_xpath(view_more_xpath)
    view_more_button.click()

    sleep(TIME_UNIT)

    for i in range(2, 50):
        print(str(i) + "th click on view more button...")
        view_more_xpath = '//*[@id="react-root"]/section/main/div/article/main/button'

        try:
            view_more_button = driver.find_element_by_xpath(view_more_xpath)
            view_more_button.click()
        except NoSuchElementException:
            print("No more requests.")
            break

        sleep(TIME_UNIT)

    requested_usernames_class_name = '-utLf'
    requested_usernames_elements = driver.find_elements_by_class_name(requested_usernames_class_name)

    requested_usernames = []
    for requested_username_element in requested_usernames_elements:
        username = requested_username_element.text
        requested_usernames.append(username)

    for username in requested_usernames:
        print("unrequesting " + username + " ...")
        insta_page = 'https://www.instagram.com/' + username
        driver.get(insta_page)
        sleep(TIME_UNIT)

        while username not in driver.current_url:
            print("Trying again to load " + insta_page)
            driver.get(insta_page)
            sleep(TIME_UNIT * 2)

        request_button_xpath = '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button'
        request_button = driver.find_element_by_xpath(request_button_xpath)
        request_button.click()
        unfollow_button_xpath = '/html/body/div[5]/div/div/div/div[3]/button[1]'
        unfollow_button = driver.find_element_by_xpath(unfollow_button_xpath)
        unfollow_button.click()
        print(username + " was unrequested successfully!")
        sleep(TIME_UNIT)

    print('Done :)')
