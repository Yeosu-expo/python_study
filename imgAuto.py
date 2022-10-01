import pyautogui

num =pyautogui.locateCenterOnScreen('1.png', confidence=0.6)

pyautogui.moveTo(num)