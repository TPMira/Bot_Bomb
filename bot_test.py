import pyautogui
import time
from datetime import datetime
from discord_webhook import DiscordWebhook
import os

url = ''

while True:

    sens = pyautogui.locateOnScreen('loginSen.png', confidence=0.75)
    if sens != None:
        pyautogui.click(sens)
        time.sleep(4)

    sens_2 = pyautogui.locateOnScreen("login2.png", confidence=0.75)
    if sens_2 != None:
        pyautogui.click(sens_2)
        time.sleep(4)

    poly = pyautogui.locateOnScreen("polygon.png", confidence=0.7)
    if poly != None:
        pyautogui.click(poly)
        time.sleep(4)

    play = pyautogui.locateOnScreen("play.png", confidence=0.65)
    if play != None:
        pyautogui.click(play)
        time.sleep(4)

    mapa = pyautogui.locateOnScreen("treasure.png", confidence=0.65)
    if mapa != None:
        pyautogui.click(mapa)
        time.sleep(15)

    carteira = pyautogui.locateOnScreen("wallet.png", confidence=0.7)    
    if carteira != None:
        pyautogui.click(carteira)
        time.sleep(4)

        coin = pyautogui.locateOnScreen('coin.png', confidence=0.7)
        c1 = pyautogui.screenshot('shot.png', region=(coin))
        webhook = DiscordWebhook(url, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url, content='Saldo do Bomb')
            webhook.add_file(file=f.read(), filename='shot.png')

            response = webhook.execute()
        os.remove('shot.png')

    seta = pyautogui.locateOnScreen('seta.png', confidence=0.65)
    if seta != None:
        pyautogui.click(seta)
        time.sleep(2)

    menu = pyautogui.locateOnScreen("menu.png", confidence=0.6)
    if menu != None:
        pyautogui.click(menu)
        time.sleep(2)

    hero = pyautogui.locateOnScreen("hero.png", confidence=0.6)
    if hero != None:
        pyautogui.click(hero)
        time.sleep(2)

    character = pyautogui.locateOnScreen('character.png', confidence=0.75)
    if character != None:
        escudo_critico = pyautogui.locateOnScreen('escudo_critico.png', confidence=0.9)
        if escudo_critico != None:
            pyautogui.click(x=419, y=318)
            time.sleep(2)
            info = pyautogui.locateOnScreen('info.png', confidence=0.6)
            c1 = pyautogui.screenshot('shot.png', region=(info))
            webhook = DiscordWebhook(url, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url, content='Escudo Critico 1')
            webhook.add_file(file=f.read(), filename='shot.png')

            response = webhook.execute()
        os.remove('shot.png')
        time.sleep(3)

        pyautogui.click(x=417, y=421)
        time.sleep(2)
        pyautogui.click(x=417, y=421)
        if escudo_critico != None:
            c1 = pyautogui.screenshot('shot.png', region=(info))
            webhook = DiscordWebhook(url, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url, content='Escudo Critico 2')
            webhook.add_file(file=f.read(), filename='shot.png')
            response = webhook.execute()
        os.remove('shot.png')
        time.sleep(3)

        pyautogui.click(x=417, y=524)
        time.sleep(2)
        pyautogui.click(x=417, y=524)
        if escudo_critico != None:
            c1 = pyautogui.screenshot('shot.png', region=(info))
            webhook = DiscordWebhook(url, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url, content='Escudo Critico 3')
            webhook.add_file(file=f.read(), filename='shot.png')
            response = webhook.execute()
        os.remove('shot.png')
        time.sleep(3)

        pyautogui.click(x=417, y=627)
        time.sleep(2)
        pyautogui.click(x=417, y=627)
        if escudo_critico != None:
            c1 = pyautogui.screenshot('shot.png', region=(info))
            webhook = DiscordWebhook(url, username='screenShot1.jpg')

        with open('shot.png', 'rb') as f:
            webhook = DiscordWebhook(url, content='Escudo Critico 4')
            webhook.add_file(file=f.read(), filename='shot.png')
            response = webhook.execute()
        os.remove('shot.png')
        time.sleep(3)
        break



    