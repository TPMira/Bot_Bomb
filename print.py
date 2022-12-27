import pyautogui
from discord_webhook import DiscordWebhook
import os
from dotenv import load_dotenv
import time

load_dotenv()

url2=(os.getenv('URL2'))

def shield():

    pyautogui.moveTo(x=456, y=372)
    time.sleep(2)

    info_escudo = (1270, 597, 68, 50)
    escudo_critico = pyautogui.locateOnScreen('pixel_vermelho.png', confidence=0.8, region=info_escudo)
    if escudo_critico != None:
        print = pyautogui.screenshot('shot_escudo.png', region=(info_escudo))
        webhook = DiscordWebhook(url2, username='screenShot2.jpg')

        with open('shot_escudo.png', 'rb') as f:
                    webhook = DiscordWebhook(url2, content='Escudo Hero 1')
                    webhook.add_file(file=f.read(), filename='shot_escudo.png')

        response = webhook.execute()
        os.remove('shot_escudo.png')

    pyautogui.moveTo(598, 372)
    time.sleep(2)
    info_escudo = (1270, 597, 68, 50)
    escudo_critico = pyautogui.locateOnScreen('pixel_vermelho.png', confidence=0.8, region=info_escudo)
    if escudo_critico != None:
        print = pyautogui.screenshot('shot_escudo.png', region=(info_escudo))
        webhook = DiscordWebhook(url2, username='screenShot2.jpg')

        with open('shot_escudo.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 2')
            webhook.add_file(file=f.read(), filename='shot_escudo.png')

            response = webhook.execute()
        os.remove('shot_escudo.png')

    pyautogui.moveTo(740, 372)
    time.sleep(2)
    info_escudo = (1270, 597, 68, 50)
    escudo_critico = pyautogui.locateOnScreen('pixel_vermelho.png', confidence=0.8, region=info_escudo)
    if escudo_critico != None:
        print = pyautogui.screenshot('shot_escudo.png', region=(info_escudo))
        webhook = DiscordWebhook(url2, username='screenShot2.jpg')

        with open('shot_escudo.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 3')
            webhook.add_file(file=f.read(), filename='shot_escudo.png')

            response = webhook.execute()
        os.remove('shot_escudo.png')

    pyautogui.moveTo(882, 372)
    time.sleep(2)
    info_escudo = (1270, 597, 68, 50)
    escudo_critico = pyautogui.locateOnScreen('pixel_vermelho.png', confidence=0.8, region=info_escudo)
    if escudo_critico != None:
        print = pyautogui.screenshot('shot_escudo.png', region=(info_escudo))
        webhook = DiscordWebhook(url2, username='screenShot2.jpg')

        with open('shot_escudo.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 4')
            webhook.add_file(file=f.read(), filename='shot_escudo.png')

            response = webhook.execute()
        os.remove('shot_escudo.png')

    pyautogui.moveTo(1024, 372)
    time.sleep(2)
    info_escudo = (1270, 597, 68, 50)
    escudo_critico = pyautogui.locateOnScreen('pixel_vermelho.png', confidence=0.8, region=info_escudo)
    if escudo_critico != None:
        print = pyautogui.screenshot('shot_escudo.png', region=(info_escudo))
        webhook = DiscordWebhook(url2, username='screenShot2.jpg')

        with open('shot_escudo.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 5')
            webhook.add_file(file=f.read(), filename='shot_escudo.png')

            response = webhook.execute()
        os.remove('shot_escudo.png')

    pyautogui.moveTo(1024, 515)
    time.sleep(2)
    info_escudo = (1270, 597, 68, 50)
    escudo_critico = pyautogui.locateOnScreen('pixel_vermelho.png', confidence=0.8, region=info_escudo)
    if escudo_critico != None:
        print = pyautogui.screenshot('shot_escudo.png', region=(info_escudo))
        webhook = DiscordWebhook(url2, username='screenShot2.jpg')

        with open('shot_escudo.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 6')
            webhook.add_file(file=f.read(), filename='shot_escudo.png')

            response = webhook.execute()
        os.remove('shot_escudo.png')

    pyautogui.moveTo(882, 515)
    time.sleep(2)
    info_escudo = (1270, 597, 68, 50)
    escudo_critico = pyautogui.locateOnScreen('pixel_vermelho.png', confidence=0.8, region=info_escudo)
    if escudo_critico != None:
        print = pyautogui.screenshot('shot_escudo.png', region=(info_escudo))
        webhook = DiscordWebhook(url2, username='screenShot2.jpg')

        with open('shot_escudo.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 7')
            webhook.add_file(file=f.read(), filename='shot_escudo.png')

            response = webhook.execute()
        os.remove('shot_escudo.png')

    pyautogui.moveTo(740, 515)
    time.sleep(2)
    info_escudo = (1270, 597, 68, 50)
    escudo_critico = pyautogui.locateOnScreen('pixel_vermelho.png', confidence=0.8, region=info_escudo)
    if escudo_critico != None:
        print = pyautogui.screenshot('shot_escudo.png', region=(info_escudo))
        webhook = DiscordWebhook(url2, username='screenShot2.jpg')

        with open('shot_escudo.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 8')
            webhook.add_file(file=f.read(), filename='shot_escudo.png')

            response = webhook.execute()
        os.remove('shot_escudo.png')

    pyautogui.moveTo(598, 515)
    time.sleep(2)

    info_escudo = (1270, 597, 68, 50)
    escudo_critico = pyautogui.locateOnScreen('pixel_vermelho.png', confidence=0.8, region=info_escudo)
    if escudo_critico != None:
        print = pyautogui.screenshot('shot_escudo.png', region=(info_escudo))
        webhook = DiscordWebhook(url2, username='screenShot2.jpg')

        with open('shot_escudo.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 9')
            webhook.add_file(file=f.read(), filename='shot_escudo.png')

            response = webhook.execute()
        os.remove('shot_escudo.png')

    pyautogui.moveTo(456, 515)
    time.sleep(2)

    info_escudo = (1270, 597, 68, 50)
    escudo_critico = pyautogui.locateOnScreen('pixel_vermelho.png', confidence=0.8, region=info_escudo)
    if escudo_critico != None:
        print = pyautogui.screenshot('shot_escudo.png', region=(info_escudo))
        webhook = DiscordWebhook(url2, username='screenShot2.jpg')

        with open('shot_escudo.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 10')
            webhook.add_file(file=f.read(), filename='shot_escudo.png')

            response = webhook.execute()
        os.remove('shot_escudo.png')

    pyautogui.moveTo(456, 667)
    time.sleep(2)

    info_escudo = (1270, 597, 68, 50)
    escudo_critico = pyautogui.locateOnScreen('pixel_vermelho.png', confidence=0.8, region=info_escudo)
    if escudo_critico != None:
        print = pyautogui.screenshot('shot_escudo.png', region=(info_escudo))
        webhook = DiscordWebhook(url2, username='screenShot2.jpg')

        with open('shot_escudo.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 11')
            webhook.add_file(file=f.read(), filename='shot_escudo.png')

            response = webhook.execute()
        os.remove('shot_escudo.png')

    pyautogui.moveTo(598, 667)
    time.sleep(2)

    info_escudo = (1270, 597, 68, 50)
    escudo_critico = pyautogui.locateOnScreen('pixel_vermelho.png', confidence=0.8, region=info_escudo)
    if escudo_critico != None:
        print = pyautogui.screenshot('shot_escudo.png', region=(info_escudo))
        webhook = DiscordWebhook(url2, username='screenShot2.jpg')

        with open('shot_escudo.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 12')
            webhook.add_file(file=f.read(), filename='shot_escudo.png')

            response = webhook.execute()
        os.remove('shot_escudo.png')

    pyautogui.moveTo(740, 667)
    time.sleep(2)

    info_escudo = (1270, 597, 68, 50)
    escudo_critico = pyautogui.locateOnScreen('pixel_vermelho.png', confidence=0.8, region=info_escudo)
    if escudo_critico != None:
        print = pyautogui.screenshot('shot_escudo.png', region=(info_escudo))
        webhook = DiscordWebhook(url2, username='screenShot2.jpg')

        with open('shot_escudo.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 13')
            webhook.add_file(file=f.read(), filename='shot_escudo.png')

            response = webhook.execute()
        os.remove('shot_escudo.png')

    pyautogui.moveTo(882, 667)
    time.sleep(2)

    info_escudo = (1270, 597, 68, 50)
    escudo_critico = pyautogui.locateOnScreen('pixel_vermelho.png', confidence=0.8, region=info_escudo)
    if escudo_critico != None:
        print = pyautogui.screenshot('shot_escudo.png', region=(info_escudo))
        webhook = DiscordWebhook(url2, username='screenShot2.jpg')

        with open('shot_escudo.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 14')
            webhook.add_file(file=f.read(), filename='shot_escudo.png')

    pyautogui.moveTo(1024, 667)
    time.sleep(2)

    info_escudo = (1270, 597, 68, 50)
    escudo_critico = pyautogui.locateOnScreen('pixel_vermelho.png', confidence=0.8, region=info_escudo)
    if escudo_critico != None:
        print = pyautogui.screenshot('shot_escudo.png', region=(info_escudo))
        webhook = DiscordWebhook(url2, username='screenShot2.jpg')

        with open('shot_escudo.png', 'rb') as f:
            webhook = DiscordWebhook(url2, content='Escudo Hero 15')
            webhook.add_file(file=f.read(), filename='shot_escudo.png')
