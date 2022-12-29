import pyautogui
import time
import os

from datetime import datetime
from discord_webhook import DiscordWebhook
from dotenv import load_dotenv
from print import shield
from recuperar_shield import recuperar_shield

load_dotenv()

url = (os.getenv('URL'))
url2 = (os.getenv('URL2'))

while True:

    sens = pyautogui.locateOnScreen('loginSen.png', confidence=0.75)
    if sens != None:
        pyautogui.moveTo(sens)
        pyautogui.click(sens)
        time.sleep(2)

    sens_2 = pyautogui.locateOnScreen("login2.png", confidence=0.75)
    if sens_2 != None:
        pyautogui.moveTo(sens_2)
        pyautogui.click(sens_2)
        time.sleep(2)

    poly = pyautogui.locateOnScreen("polygon.png", confidence=0.75)
    if poly != None:
        pyautogui.moveTo(poly)
        pyautogui.click(poly)
        time.sleep(2)

    play = pyautogui.locateOnScreen("play.png", confidence=0.75)
    if play != None:
        pyautogui.moveTo(play)
        pyautogui.click(play)
        time.sleep(5)

    mapa = pyautogui.locateOnScreen("treasure.png", confidence=0.75)
    if mapa != None:
        pyautogui.moveTo(mapa)
        pyautogui.click(mapa)
        time.sleep(15)

    carteira = pyautogui.locateOnScreen("wallet.png", confidence=0.75)    
    if carteira != None:
        pyautogui.moveTo(carteira)
        pyautogui.click(carteira)
        time.sleep(2)

        coin = pyautogui.locateOnScreen('coin.png', confidence=0.75)
        c1 = pyautogui.screenshot('shot.png', region=(coin))
        webhook = DiscordWebhook(url, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url, content='Saldo do Bomb')
            webhook.add_file(file=f.read(), filename='shot.png')

            response = webhook.execute()
        os.remove('shot.png')
        time.sleep(2)

    seta = pyautogui.locateOnScreen('seta.png', confidence=0.75)
    if seta != None:
        pyautogui.moveTo(seta)
        pyautogui.click(seta, duration=0.7)
        time.sleep(3)
    
    pyautogui.moveTo(x=1252, y=873)
    pyautogui.click(x=1252, y=873, duration=0.7)
    time.sleep(2)

    menu = pyautogui.locateOnScreen("menu.png", confidence=0.65)
    if menu != None:
        pyautogui.click(menu, duration=0.7)
        time.sleep(2)

    #chest = pyautogui.locateOnScreen("chest.png", confidence=0.65)
    #if chest != None:
        #pyautogui.moveTo(chest)
        #pyautogui.click(chest)
        #time.sleep(2)
        
    #shield()
    #time.sleep(2)

    recuperar_shield()
    time.sleep(2)

    site = pyautogui.locateOnScreen('site.png', confidence=0.8)
    if site != None:
        pyautogui.click(site)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(10)


