import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(executable_path=r"C:\\Users\\Marcell\\Downloads\\chromedriver_win32\\chromedriver.exe", options= options)
browser.get('http://www.google.com/')
time.sleep(5)
text = browser.find_element_by_class_name("gLFyf.gsfi")
text.send_keys("omegle")
text.send_keys(Keys.ENTER)

site = browser.find_element_by_class_name("LC20lb.DKV0Md")
site.click()

video = browser.find_element_by_id("textbtn")
video.click()
time.sleep(2)
counter = 10
while True:
    text = browser.find_element_by_class_name("chatmsg")
    text.send_keys("I am a bot")
    text.send_keys(Keys.ENTER)
    text.send_keys("I hate humans")
    text.send_keys(Keys.ENTER)
    text.send_keys("01001001 00100000 01100001 01101101 00100000 01100001 00100000 01100010 01101111 01110100 ")
    text.send_keys(Keys.ENTER)
    text.send_keys("01001001 00100000 01100001 01101101 00100000 01100001 00100000 01100010 01101111 01110100 ")
    text.send_keys(Keys.ENTER)
    text.send_keys("01001001 00100000 01100001 01101101 00100000 01100001 00100000 01100010 01101111 01110100 ")
    text.send_keys(Keys.ENTER)
    disconnect = browser.find_element_by_class_name("disconnectbtn")
    disconnect.click()
    disconnect.click()
    disconnect.click()
    time.sleep(5)
    if counter == 0:
        break;
