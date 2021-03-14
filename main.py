import webbrowser
import time
import pyautogui


for i in range(10):
    webbrowser.open("www.damianfallon.blogspot.com")
    time.sleep(15)
    x=600
    y=600
    pyautogui.moveTo(x,y, duration = 10)

    pyautogui.scroll(-1000)

    x=1341
    y=12
    pyautogui.moveTo(x,y, duration = 10)
    pyautogui.click()

    webbrowser.open("www.latestonmars.blogspot.com")
    time.sleep(15)

    x=600
    y=600
    pyautogui.moveTo(x,y, duration = 10)

    pyautogui.scroll(-1000)

    x=1341
    y=12
    pyautogui.moveTo(x,y, duration = 10)
    pyautogui.click()






