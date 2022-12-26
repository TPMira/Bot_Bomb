import pyautogui
import time
from datetime import datetime
from discord_webhook import DiscordWebhook
from dotenv import load_dotenv
import os

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

    poly = pyautogui.locateOnScreen("polygon.png", confidence=0.7)
    if poly != None:
        pyautogui.moveTo(poly)
        pyautogui.click(poly)
        time.sleep(2)

    play = pyautogui.locateOnScreen("play.png", confidence=0.65)
    if play != None:
        pyautogui.moveTo(play)
        pyautogui.click(play)
        time.sleep(2)

    mapa = pyautogui.locateOnScreen("treasure.png", confidence=0.65)
    if mapa != None:
        pyautogui.moveTo(mapa)
        pyautogui.click(mapa)
        time.sleep(15)

    carteira = pyautogui.locateOnScreen("wallet.png", confidence=0.7)    
    if carteira != None:
        pyautogui.moveTo(carteira)
        pyautogui.click(carteira)
        time.sleep(2)

        coin = pyautogui.locateOnScreen('coin.png', confidence=0.7)
        c1 = pyautogui.screenshot('shot.png', region=(coin))
        webhook = DiscordWebhook(url, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url, content='Saldo do Bomb')
            webhook.add_file(file=f.read(), filename='shot.png')

            response = webhook.execute()
        os.remove('shot.png')
        time.sleep(2)

    seta = pyautogui.locateOnScreen('seta.png', confidence=0.6)
    if seta != None:
        pyautogui.moveTo(seta)
        pyautogui.click(seta, duration=0.7)
        time.sleep(3)
    
    pyautogui.moveTo(x=1252, y=873)
    pyautogui.click(x=1252, y=873, duration=0.7)
    time.sleep(2)

    menu = pyautogui.locateOnScreen("menu.png", confidence=0.5)
    if menu != None:
        pyautogui.click(menu, duration=0.7)
        time.sleep(2)

    chest = pyautogui.locateOnScreen("chest.png", confidence=0.6)
    if chest != None:
        pyautogui.click(chest, duration=0.7)
        time.sleep(2)

    inventory = pyautogui.locateOnScreen("inventory.png", confidence=0.75)
    if inventory != None:
        pyautogui.moveTo(743, 398)
        time.sleep(0.8)

        info = pyautogui.locateOnScreen("info.png", confidence=0.6)
        
        pyautogui.moveTo(x=456, y=372)
        time.sleep(2)
        print = pyautogui.screenshot('shot.png', region=(info))
        webhook = DiscordWebhook(url2, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 1')
            webhook.add_file(file=f.read(), filename='shot.png')

            response = webhook.execute()
        os.remove('shot.png')

        pyautogui.moveTo(598, 372)
        time.sleep(2)
        print = pyautogui.screenshot('shot.png', region=(info))
        webhook = DiscordWebhook(url2, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 2')
            webhook.add_file(file=f.read(), filename='shot.png')

            response = webhook.execute()
        os.remove('shot.png')

        pyautogui.moveTo(740, 372)
        time.sleep(2)
        print = pyautogui.screenshot('shot.png', region=(info))
        webhook = DiscordWebhook(url2, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 3')
            webhook.add_file(file=f.read(), filename='shot.png')

            response = webhook.execute()
        os.remove('shot.png')

        pyautogui.moveTo(882, 372)
        time.sleep(2)
        print = pyautogui.screenshot('shot.png', region=(info))
        webhook = DiscordWebhook(url2, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 4')
            webhook.add_file(file=f.read(), filename='shot.png')

            response = webhook.execute()
        os.remove('shot.png')

        pyautogui.moveTo(1024, 372)
        time.sleep(2)
        print = pyautogui.screenshot('shot.png', region=(info))
        webhook = DiscordWebhook(url2, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 5')
            webhook.add_file(file=f.read(), filename='shot.png')

            response = webhook.execute()
        os.remove('shot.png')

        pyautogui.moveTo(1024, 515)
        time.sleep(2)
        print = pyautogui.screenshot('shot.png', region=(info))
        webhook = DiscordWebhook(url2, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 6')
            webhook.add_file(file=f.read(), filename='shot.png')

            response = webhook.execute()
        os.remove('shot.png')

        pyautogui.moveTo(882, 515)
        time.sleep(2)
        print = pyautogui.screenshot('shot.png', region=(info))
        webhook = DiscordWebhook(url2, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 7')
            webhook.add_file(file=f.read(), filename='shot.png')

            response = webhook.execute()
        os.remove('shot.png')

        pyautogui.moveTo(740, 515)
        time.sleep(2)
        print = pyautogui.screenshot('shot.png', region=(info))
        webhook = DiscordWebhook(url2, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 8')
            webhook.add_file(file=f.read(), filename='shot.png')

            response = webhook.execute()
        os.remove('shot.png')

        pyautogui.moveTo(598, 515)
        time.sleep(2)
        print = pyautogui.screenshot('shot.png', region=(info))
        webhook = DiscordWebhook(url2, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 9')
            webhook.add_file(file=f.read(), filename='shot.png')

            response = webhook.execute()
        os.remove('shot.png')

        pyautogui.moveTo(456, 515)
        time.sleep(2)
        print = pyautogui.screenshot('shot.png', region=(info))
        webhook = DiscordWebhook(url2, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 10')
            webhook.add_file(file=f.read(), filename='shot.png')

            response = webhook.execute()
        os.remove('shot.png')

        pyautogui.moveTo(456, 667)
        time.sleep(2)
        print = pyautogui.screenshot('shot.png', region=(info))
        webhook = DiscordWebhook(url2, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 11')
            webhook.add_file(file=f.read(), filename='shot.png')

            response = webhook.execute()
        os.remove('shot.png')

        pyautogui.moveTo(598, 667)
        time.sleep(2)
        print = pyautogui.screenshot('shot.png', region=(info))
        webhook = DiscordWebhook(url2, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 12')
            webhook.add_file(file=f.read(), filename='shot.png')

            response = webhook.execute()
        os.remove('shot.png')

        pyautogui.moveTo(740, 667)
        time.sleep(2)
        print = pyautogui.screenshot('shot.png', region=(info))
        webhook = DiscordWebhook(url2, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 13')
            webhook.add_file(file=f.read(), filename='shot.png')

            response = webhook.execute()
        os.remove('shot.png')

        pyautogui.moveTo(882, 667)
        time.sleep(2)
        print = pyautogui.screenshot('shot.png', region=(info))
        webhook = DiscordWebhook(url2, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 14')
            webhook.add_file(file=f.read(), filename='shot.png')

            response = webhook.execute()
        os.remove('shot.png')

        pyautogui.moveTo(1024, 667)
        time.sleep(2)
        print = pyautogui.screenshot('shot.png', region=(info))
        webhook = DiscordWebhook(url2, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 15')
            webhook.add_file(file=f.read(), filename='shot.png')

            response = webhook.execute()
        os.remove('shot.png')
        time.sleep(2)

        site = pyautogui.locateOnScreen('site.png', confidence=0.8)
        if site != None:
            pyautogui.click(site)
            time.sleep(2)
            pyautogui.press('enter')


