
# import requests
# import pandas
# from bs4 import BeautifulSoup
# from PIL import ImageGrab, Image
#
# img = ImageGrab.grab()
# imgCrop = img.crop((100,100,200,200))
# saveas="{} {}".format('imagename', 'png')
# imgCrop.save((saveas))
#
# img1 = Image.open(saveas)
# img2 = Image.open('check.png')
#
# if img1 == img2:
#     print("same")
# else:
#     print("differ")
# import pyautogui as pag
# from PIL import ImageGrab
#
# path = r"C:\1.png"
# path = pag.locateOnScreen(path)
# if(path is not None):
#     getPos = pag.center(path)
#     pag.moveTo(getPos)
#     pag.click()

# import pyautogui as pag
from PIL import ImageGrab
# 캡쳐할 영역의 왼쪽 상단 모서리와 오른쪽 하단 모서리의 좌표값을 미리구해둔다.
# print(pag.position())

#left_top = (100, 100)
#right_bottom = (300, 300)
#left_top_x = left_top[0]
#right_bottom_y = right_bottom[1]
#capture_width = right_bottom[0]-left_top[0]
#capture_height = right_bottom[1]-left_top[1]
#path = r"C:\capture1.png"
#pag.screenshot(path, region=(left_top_x, right_bottom_y, capture_width, capture_height))

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from PIL import ImageGrab, Image

#chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--autoplay")

# 구글을 키고 도움말->chrome정보를 눌러 자기 버전에 맞는 webdriver를 아래 링크에서 설치할 것
# https://chromedriver.chromium.org/downloads
#options = webdriver.ChromeOptions()
#options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
driver = webdriver.Chrome(r"C:\Users\Win10\Desktop\chromedriver_win32\chromedriver.exe")

try:
    driver.get("https://www.youtube.com/watch?v=ydYDqZQpim8")
    # driver.send_keys('keys.SPACE')
    # 창 최대화
    driver.maximize_window()
    # video = driver.find_element_by_id('movie_player')
    # 스크린샷 전에 시간 두기(로딩이 느릴수도 있으니)
    time.sleep(15)
    # 스크린샷 찍기
    driver.save_screenshot(r"C:\Users\Win10\Desktop\photo\photo.png")
    # 종료 (모든 탭 종료)
    driver.quit()
    print("### capture complete")

except Exception as e: print('### error msg :: ', e)
driver.quit()

# img = ImageGrab.grab()
# imgCrop = img.crop((100,100,200,200))
# saveas="{} {}".format('imagename', 'png')
# imgCrop.save((saveas))
#
# img1 = Image.open(saveas)
# img2 = Image.open('check.png')
#
# if img1 == img2:
#     print("same")
# else:
#     print("differ")
