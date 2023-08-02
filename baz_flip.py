#--------------- IMPORTS / BOILERPLATE
from PIL import ImageGrab, Image
import pytesseract
import time
import numpy as np
import os
from pynput.keyboard import Key, Controller
import pyautogui as pag
import coordinates
import log
import tkinter as tk

startTime = 0
endTime = 0

keyboard = Controller()
#--------------- USER INTERFACE 

def main_gui():
    window = tk.Tk(width=400, height=500)
    windowTitle = tk.Label(text="MangoAddons - Joshubruh")
    windowTitle.pack()
    window.mainloop()

def main():
    print('''
88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8  ,adPPYba,   
88P'   "88"    "8a ""     `Y8 88P'   `"8a a8"    `Y88 a8"     "8a  
88      88      88 ,adPPPPP88 88       88 8b       88 8b       d8  
88      88      88 88,    ,88 88       88 "8a,   ,d88 "8a,   ,a8"  
88      88      88 `"8bbdP"Y8 88       88  `"YbbdP"Y8  `"YbbdP"'   
                                           aa,    ,88              
                                            "Y8bbdP"          ''')
    print("----------------------------")
    print("MangoAddons, Bazaar Flipper Module")
    print("Programmed by @joshubruh")
    print("----------------------------")
    get_action()

def get_action():
    print("Enter your desired module: [Master Star, Kismet, Serum]: ")
    module = input("> ")

    print("Now, enter if you want to start with a SELL, or a BUY (if you already have an item, run SELL) [sell/buy]")
    action = input("> ")

    if module == "Master Star":
        if action == "sell":
            print("MS1 Sell - Starting in 5 Seconds")
            time.sleep(5)
            sell_offer_ms1(True)
        if action == "buy":
            print("MS1 Buy - Starting in 5 Seconds")
            time.sleep(5)
            create_buy_order_ms1(True)
        else:
            print("UH-OH! Action Invalid! Please re-enter your action")
            get_action()

    elif module == "Kismet":
        print("UH-OH! The Kismet module has been discontinued! Please run a different module")
        get_action()

    if module == "Serum":
        if action == "sell":
            print("Serum Sell - Starting in 5 Seconds")
            time.sleep(5)
            sell_offer_serum(True)
        if action == "buy":
            print("Serum Buy - Starting in 5 Seconds")
            time.sleep(5)
            create_buy_order_serum(True)
        else:
            print("UH-OH! Action Invalid! Please re-enter your action")
            get_action()




#--------------- GLOBAL COMMANDS
def read_chat(): # Grabs section of chat history and converts to text
    chatGrabImg = ImageGrab.grab(bbox=(0,1140,950,1340))
    chatGrab = pytesseract.image_to_string(chatGrabImg)
    return chatGrab

def determine_gui_open(called_from):
    img = ImageGrab.grab()
    color = img.getpixel((1430, 420))
    if color == (198, 198, 215):
        time.sleep(0.3)
        keyboard.press(Key.esc)
        time.sleep(0.1)
        keyboard.release(Key.esc)

def execute(arg, needsDelay):
    if needsDelay:
        time.sleep(10)
    for char in arg:
        keyboard.press(char)
        time.sleep(0.35)
        keyboard.release(char)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def reconnect(trigger):
    print("[LOG]: Disconnect Detected")
    os.system("espeak disconnect_detected")
    time.sleep(5)
    pag.click(1275,790)
    pag.moveTo(890,315)
    time.sleep(0.3)
    pag.click()

    execute("/play skyblock", True)
    time.sleep(10)

    if trigger == "buy": # Switch all instances of ms1 for whatever you are currently flippinh
        cancel_order(True)
        create_buy_order_serum(False)
    elif trigger == "sell":
        cancel_sell(True)
        sell_offer_serum(False)



def determine_connected(trigger):
    chatGrabImg = ImageGrab.grab(bbox=(1112,768,1437,816))
    chatGrab = pytesseract.image_to_string(chatGrabImg)
    if "Back" in chatGrab and "list" in chatGrab:
        reconnect(trigger)

