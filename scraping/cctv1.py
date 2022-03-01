from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import subprocess
import time
import pyautogui

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동


option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
    driver.get("https://www.youtube.com/watch?v=-JhoMGoAfFc")
    # 아래의 xpath를 구하는 방법이 되지 않아 아래 if 문을 사용했다.
    # driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button')
    # driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[28]/div[2]/div[2]/button[10]').click()
    # time.sleep(2)
    # 현재 마우스 위치를 파악한다.
    # print(pyautogui.position())
    # 마우스 위치를 이동한다.
    # pyautogui.moveTo(100, 200)
    # 출력한 창에 광고 skip의 class 이름이 존재하는지 살펴본다.
    if driver.find_elements(By.CLASS_NAME, 'ytp-ad-preview-container'):
        # if 문이 실제 작동하는지 창 최대화를 통해 살펴본다.(실제 작동하는 것을 확인했다.)
        # driver.maximize_window()
        # 다시 페이지를 로드하는 방법을 사용했으나 여전히 과고가 나오게 되었다.
        # driver.get("https://www.youtube.com/watch?v=-JhoMGoAfFc")
        # 20초를 기다
        time.sleep(16)
        driver.get("https://www.youtube.com/watch?v=-JhoMGoAfFc")
        time.sleep(3)
        pyautogui.moveTo(100, 200)
        pyautogui.click()
        pyautogui.press('f')
        time.sleep(10)
        driver.save_screenshot(r"C:\Users\Win10\Desktop\photo\photo.png")
        print("### capture complete")
    else:
        pyautogui.moveTo(100, 200)
        pyautogui.click()
        pyautogui.press('f')
        time.sleep(10)
        driver.save_screenshot(r"C:\Users\Win10\Desktop\photo\photo.png")
        print("### capture complete")
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
    # driver.get("https://www.youtube.com/watch?v=-JhoMGoAfFc")
    # time.sleep(5)
    # pyautogui.press('f')
    # driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[28]/div[2]/div[2]/button[10]').click()
    # driver.maximize_window()
    # driver.save_screenshot(r"C:\Users\Win10\Desktop\photo\photo.png")
    # driver.quit()
    # print("### capture complete")
    #// *[ @ id = "skip-button:5"] / span / button
    #// *[ @ id = "skip-button:5"] / span / button
    #// *[ @ id = "skip-button:5"] / span / button
    #< span
    #         class ="ytp-ad-skip-button-slot" id="skip-button:5" style="" > < span class ="ytp-ad-skip-button-container" style="" > < button class ="ytp-ad-skip-button ytp-button" > < div class ="ytp-ad-text ytp-ad-skip-button-text" id="ad-text:6" style="" > 광고 건너뛰기 < / div > < span class ="ytp-ad-skip-button-icon" > < svg height="100%" version="1.1" viewBox="0 0 36 36" width="100%" > < use class ="ytp-svg-shadow" xlink:href = "#ytp-id-36" > <
    #
    #         / use > < path
    #
    #
    #         class ="ytp-svg-fill" d="M 12,24 20.5,18 12,12 V 24 z M 22,12 v 12 h 2 V 12 h -2 z" id="ytp-id-36" > < / path > < / svg > < / span > < / button > < / span > < / div >
    #
    # class ="ytp-ad-preview-container countdown-next-to-thumbnail" style="display: none;" > < div class ="ytp-ad-text ytp-ad-preview-text" id="ad-text:n" style="display: none;" > 0 < / div > < span class ="ytp-ad-preview-image" > < img class ="ytp-ad-image" id="ad-image:o" src="https://i.ytimg.com/vi/t9R-ZTJN9OE/mqdefault.jpg" alt="" style="display: none;" > < / span > < / span >