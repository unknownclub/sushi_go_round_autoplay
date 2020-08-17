import time
import os

import win32api
import win32con
from PIL import ImageGrab, Image
from numpy import *

from core.entity import Entity


class Bot:
    def __init__(self):
        self.grab = ImageGrab
        self.main_path = os.path.dirname(__file__)
        self.img_path = os.path.join(self.main_path, 'img')
        self.box = ()
        self.current_mouse_pos = ()
        self.current_mouse_focus = ()
        self.food = None
        self.component = None
        self.temp_img = None

    def grab_img(self):
        self.box = (337, 458, 1134, 1056)
        img = self.grab.grab()
        self.temp_img = f'{self.img_path}/temp.jpg'
        img.save(self.temp_img)
        # return img

    def focus(self, cord):
        self.current_mouse_focus = cord
        win32api.SetCursorPos((cord[0], cord[1]))

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

    def show_rice_px(self):
        self.grab_img()
        im = Image.open(self.temp_img)
        rgb_im = im.convert('RGB')

        self.focus(Entity.rice_rice)
        px = rgb_im.getpixel(Entity.rice_rice)
        print("active_rice = ", px)
        time.sleep(1)

    def show_topping_px(self):

        self.grab_img()
        im = Image.open(self.temp_img)
        rgb_im = im.convert('RGB')

        self.focus(Entity.topping_nori)
        px = rgb_im.getpixel(Entity.topping_nori)
        print("active_topping_nori = ", px)
        time.sleep(1)

        self.focus(Entity.topping_shrimp)
        px = rgb_im.getpixel(Entity.topping_shrimp)
        print("active_topping_shrimp = ", px)
        time.sleep(1)

        self.focus(Entity.topping_unagi)
        px = rgb_im.getpixel(Entity.topping_unagi)
        print("active_topping_unagi = ", px)
        time.sleep(1)

        self.focus(Entity.topping_salmon)
        px = rgb_im.getpixel(Entity.topping_salmon)
        print("active_topping_salmon = ", px)
        time.sleep(1)

        self.focus(Entity.topping_fish_egg)
        px = rgb_im.getpixel(Entity.topping_fish_egg)
        print("active_topping_fish_egg = ", px)
        time.sleep(1)

    def clean(self):
        self.mouse_click((354, 574))
        self.mouse_click((455, 566))
        self.mouse_click((560, 565))
        self.mouse_click((649, 573))
        self.mouse_click((750, 572))
        self.mouse_click((861, 570))

    def buy(self, component):

        self.grab_img()
        im = Image.open(self.temp_img)
        rgb_im = im.convert('RGB')
        time.sleep(1)

        self.component = component
        if component == 'nori':
            self.mouse_click(Entity.phone)
            self.mouse_click(Entity.phone_topping)
            px = rgb_im.getpixel(Entity.topping_nori)
            print("current RGB: ", px)
            print("Entity.topping_nori: ", Entity.topping_nori)
            if px != Entity.active_topping_nori:
                self.mouse_click(Entity.topping_nori)
                time.sleep(1)
                self.mouse_click(Entity.press_order)
                print('Buying nori now... | RGB: ', px)
            else:
                print("Cannot buy nori | RGB: ", px)
                self.mouse_click(Entity.dia_down_phone)
        elif component == 'salmon':
            self.mouse_click(Entity.phone)
            self.mouse_click(Entity.phone_topping)
            px = rgb_im.getpixel(Entity.topping_salmon)
            print("current RGB: ", px)
            print("Entity.active_topping_salmon: ", Entity.active_topping_salmon)
            if px != Entity.active_topping_salmon:
                self.mouse_click(Entity.topping_salmon)
                time.sleep(1)
                self.mouse_click(Entity.press_order)
                print('Buying salmon now... | RGB: ', px)
            else:
                print("Cannot buy salmon | RGB: ", px)
                time.sleep(1)
                self.mouse_click(Entity.dia_down_phone)
        elif component == 'fish egg':
            self.mouse_click(Entity.phone)
            self.mouse_click(Entity.phone_topping)
            px = rgb_im.getpixel(Entity.topping_fish_egg)
            print("current RGB: ", px)
            print("Entity.active_topping_fish_egg: ", Entity.active_topping_fish_egg)
            if px != Entity.active_topping_fish_egg:
                self.mouse_click(Entity.topping_fish_egg)
                time.sleep(1)
                self.mouse_click(Entity.press_order)
                print('Buying fish egg now... | RGB: ', px)
            else:
                print("Cannot buy fish egg | RGB: ", px)
                time.sleep(1)
                self.mouse_click(Entity.dia_down_phone)

        elif component == 'unagi':
            self.mouse_click(Entity.phone)
            self.mouse_click(Entity.phone_topping)
            px = rgb_im.getpixel(Entity.topping_unagi)
            print("current RGB: ", px)
            print("Entity.active_topping_unagi: ", Entity.active_topping_unagi)
            if px != Entity.active_topping_unagi:
                self.mouse_click(Entity.topping_unagi)
                time.sleep(1)
                self.mouse_click(Entity.press_order)
                print('Buying unagi now... | RGB: ', px)
            else:
                print("Cannot buy unagi | RGB: ", px)
                time.sleep(1)
                self.mouse_click(Entity.dia_down_phone)

        elif component == 'shrimp':
            self.mouse_click(Entity.phone)
            self.mouse_click(Entity.phone_topping)
            px = rgb_im.getpixel(Entity.topping_shrimp)
            print("current RGB: ", px)
            print("Entity.active_topping_shrimp: ", Entity.active_topping_shrimp)
            if px != Entity.active_topping_shrimp:
                self.mouse_click(Entity.topping_shrimp)
                time.sleep(1)
                self.mouse_click(Entity.press_order)
                print('Buying shrimp now... | RGB: ', px)
            else:
                print("Cannot buy shrimp | RGB: ", px)
                time.sleep(1)
                self.mouse_click(Entity.dia_down_phone)
        elif component == 'rice':
            self.mouse_click(Entity.phone)
            self.mouse_click(Entity.phone_rice)
            px = rgb_im.getpixel(Entity.rice_rice)
            print("current RGB: ", px)
            print("Entity.active_rice: ", Entity.active_rice)
            if px != Entity.active_rice:
                self.mouse_click(Entity.rice_rice)
                time.sleep(1)
                self.mouse_click(Entity.press_order)
                print('Buying rice now... | RGB: ', px)
            else:
                print("Cannot buy rice | RGB: ", px)
                time.sleep(1)
                self.mouse_click(Entity.rice_dia_down_phone)
        else:
            pass
