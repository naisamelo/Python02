import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://www.amazon.com.br/")
pyautogui.press("enter")

time.sleep(5)