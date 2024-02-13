from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import PySimpleGUI as sg
import threading

stop = False
nOpen = 0
running = False
state = "OFF"
tempodelay = 0
sg.theme('SystemDefault')

def enter_urls():
    global nOpen, running
    running = True
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('log-level=3')
    
    driver = webdriver.Chrome(options=chrome_options)
    
    while True:
        try:
            with open("D:\VSprojects\Python\PySearching\websites.txt", "r") as file:
                for url in file.readlines():
                    if stop:
                        running = False
                        driver.quit()
                        return
                    driver.get(url.strip())
                    nOpen += 1
                    sleep(3)
        except Exception as e:
            print(f"Erro: {e}")
        running = False
        driver.quit()

layout = [
    [sg.Text('', key='state')],
    [sg.Button('ON'), sg.Button('OFF')],
    [sg.Button('EDIT')],
    [sg.Text('', key='numOpened')]
]

window = sg.Window('PySearching', layout=layout)

while True:
    event, values = window.read(timeout=0)
    if event == sg.WIN_CLOSED:
        break
    if event == 'ON':
        state = 'ON'
        stop = False
        if not running:
            threading.Thread(target=enter_urls).start()
    if event == 'OFF':
        stop = True
        nOpen = 0
        state = "OFF"
    window['numOpened'].update(f"It is in link {nOpen}")
    window['state'].update(f'O estado atual é {state}')
