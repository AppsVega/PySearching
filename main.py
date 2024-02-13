from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import PySimpleGUI as sg
chrome_options = Options()
chrome_options.add_argument('log-level=3')
driver = webdriver.Chrome(options=chrome_options)
nOpen = 0
def enter_urls():
    while True:
        try:
            with open("D:\VSprojects\Python\PySearching\websites.txt", "r") as file:
                for url in file.readlines():
                    driver.get(url)
                    nOpen +=1
                    sleep(3)
                    print(nOpen)
        except:
            print(end="")
enter_urls()
layout = [
    [sg.Button('ON / OFF')],
    [sg.Button('EDIT')],
    [sg.Text('',key='numOpened')]
]
window = sg.Window('PySearching',layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'ON / OFF':
        enter_urls()
    window['numOpened'].update(f"It is in link {nOpen}")