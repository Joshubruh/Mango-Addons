#--------------- IMPORTS / BOILERPLATE
from PIL import ImageGrab
import pytesseract
import time
import numpy as np
import os
from pynput.keyboard import Key, Controller
import pyautogui as pag
import coordinates


keyboard = Controller()
#--------------- GLOBAL COMMANDS
def read_chat(): # Grabs section of chat history and converts to text
    chatGrabImg = ImageGrab.grab(bbox=(0,1140,950,1340))
    chatGrab = pytesseract.image_to_string(chatGrabImg)
    return chatGrab

def warpout_failsafe(called_from):
    os.system("espeak executing_warpout_protocol")
    time.sleep(60)
    time.sleep(0.1)
    keyboard.press("i")
    time.sleep(0.1)
    keyboard.release("i")
    time.sleep(0.1)
    keyboard.press("s")
    time.sleep(0.1)
    keyboard.release("s")
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    keyboard.press("/")
    time.sleep(0.1)
    keyboard.release("/")

    if called_from == "ms1_sell":
        handle_outdated_ms1_sell()
    elif called_from == "ms1_buy":
        handle_outdated_ms1_buy()


def open_bazaar():
    status = "bazaar"
    keyboard.press("/")
    time.sleep(0.1)
    keyboard.release("/")
    time.sleep(0.1)
    keyboard.press("b")
    time.sleep(0.1)
    keyboard.release("b")
    time.sleep(0.1)
    keyboard.press("z")
    time.sleep(0.1)
    keyboard.release("z")
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def bz_wo_slash():
    time.sleep(1)
    keyboard.press("b")
    time.sleep(0.1)
    keyboard.release("b")
    time.sleep(0.1)
    keyboard.press("z")
    time.sleep(0.1)
    keyboard.release("z")
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def claim_sell(slash):
    if slash:
        open_bazaar()
    else:
        bz_wo_slash()
    time.sleep(1)
    pag.moveTo(1335, 725, duration=0.1)
    pag.click()
    time.sleep(1)
    pag.moveTo(1115, 575, duration=0.1)
    pag.click()
    time.sleep(1)
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(1)
    keyboard.press("/")
    keyboard.release("/")
    time.sleep(1)

def cancel_sell(slash):
    if slash:
        open_bazaar()
    else:
        bz_wo_slash()
    time.sleep(1)
    pag.moveTo(1330, 730, duration=0.1)
    pag.click()
    time.sleep(1)
    pag.moveTo(1115, 580, duration=0.1)
    pag.click()
    pag.moveTo(1280, 580, duration=0.1)
    pag.click()
    time.sleep(1)
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

def cancel_order(slash):
    if slash:
        open_bazaar()
    else:
        bz_wo_slash()
    time.sleep(1)
    time.sleep(1)
    pag.moveTo(1330, 730, duration=0.1)
    pag.click()
    time.sleep(1)
    pag.moveTo(1120, 620, duration=0.1)
    pag.click()
    time.sleep(1)
    pag.moveTo(1170, 565, duration=0.1)
    pag.click()
    time.sleep(0.35)

    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(0.5)
    keyboard.press("/")
    keyboard.release("/")
    time.sleep(0.1)

#--------------- START KISMET SUB-MOD
def main_kismet():
    time.sleep(3)
    buy_order_kismet("5")
    time.sleep(3)
    while True:
        detect_outdated_kismet()
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
    keyboard.press("/")
    keyboard.release("/")
    status = "idle"

def outdated_handler_kismet():
    any_filled = "NULL"
    time.sleep(3)
    any_filled = claim_order()
    time.sleep(0.3)
    cancel_order()
    time.sleep(0.3)
    if any_filled == "SUCCESS":
        sell_offer_kismets()
    else:
        main_kismet()

def claim_order(slash):
    if slash:
        open_bazaar()
    else:
        bz_wo_slash()
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
    keyboard.press("/")
    keyboard.release("/")
    time.sleep(0.1)


    if "Claimed" in read_chat():
        return "SUCCESS"
    else:
        return "FAIL"

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
        detect_outdated_sell_kismet()
        time.sleep(1)

