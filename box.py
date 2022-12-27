import pyautogui

box = pyautogui.locateOnScreen('numero.png', confidence=0.6)
print(box)