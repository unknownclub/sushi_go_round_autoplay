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



