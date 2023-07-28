from PIL import ImageGrab
import pytesseract
import time
import numpy as np
import os
import discord
from discord.ext import commands
import io
import aiohttp
from pynput.keyboard import Key, Controller
import pyautogui as pag

fishing_tab_bz = {"x":1105, "y":716}
clay_tab_tab = {"x":1442, "y":571}
ench_clay_bz = {"x":1333, "y":570}
buy_order_create = {"x":1391, "y":570}
custom_amt = {"x":1444, "y":571}
done_typing = {"x":1280, "y":781}
top_plus_one = {"x":1226, "y":569}
order_confirmation = {"x":1281, "y":569}

keyboard = Controller()
flippable_items = ["clay", "snow_block"]
# LOGIC

def mainLoop(amt):
    time.sleep(3)
    timesCycleRecursed = 0
    flip_clay(amt)
    while True:
          if "filled" in read_chat():
            claim_order()
            sell_inv()
            flip_clay(amt)
    

def read_chat(): # Grabs section of chat history and converts to text
    chatGrabImg = ImageGrab.grab(bbox=(0,1050,950,1250))
    chatGrab = pytesseract.image_to_string(chatGrabImg)
    return chatGrab

def player_walk():
    keyboard.press("w")

chatGrab = read_chat()
print(chatGrab) # Used for debugging
if "MATCHED" in chatGrab:
    print("MATCHED OH NO")
if "OUTDATED" in chatGrab or "QUTDATED" in chatGrab or "QUTIDATED" in chatGrab:
    print("OUTDATED OH NO")
if "filled" in chatGrab:
    print("FILLED POGGERS")

def cancel_order():
    open_bazaar()
    time.sleep(0.2)
    pag.moveTo(115, 615, duration=0.1)
    pag.click()
    pag.moveTo(1175, 570, duration=0.1)
    pag.click()

def open_bazaar():
    keyboard.press("/")
    time.sleep(0.05)
    keyboard.release("/")
    time.sleep(0.01)
    keyboard.press("b")
    time.sleep(0.05)
    keyboard.release("b")
    time.sleep(0.01)
    keyboard.press("z")
    time.sleep(0.05)
    keyboard.release("z")
    time.sleep(0.01)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
def matched_actions():
    pass
    timesCycleRecursed = 0

def filled_actions():
    pass

def flip_clay(amt):
    open_bazaar()
    time.sleep(0.5)
    pag.click(1070, 623)
    time.sleep(0.1)
    pag.click(1440, 570)
    time.sleep(0.1)
    pag.click(1335, 570)
    time.sleep(0.1)
    pag.click(1390, 570)
    time.sleep(0.1)
    pag.click(1443, 570)
    time.sleep(0.3)
    keyboard.type(str(amt))
    time.sleep(0.1)
    pag.click(1328, 784)
    time.sleep(0.3)
    pag.click(1228, 570)
    time.sleep(0.1)
    pag.click(1280, 570)
    #print(pag.displayMousePosition())

def claim_order():
    open_bazaar()
    time.sleep(0.5)
    pag.moveTo(1335, 725, duration=0.1)
    pag.click()
    time.sleep(0.2)
    pag.moveTo(1120, 620, duration=0.1)
    pag.click()
    time.sleep(0.2)
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

def sell_inv():
    keyboard.press("t")
    time.sleep(0.1)
    keyboard.release("t")
    time.sleep(0.1)
    keyboard.press("/")
    time.sleep(0.1)
    keyboard.release("/")
    time.sleep(0.1)
    keyboard.press("t")
    time.sleep(0.1)
    keyboard.release("t")
    time.sleep(0.1)
    keyboard.press("r")
    time.sleep(0.1)
    keyboard.release("r")
    time.sleep(0.1)
    keyboard.press("a")
    time.sleep(0.1)
    keyboard.release("a")
    time.sleep(0.1)
    keyboard.press("d")
    time.sleep(0.1)
    keyboard.release("d")
    time.sleep(0.1)
    keyboard.press("e")
    time.sleep(0.1)
    keyboard.release("e")
    time.sleep(0.1)
    keyboard.press("s")
    time.sleep(0.1)
    keyboard.release("s")
    time.sleep(0.1)
    keyboard.press(Key.enter)
    time.sleep(0.1)
    keyboard.release(Key.enter)
    time.sleep(0.2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.3)

    pag.moveTo(1065, 820, duration=0.3)

    for i in range(9):
        pag.leftClick()
        pag.moveRel(55, 0, duration=0.2)
    pag.moveTo(1065, 875)
    time.sleep(0.1)
    for i in range(9):
        pag.leftClick()
        pag.moveRel(55, 0, duration=0.2)
    pag.moveTo(1065, 930)
    time.sleep(0.1)
    for i in range(9):
        pag.leftClick()
        pag.moveRel(55, 0, duration=0.2)
    pag.moveTo(1065, 995)
    time.sleep(0.1)
    for i in range(9):
        pag.leftClick()
        pag.moveRel(55, 0, duration=0.2)

    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

def mouse_show():
    pag.displayMousePosition()

mainLoop(2240)