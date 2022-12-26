import pyautogui
import time
import os
from discord_webhook import DiscordWebhook

url='https://discord.com/api/webhooks/1056610946254110812/OpWHmlwn8P4K3Ee84RY5NulGqGlYN8T0AyJsvGP-Ce1E9r8n-5LgzSYG9d2jRoSg7gKV'

pyautogui.moveTo(598, 372)
time.sleep(0.8)
pixel = pyautogui.pixel(1303, 625)
info = pyautogui.locateOnScreen("info.png", confidence=0.6)
if pixel == (255, 0, 0):
    print = pyautogui.screenshot('shot.png', region=(info))
    webhook = DiscordWebhook(url, username='screenShot1.jpg')

    with open('shot.png', 'rb') as f:
        webhook = DiscordWebhook(url, content='Saldo do Bomb')
        webhook.add_file(file=f.read(), filename='shot.png')

        response = webhook.execute()
    os.remove('shot.png')