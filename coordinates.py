import pyautogui as pag
import time

baz = {
    "r1y": "465",
    "r2y": "525",
    "r3y": "580",
    "r4y": "635",
    "r5y": "690",
    "r6y": "745",

    "c1x": "1060",
    "c2x": "1115",
    "c3x": "1170",
    "c4x": "1225",
    "c5x": "1280",
    "c6x": "1335",
    "c7x": "1390",
    "c8x": "1445",
    "c9x": "1490",
}

submenu = {
    "r1y": "495",
    "r2y": "550",
    "r3y": "605",
    "r4y": "660",
    "r5y": "715",
}

order_menu = {
    "r1y": "520",
    "r2y": "575",
    "r3y": "635",
    "r4y": "685",
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
    time.sleep(0.2)

#time.sleep(3)
#click(oddities_cat)
#pag.displayMousePosition()
