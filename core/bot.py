import time
import os

import win32api
import win32con
from PIL import ImageGrab
from numpy import *

from core.entity import Entity


class Bot:
    def __init__(self):
        self.grab = ImageGrab
        self.main_path = os.path.dirname(__file__)
        self.img_path = os.path.join(self.main_path, 'img')
        self.box = ()
        self.current_mouse_pos = ()
        self.food = None
        self.component = None

    def grab_img(self):
        self.box = (337, 458, 1134, 1056)
        img = self.grab.grab()
        return img

    def mouse_click(self, cord):
        self.current_mouse_pos = cord
        win32api.SetCursorPos((cord[0], cord[1]))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(0.2)

    def start_game(self):
        # play
        self.mouse_click((577, 565))
        # skip
        self.mouse_click((870, 818))
        # continue
        self.mouse_click((548, 739))

    def cook(self, food):
        self.food = food
        if food == 'onigiri':
            self.mouse_click(Entity.rice)
            self.mouse_click(Entity.rice)
            self.mouse_click(Entity.nori)
            self.mouse_click(Entity.press_cook)
        elif food == 'california roll':
            self.mouse_click(Entity.rice)
            self.mouse_click(Entity.nori)
            self.mouse_click(Entity.roe)
            self.mouse_click(Entity.press_cook)
        elif food == 'gunran maki':
            self.mouse_click(Entity.rice)
            self.mouse_click(Entity.nori)
            self.mouse_click(Entity.roe)
            self.mouse_click(Entity.roe)
            self.mouse_click(Entity.press_cook)
        else:
            pass

    def buy(self, component):
        self.component = component
        if component == 'nori':
            self.mouse_click(Entity.phone)
            self.mouse_click(Entity.phone_topping)
            px = self.grab_img().getpixel(Entity.topping_nori)
            if px != (88, 68, 57):
                self.mouse_click(Entity.topping_nori)
                time.sleep(1)
                self.mouse_click(Entity.press_order)
                print('Buying nori now... | px: ', px)
            else:
                print("Cannot buy nori | px: ", px)
                self.mouse_click(Entity.dia_down_phone)
        elif component == 'salmon':
            self.mouse_click(Entity.phone)
            self.mouse_click(Entity.phone_topping)
            px = self.grab_img().getpixel(Entity.topping_salmon)
            if px != (174, 101, 48):
                self.mouse_click(Entity.topping_salmon)
                time.sleep(1)
                self.mouse_click(Entity.press_order)
                print('Buying salmon now... | px: ', px)
            else:
                print("Cannot buy salmon | px: ", px)
                self.mouse_click(Entity.dia_down_phone)
        elif component == 'fish egg':
            self.mouse_click(Entity.phone)
            self.mouse_click(Entity.phone_topping)
            px = self.grab_img().getpixel(Entity.topping_fish_egg)
            if px != (225, 181, 105):
                self.mouse_click(Entity.topping_fish_egg)
                time.sleep(1)
                self.mouse_click(Entity.press_order)
                print('Buying fish egg now... | px: ', px)
            else:
                print("Cannot buy fish egg | px: ", px)
                self.mouse_click(Entity.dia_down_phone)

        elif component == 'unagi':
            self.mouse_click(Entity.phone)
            self.mouse_click(Entity.phone_topping)
            px = self.grab_img().getpixel(Entity.topping_unagi)
            if px != (208, 168, 97):
                self.mouse_click(Entity.topping_unagi)
                time.sleep(1)
                self.mouse_click(Entity.press_order)
                print('Buying unagi now... | px: ', px)
            else:
                print("Cannot buy unagi | px: ", px)
                self.mouse_click(Entity.dia_down_phone)

        elif component == 'shrimp':
            self.mouse_click(Entity.phone)
            self.mouse_click(Entity.phone_topping)
            px = self.grab_img().getpixel(Entity.topping_shrimp)
            if px != (225, 181, 105):
                self.mouse_click(Entity.topping_shrimp)
                time.sleep(1)
                self.mouse_click(Entity.press_order)
                print('Buying shrimp now... | px: ', px)
            else:
                print("Cannot buy shrimp | px: ", px)
                self.mouse_click(Entity.dia_down_phone)
        else:
            pass

    def clean(self):
        self.mouse_click((354, 574))
        self.mouse_click((455, 566))
        self.mouse_click((560, 565))
        self.mouse_click((649, 573))
        self.mouse_click((750, 572))
        self.mouse_click((861, 570))

