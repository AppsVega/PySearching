from selenium import webdriver
from time import sleep
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
while True:
    with open("D:\VSprojects\Python\PySearching\websites.txt", "r") as file:
        for url in file.readlines():
            driver.get(url)
            sleep(15)