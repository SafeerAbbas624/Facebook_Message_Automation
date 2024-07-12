import concurrent.futures
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
import multiprocessing
from fake_useragent import UserAgent

def read_login_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    login_data = []
    for line in lines:
        email, password, message = line.strip().split('|')
        login_data.append((email, password, message))
    return login_data

def login_to_facebook(data):
    email, password, _ = data
    ua = UserAgent()
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument(f'user-agent={ua.random}')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.facebook.com/")
    time.sleep(random.randint(15, 25))
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "pass")
    email_input.send_keys(email)
    password_input.send_keys(password)
    password_input.submit()
    time.sleep(random.randint(5, 10))
    return driver

def reply_to_messages(index, drivers, message):
    driver = drivers[index]
    while True:
        try:
            driver.get("https://www.facebook.com/messages/t")
            time.sleep(random.randint(5, 10))
            new_message = driver.find_element(By.XPATH, '//span[contains(text(), "new")]').text
            if 'new' in new_message:
                reply_button = driver.find_element(By.XPATH, '//div[contains(@class, "x1lliihq x1n2onr6 xh8yej3 x1ja2u2z x1iyjqo2 x1gmr53x x1abvqpe x2lah0s x1q0g3np x1nc0l9o x1nhvcw7 xm0m39n x9f619 x1ypdohk xdl7l9j x1ora5w5 xwibzug x1qij0fl x1lcqo3u x1t137rt x1q0g3np x1nhvcw7 x1fz4u7x x1lliihq x1s928wv x1ja2u2z x1iyjqo2 x1gmr53x x1abvqpe x2lah0s x1q0g3np x1nc0l9o x1nhvcw7 xm0m39n x9f619 x1ypdohk xdl7l9j x1ora5w5 xwibzug x1qij0fl x1lcqo3u x1t137rt")]')
                driver.execute_script("arguments[0].click();", reply_button)
                time.sleep(random.randint(2, 5))
                message_input = driver.find_element(By.XPATH, '//div[contains(@class, "x1lliihq x1n2onr6 xh8yej3 x1iyjqo2 x1gmr53x x1abvqpe x2lah0s x1q0g3np x1nc0l9o x1nhvcw7 xm0m39n x9f619 x1ypdohk xdl7l9j x1ora5w5 xwibzug x1qij0fl x1lcqo3u x1t137rt x1q0g3np x1nhvcw7 x1fz4u7x x1lliihq x1s928wv x1ja2u2z x1iyjqo2 x1gmr53x x1abvqpe x2lah0s x1q0g3np x1nc0l9o x1nhvcw7 xm0m39n x9f619 x1ypdohk xdl7l9j x1ora5w5 xwibzug x1qij0fl x1lcqo3u x1t137rt")]')
                driver.execute_script("arguments[0].value = arguments[1];", message_input, message)
                time.sleep(random.randint(2, 5))
                send_button = driver.find_element(By.XPATH, '//span[contains(@class, "x1lku1pv x1enjqo5 x16tdsg8 x193iq5w x6ikm8r x10wlt62 x1n2onr6 x1q0g3np x1iyjqo2 x1gmr53x x1abvqpe x2lah0s x1q0g3np x1nc0l9o x1nhvcw7 xm0m39n x9f619 x1ypdohk xdl7l9j x1ora5w5 xwibzug x1qij0fl x1lcqo3u x1t137rt x1q0g3np x1nhvcw7 x1fz4u7x x1lliihq x1s928wv x1ja2u2z x1iyjqo2 x1gmr53x x1abvqpe x2lah0s x1q0g3np x1nc0l9o x1nhvcw7 xm0m39n x9f619 x1ypdohk xdl7l9j x1ora5w5 xwibzug x1qij0fl x1lcqo3u x1t137rt")]')
                driver.execute_script("arguments[0].click();", send_button)
                time.sleep(random.randint(5, 10))
                return True
            else:
                time.sleep(random.randint(60, 120))
                pass
        except Exception as e:
            print("Error during message handling:", str(e))
            time.sleep(random.randint(60, 120))
            return False
from functools import partial

def main():
    login_data_file = "login_data.txt"
    login_data = read_login_data(login_data_file)
    drivers = [login_to_facebook(data) for data in login_data]
    messages = [data[2] for data in login_data]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for index, driver in enumerate(drivers):
            executor.submit(reply_to_messages, index, driver, messages[index])

if __name__ == "__main__":
    main()


