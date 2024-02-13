from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
def enter_urls():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('log-level=3')
    driver = webdriver.Chrome(options=chrome_options)
    nOpen = 0
    while True:
        try:
            with open("D:\VSprojects\Python\PySearching\websites.txt", "r") as file:
                for url in file.readlines():
                    driver.get(url)
                    nOpen +=1
                    os.system('cls')
                    print(f"It is in link {nOpen}")
                    sleep(3)
        except:
            print(end="")