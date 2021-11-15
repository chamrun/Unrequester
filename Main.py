import configparser


if __name__ == '__main__':

    config = configparser.ConfigParser()
    config.read('login_data.ini')

    my_username = config['instagram']['username']
    my_password = config['instagram']['password']