def detect_outdated_sell_kismet():
    if "MATCHED" in read_chat() or "OUT" in read_chat() or "ATED" in read_chat():
        print("Outdated: Relisting Order")
        handle_outdated_sell_kismet()
    elif "filled" in read_chat():
        handle_filled_sell_kismet()
    else:
        pass

def detect_outdated_kismet():
    if "MATCHED" in read_chat() or "OUT" in read_chat() or "ATED" in read_chat():
        print("Outdated: Relisting Order")
        outdated_handler_kismet()
    elif "filled" in read_chat():
        filled_handler_kismets()
    else:
        pass

def filled_handler_kismets():
    claim_order()
    open_bazaar()
    sell_offer_kismets()

def handle_filled_sell_kismet():
    claim_order()
    main_kismet()

def handle_outdated_sell_kismet():
    claim_sell()
    time.sleep(1)
    cancel_sell()

    time.sleep(1)
    sell_offer_kismets()
#--------------- START OF MS1 SUB-MOD
def sell_offer_ms1():
    bz_wo_slash()
    time.sleep(0.3)
    coordinates.click(coordinates.oddities_cat)
    coordinates.click(coordinates.modifiers_menu)
    coordinates.click(coordinates.first_ms)
    coordinates.click(coordinates.create_sell_order)
    coordinates.click(coordinates.undercut_by_1)
    coordinates.click(coordinates.confirm_offer)
    keyboard.press("/")
    keyboard.release("/")
    while True:
        detect_outdated_ms1_sell()
        time.sleep(1)

def create_buy_order_ms1(firstexec):

    if firstexec == False:
        bz_wo_slash()
    else:
        open_bazaar()

    time.sleep(0.5)
    coordinates.click(coordinates.oddities_cat)
    coordinates.click(coordinates.modifiers_menu)
    coordinates.click(coordinates.first_ms)
    coordinates.click(coordinates.create_buy_order)
    coordinates.click(coordinates.buy_order_lowest_preset)
    coordinates.click(coordinates.undercut_by_1)
    coordinates.click(coordinates.confirm_offer)
    keyboard.press("/")
    keyboard.release("/")
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
    elif "restart" in read_chat():
        warpout_failsafe("ms1_sell")
    else:
        pass

def detect_outdated_ms1_buy():
    if "MATCHED" in read_chat() or "OUT" in read_chat() or "ATED" in read_chat():
        print("Outdated: Relisting Order")
        handle_outdated_ms1_buy()
    elif "filled" in read_chat():
        handle_filled_ms1_buy()
    elif "restart" in read_chat():
        warpout_failsafe("ms1_buy")
    else:
        pass

def handle_filled_ms1_sell():
    print("Cycle Completed!")
    claim_sell(False)
    time.sleep(0.5)
    create_buy_order_ms1(False)

def handle_filled_ms1_buy():
    print("\a")
    claim_order(False)
    time.sleep(0.5)
    sell_offer_ms1()
    
def handle_outdated_ms1_buy():
    print("\a")
    cancel_order(False)
    time.sleep(0.5)
    create_buy_order_ms1(False)

def handle_outdated_ms1_sell():
    print("\a")
    time.sleep(0.7)
    cancel_sell(False)
    keyboard.press("/")
    keyboard.release("/")
    time.sleep(0.5)
    sell_offer_ms1()


# DEBUG - Used to run each function individually, as to detect issues

time.sleep(3)
#outdated_handler()
#read_chat()
#main_kismet()
#time.sleep(3)
#cancel_sell()
#time.sleep(3)
#print(claim_order())
create_buy_order_ms1(True)
#sell_offer_ms1()
#cancel_sell(False)
#create_buy_order_ms1()
#coordinates.debugmouse()
#handle_filled_ms1_buy()
#sell_offer_ms1()