def warpout_failsafe(called_from):
    print("[LOG]: Warpout Detected")
    os.system("espeak executing_warpout_protocol")
    time.sleep(65)
    execute("/play skyblock")
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
    time.sleep(1)
    pag.moveTo(1280, 580, duration=0.1)
    pag.click()
    time.sleep(1)
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(0.5)
    keyboard.press("/")
    keyboard.release("/")
    time.sleep(0.1)
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
    time.sleep(1)

    keyboard.press(Key.esc)
    time.sleep(0.1)
    keyboard.release(Key.esc)
    time.sleep(0.5)
    keyboard.press("/")
    keyboard.release("/")
    time.sleep(0.5)

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
def sell_offer_ms1(firstexec):
    if firstexec == True:
        open_bazaar()
    else:
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
    log.start()
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
    elif len(read_chat()) < 5:
        determine_connected("sell")
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
    elif len(read_chat()) < 5:
        determine_connected("buy")

def handle_filled_ms1_sell():
    print("[LOG]: MS1 Sell Filled In: "+str(round(log.end()))+" Seconds!")
    claim_sell(False)
    time.sleep(0.5)
    create_buy_order_ms1(False)

def handle_filled_ms1_buy():
    print("[LOG]: MS1 Buy Filled")
    claim_order(False)
    time.sleep(1)
    sell_offer_ms1(False)
    
def handle_outdated_ms1_buy():
    print("[LOG]: MS1 Buy Outdated")
    print("\a")
    cancel_order(False)
    time.sleep(1)
    create_buy_order_ms1(False)

def handle_outdated_ms1_sell():
    print("[LOG]: MS1 Sell Outdated")
    print("\a")
    time.sleep(0.7)
    cancel_sell(False)
    time.sleep(1)
    sell_offer_ms1(False)

# Start Serum Module

def sell_offer_serum(firstexec):
    determine_gui_open("NULL")
    if firstexec == True:
        open_bazaar()
    else:
        bz_wo_slash()
    time.sleep(0.3)
    coordinates.click(coordinates.oddities_cat)
    coordinates.click(coordinates.modifiers_menu)
    coordinates.click(coordinates.serum)
    coordinates.click(coordinates.create_sell_order)
    coordinates.click(coordinates.undercut_by_1)
    coordinates.click(coordinates.confirm_offer)
    keyboard.press("/")
    keyboard.release("/")
    while True:
        detect_outdated_ms1_sell()
        time.sleep(1)

def create_buy_order_serum(firstexec):
    determine_gui_open("NULL")
    log.start()
    if firstexec == False:
        bz_wo_slash()
    else:
        open_bazaar()

    time.sleep(0.5)
    coordinates.click(coordinates.oddities_cat)
    coordinates.click(coordinates.modifiers_menu)
    coordinates.click(coordinates.serum)
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
        warpout_failsafe("serum_sell")
    elif len(read_chat()) < 5:
        determine_connected("sell")
    else:
        pass

def detect_outdated_ms1_buy():
    if "MATCHED" in read_chat() or "OUT" in read_chat() or "ATED" in read_chat():
        print("Outdated: Relisting Order")
        handle_outdated_ms1_buy()
    elif "filled" in read_chat():
        handle_filled_ms1_buy()
    elif "restart" in read_chat():
        warpout_failsafe("serum_buy")
    elif len(read_chat()) < 5:
        determine_connected("buy")

def handle_filled_ms1_sell():
    print("[LOG]: Serum Sell Filled In: "+str(round(log.end()))+" Seconds!")
    claim_sell(False)
    time.sleep(0.5)
    create_buy_order_serum(False)

def handle_filled_ms1_buy():
    print("[LOG]: Serum Buy Filled")
    print("\a")
    claim_order(False)
    time.sleep(1)
    sell_offer_serum(False)
    
def handle_outdated_ms1_buy():
    print("[LOG]: Serum Buy Outdated")
    print("\a")
    cancel_order(False)
    time.sleep(1)
    create_buy_order_serum(False)

def handle_outdated_ms1_sell():
    print("[LOG]: Serum Sell Outdated")
    print("\a")
    time.sleep(0.7)
    cancel_sell(False)
    time.sleep(1)
    sell_offer_serum(False)

main_gui()
