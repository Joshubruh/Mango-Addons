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
import coordinates

keyboard = Controller()

status = "idle"

def main():
    time.sleep(3)
    buy_order_kismet("5")
    time.sleep(3)
    while True:
        detect_outdated()
        time.sleep(1)

def buy_order_kismet(amt):
    status = "create"
    open_bazaar()
    time.sleep(0.3)
    pag.moveTo(1055, 580, duration=0.1)
    time.sleep(0.1)
    pag.click()
    pag.moveTo(1385, 620, duration=0.1)
    pag.click()
    pag.moveTo(1115, 540, duration=0.1)
    pag.click()
    pag.moveTo(1390, 565, duration=0.1)
    pag.click()
    pag.moveTo(1440, 560, duration=0.1)
    pag.click()
    time.sleep(0.3)
    keyboard.type(str(amt))
    pag.moveTo(1250, 770, duration=0.1)
    pag.click()
    time.sleep(0.1)
    pag.moveTo(1220, 565, duration=0.1)
    pag.click()
    pag.moveTo(1275, 560, duration=0.1)
    pag.click()
    status = "idle"

def open_bazaar():
    status = "bazaar"
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

def outdated_handler():
    any_filled = "NULL"
    time.sleep(3)
    any_filled = claim_order()
    time.sleep(0.3)
    cancel_order()
    time.sleep(0.3)
    if any_filled == "SUCCESS":
        sell_offer_kismets()
    else:
        main()

def create_buy_order_ms1():
    open_bazaar()
    time.sleep(0.5)
    coordinates.click(coordinates.oddities_cat)
    coordinates.click(coordinates.modifiers_menu)
    coordinates.click(coordinates.first_ms)
    coordinates.click(coordinates.create_buy_order)
    coordinates.click(coordinates.buy_order_lowest_preset)
    coordinates.click(coordinates.undercut_by_1)
    coordinates.click(coordinates.confirm_offer)
    while True:
        detect_outdated_ms1_buy()
        time.sleep(1)

def detect_outdated_ms1_sell():
    read_chat()
    if "MATCHED" in read_chat() or "OUT" in read_chat() or "ATED" in read_chat():
        print("Outdated: Relisting Order")
        handle_outdated_ms1_sell()
    elif "filled" in read_chat():
        handle_filled_ms1_sell()
    else:
        pass

def handle_filled_ms1_sell():
    claim_sell()
    create_buy_order_ms1()


def detect_outdated_ms1_buy():
    if "MATCHED" in read_chat() or "OUT" in read_chat() or "ATED" in read_chat():
        print("Outdated: Relisting Order")
        handle_outdated_ms1_buy()
    elif "filled" in read_chat():
        handle_filled_ms1_buy()
    else:
        pass

def sell_offer_ms1():
    open_bazaar()
    time.sleep(0.3)
    coordinates.click(coordinates.oddities_cat)
    coordinates.click(coordinates.modifiers_menu)
    coordinates.click(coordinates.first_ms)
    coordinates.click(coordinates.create_sell_order)
    coordinates.click(coordinates.undercut_by_1)
    coordinates.click(coordinates.confirm_offer)
    while True:
        detect_outdated_ms1_sell()
        time.sleep(1)

def handle_filled_ms1_buy():
    claim_order()
    sell_offer_ms1()

def handle_outdated_ms1_buy():
    cancel_order()
    create_buy_order_ms1()

def handle_outdated_ms1_sell():
    cancel_sell()
    sell_offer_ms1()

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
    time.sleep(1)

    if "Claimed" in read_chat():
        return "SUCCESS"
    else:
        return "FAIL"

def claim_sell():
    open_bazaar()
    time.sleep(0.5)
    pag.moveTo(1335, 725, duration=0.1)
    pag.click()
    time.sleep(0.2)
    pag.moveTo(1115, 575, duration=0.1)
    pag.click()
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(1)

def cancel_sell():
    open_bazaar()
    time.sleep(0.2)
    pag.moveTo(1330, 730, duration=0.1)
    pag.click()
    time.sleep(0.1)
    pag.moveTo(1115, 580, duration=0.1)
    pag.click()
    pag.moveTo(1280, 580, duration=0.1)
    pag.click()
    time.sleep(0.5)
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

def cancel_order():
    open_bazaar()
    time.sleep(1)
    time.sleep(0.2)
    pag.moveTo(1330, 730, duration=0.1)
    pag.click()
    time.sleep(0.1)
    pag.moveTo(1120, 620, duration=0.1)
    pag.click()
    time.sleep(0.1)
    pag.moveTo(1170, 565, duration=0.1)
    pag.click()
    time.sleep(1)

    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

def handle_outdated_sell():
    claim_sell()
    time.sleep(1)
    cancel_sell()

    time.sleep(1)
    sell_offer_kismets()

def sell_offer_kismets():
    open_bazaar()
    time.sleep(0.3)
    pag.moveTo(1055, 580, duration=0.1)
    time.sleep(0.1)
    pag.click()
    pag.moveTo(1385, 620, duration=0.1)
    pag.click()
    pag.moveTo(1115, 540, duration=0.1)
    pag.click()
    pag.moveTo(1440, 580, duration=0.1)
    pag.click()
    pag.moveTo(1220, 565, duration=0.1)
    pag.click()
    pag.moveTo(1275, 560, duration=0.1)
    pag.click()
    while True:
        print("PEEPEEINMYBUTT")
        detect_outdated_sell()
        time.sleep(1)


def handle_filled_sell():
    claim_order()
    main()

def detect_outdated_sell():
    if "MATCHED" in read_chat() or "OUT" in read_chat() or "ATED" in read_chat():
        print("Outdated: Relisting Order")
        handle_outdated_sell()
    elif "filled" in read_chat():
        handle_filled_sell()
    else:
        pass


def filled_handler():
    claim_order()
    open_bazaar()
    sell_offer_kismets()

def detect_outdated():
    if "MATCHED" in read_chat() or "OUT" in read_chat() or "ATED" in read_chat():
        print("Outdated: Relisting Order")
        outdated_handler()
    elif "filled" in read_chat():
        filled_handler()
    else:
        pass


def read_chat(): # Grabs section of chat history and converts to text
    chatGrabImg = ImageGrab.grab(bbox=(0,1100,950,1300))
    chatGrab = pytesseract.image_to_string(chatGrabImg)
    print(chatGrab)
    return chatGrab

#outdated_handler()

#read_chat()

#main()

#time.sleep(3)
#cancel_sell()

#time.sleep(3)
#print(claim_order())    open_bazaar()
time.sleep(3)
create_buy_order_ms1()
#sell_offer_ms1()

#create_buy_order_ms1()
