import pyautogui as pag
import time

baz = {
    "r1y": "278",
    "r2y": "330",
    "r3y": "385",
    "r4y": "440",
    "r5y": "500",
    "r6y": "545",

    "c1x": "740",
    "c2x": "794",
    "c3x": "850",
    "c4x": "900",
    "c5x": "960",
    "c6x": "1010",
    "c7x": "1065",
    "c8x": "1120",
    "c9x": "1170",
}

submenu = {
    "r1y": "303",
    "r2y": "355",
    "r3y": "410",
    "r4y": "465",
    "r5y": "520",
}

order_menu = {
    "r1y": "330",
    "r2y": "385",
    "r3y": "440",
    "r4y": "490",
}

# Important Menu Locations


create_buy_order = order_menu["r2y"] + " " + baz["c7x"]
buy_order_lowest_preset = order_menu["r2y"] + " " + baz["c2x"]

undercut_by_1 = order_menu["r2y"] + " " + baz["c4x"]
confirm_offer = order_menu["r2y"] + " " + baz["c5x"]

create_sell_order = order_menu["r2y"] + " " + baz["c8x"]

oddities_cat = baz["r5y"] + " " + baz["c1x"]
orders = baz["r5y"] + " " + baz["c6x"]
first_sell_offer = order_menu["r2y"] + " " + baz["c2x"]

modifiers_menu = baz["r3y"] + " " + baz["c8x"]
first_ms = submenu["r3y"] + " " + baz["c2x"]
serum = submenu["r3y"] + " " + baz["c7x"]

def debugmouse():
    pag.displayMousePosition()

def splice(coords):
    splicedCoords = coords.split(" ")
    return splicedCoords

def click(menu):
    y = splice(menu)[0]
    x = splice(menu)[1]
    pag.moveTo(int(x), int(y), duration=0.1)
    pag.click()
    time.sleep(0.4)

#time.sleep(3)
#click(oddities_cat)
#pag.displayMousePosition()
