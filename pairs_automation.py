import os
import time
import random
import sys
import time
import math
from datetime import datetime
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Hour = 3600
Minute = 60
TotalNum=1
NumForOnePage = 16

def IntTryParse(val):
    try:
        return int(val)
    except ValueError:
        return val

def LeaveFootPrint(repeatStr):
    global TotalNum
    num=1
    currentNum = 1
    maxNum = random.randint(500,700)
    print("Leave %s footprints"%str(maxNum))
    while currentNum < maxNum:
        src= "https://pairs.lv/#/search/one/%s"%str(num)
        driver.get(src)
        print("Current: {0}/{1}, Total: {2}, {3}".format(str(currentNum), maxNum, str(TotalNum), repeatStr))
        if num == NumForOnePage:
            num = 0
        num += 1
        currentNum += 1
        TotalNum += 1
        time.sleep(random.randint(3,7))

def ShowElapsedTime(startTime):
    elapsed_time = time.time() - startTime
    hour = math.floor(elapsed_time / Hour)
    elapsedHour = hour * Hour
    minite = math.floor((elapsed_time - elapsedHour) / Minute)
    sec = str(elapsed_time - elapsedHour - minite * Minute)[:2]
    print("所要時間は「%s時間%s分%s秒」"%(str(hour), str(minite), str(sec)))

def TakeRest():
    minutesToRest = random.randint(15,30)
    print("Take a rest for {0} minutes".format(str(minutesToRest)))
    nowTime = datetime.now()
    print("will end %s:%s"%(str(nowTime.hour), str(nowTime.minute + minutesToRest)))
    driver.get("https://pairs.lv/#/search/grid/1")
    time.sleep(minutesToRest * 60)

def GetRepeatString(counter, maxRepeatNum):
    repeatStr = "Repeat: "
    if maxRepeatNum == 0:
        repeatStr += "なし"
    elif maxRepeatNum > 0:
        repeatStr += "{0}/{1}".format(str(counter), str(maxRepeatNum))
    else:
        repeatStr += "無限"
    return repeatStr

driver = webdriver.Chrome(r'./chromedriver.exe')
driver.get("https://pairs.lv/#/login")

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "registerBtn1"))
)

if element is not None:
    print(element)
    driver.execute_script("arguments[0].click();", element)

key = input('pairsのトップページが出たらrepeat回数を指定してください(マイナスの値は無限ループ)')
while not isinstance(IntTryParse(key), int):
    print("数字を入力してください")
    key = input()

print("Start!")
maxRepeatNum = int(key)
counter = 1
while True:
    startTime = time.time()
    print("%s回目"%str(counter))
    LeaveFootPrint(GetRepeatString(counter, maxRepeatNum))
    ShowElapsedTime(startTime)
    if (maxRepeatNum     > -1 and counter > maxRepeatNum):
        print("End")
        break
    TakeRest()
    counter += 1