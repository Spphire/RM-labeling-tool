import os
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

download_path = os.path.join(os.getcwd(), "download")  # 下载路径
if not os.path.exists(download_path):
    os.mkdir(download_path)
background_path = os.path.join(os.getcwd(), "background")  # 背景图路径
if not os.path.exists(background_path):
    os.mkdir(background_path)

url = 'https://spphire.github.io/RM-labeling-tool/'

bk_paths = os.listdir(background_path)
new_bk_paths = []
for p in bk_paths:
    if p.endswith('.png') or p.endswith('.jpg') or p.endswith('.jpeg'):
        new_bk_paths.append(p)
bk_paths = new_bk_paths

s = Service('chromedriver.exe')
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory': download_path,
         'profile.default_content_setting_values.automatic_downloads': 1}
options.add_experimental_option('prefs', prefs)

# options.add_argument('--headless')   # 隐藏浏览器

browser = webdriver.Chrome(service=s, options=options)
browser.get(url)
browser.implicitly_wait(15)

while browser.execute_script("return myGameInstance==null"):
    time.sleep(1)

# input
e = browser.find_element(By.ID, 'Temp')
input('ready?')


def run(i: int):
    if (i <= 0):
        i = 0
    timeall = 0
    while (True):
        for _ in range(i):
            browser.execute_script("myGameInstance.SendMessage('GameController','CaptureContinue',0)")
            timeall += 1
            print(timeall)

        browser.execute_script("myGameInstance.SendMessage('GameController','SetVisibleMap',0)")
        e.send_keys(os.path.join(background_path, random.choice(bk_paths)))
        jscm = "myGameInstance.SendMessage('ImgTemp', 'FileSelected', URL.createObjectURL(document.getElementById('Temp').files[0]));"
        browser.execute_script(jscm)


run(10)
