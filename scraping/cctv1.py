from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import time

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동


option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
    driver.get("https://www.youtube.com/watch?v=-JhoMGoAfFc")
    driver.maximize_window()
    time.sleep(100)
    driver.save_screenshot(r"C:\Users\Win10\Desktop\photo\photo.png")
    driver.quit()
    print("### capture complete")
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
    driver.get("https://www.youtube.com/watch?v=-JhoMGoAfFc")
    # driver.element.click()
    driver.maximize_window()
    time.sleep(100)
    driver.save_screenshot(r"C:\Users\Win10\Desktop\photo\photo.png")
    driver.quit()
    print("### capture complete")