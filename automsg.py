# automsg

import pyautogui
import time
while True:
    time.sleep(2)
    pyautogui.typewrite('This is from a bot')
    pyautogui.press('enter')
    
import pywhatkit
pywhatkit.sendwhatmsg('+88018188888', 'Hi from py', 18, 10)
