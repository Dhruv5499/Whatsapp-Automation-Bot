#SEND A GENERAL WHATSAPP MESSAGE TO MULTIPLE UNKNOWN NUMBERS AT ONCE!

import webbrowser
import pyautogui as gui
import time 

interval=5
position = 680,323

numbers={919779572922}

#msg = """Hi.%0aThis is a test message."""
msg = """Hi, I am clearing your payment for the Shooting Stars followers task.%0aKindly, send me your Gpay or Paytm number so that I can send your payment!%0a%0aYou brought 1 follower.%0aYour Payment: ₹5 x 1 = ₹5"""
for i in numbers:
    url= 'https://wa.me/{}?text={}'.format(i,msg)
    webbrowser.open(url)
    time.sleep(5)
    gui.click(position)
    time.sleep(5)
    gui.press('enter')
    time.sleep(interval)
    print(i)