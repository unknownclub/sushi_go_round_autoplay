import time
import os

import win32api
import win32con
from PIL import ImageGrab, Image, ImageOps
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
        self.food_on_hand = {
            "nori": 10,
            "fish egg": 10,
            "rice": 10
        }

        self.sushi_type = {
            "onigiri": [2227, 2163, 2099],
            "gunran maki": [2216, 2089, 1962],
            "california roll": [2547, 2293]
        }

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
            self.food_on_hand['rice'] -= 2
            self.food_on_hand['nori'] -= 1
        elif food == 'california roll':
            self.mouse_click(Entity.rice)
            self.mouse_click(Entity.nori)
            self.mouse_click(Entity.roe)
            self.mouse_click(Entity.press_cook)
            self.food_on_hand['rice'] -= 1
            self.food_on_hand['nori'] -= 1
            self.food_on_hand['fish egg'] -= 1
        elif food == 'gunran maki':
            self.mouse_click(Entity.rice)
            self.mouse_click(Entity.nori)
            self.mouse_click(Entity.roe)
            self.mouse_click(Entity.roe)
            self.mouse_click(Entity.press_cook)
            self.food_on_hand['rice'] -= 1
            self.food_on_hand['nori'] -= 1
            self.food_on_hand['fish egg'] -= 2
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
        time.sleep(1)

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
            if 231 != self.cant_buy_nori():
                self.mouse_click(Entity.topping_nori)
                time.sleep(1)
                self.mouse_click(Entity.press_order)
                self.food_on_hand['nori'] += 10
                print('Buying nori now... | RGB: ', px)
            else:
                print("Cannot buy nori | RGB: ", px)
                self.mouse_click(Entity.dia_down_phone)
        elif component == 'fish egg':
            self.mouse_click(Entity.phone)
            self.mouse_click(Entity.phone_topping)
            px = rgb_im.getpixel(Entity.topping_fish_egg)
            print("current RGB: ", px)
            print("Entity.active_topping_fish_egg: ", Entity.active_topping_fish_egg)
            if 231 != self.cant_buy_roe():
                self.mouse_click(Entity.topping_fish_egg)
                time.sleep(1)
                self.mouse_click(Entity.press_order)
                self.food_on_hand['fish egg'] += 10
                print('Buying fish egg now... | RGB: ', px)
            else:
                print("Cannot buy fish egg | RGB: ", px)
                time.sleep(1)
                self.mouse_click(Entity.dia_down_phone)
        elif component == 'rice':
            self.mouse_click(Entity.phone)
            self.mouse_click(Entity.phone_rice)
            px = rgb_im.getpixel(Entity.rice_rice)
            print("current RGB: ", px)
            print("Entity.active_rice: ", Entity.active_rice)
            if 220 != self.cant_buy_rice():
                self.mouse_click(Entity.rice_rice)
                time.sleep(1)
                self.mouse_click(Entity.press_order)
                print('Buying rice now... | RGB: ', px)
                self.food_on_hand['rice'] += 10
            else:
                print("Cannot buy rice | RGB: ", px)
                time.sleep(1)
                self.mouse_click(Entity.rice_dia_down_phone)
        else:
            pass
        time.sleep(3)

    def check_component(self):
        time.sleep(2)
        for k, v in self.food_on_hand.items():
            if k == "nori" or k == "rice" or k == "fish egg":
                if v < 4:
                    self.buy(k)

    def get_seat_1(self):
        '''
        pixel: 368, 536
        '''
        box = (368, 536, 368 + 79, 536 + 12)
        img = ImageOps.grayscale(self.grab.grab(box))
        sum_color = array(img.getcolors())
        sum_color = sum_color.sum()
        img.save(f'{self.img_path}/seat_1.jpg')
        print("seat_1 color value: ", sum_color)
        return sum_color

    def get_seat_2(self):
        '''
        pixel: 495, 536
        '''
        box = (495, 536, 495 + 79, 536 + 12)
        img = ImageOps.grayscale(self.grab.grab(box))
        sum_color = array(img.getcolors())
        sum_color = sum_color.sum()
        img.save(f'{self.img_path}/seat_2.jpg')
        print("seat_2 color value: ", sum_color)
        return sum_color

    def get_seat_3(self):
        '''
        pixel: 621, 536
        '''
        box = (621, 536, 621 + 79, 536 + 12)
        img = ImageOps.grayscale(self.grab.grab(box))
        sum_color = array(img.getcolors())
        sum_color = sum_color.sum()
        img.save(f'{self.img_path}/seat_3.jpg')
        print("seat_3 color value: ", sum_color)
        return sum_color

    def get_seat_4(self):
        '''
        pixel: 747, 536
        '''
        box = (747, 536, 747 + 79, 536 + 12)
        img = ImageOps.grayscale(self.grab.grab(box))
        sum_color = array(img.getcolors())
        sum_color = sum_color.sum()
        img.save(f'{self.img_path}/seat_4.jpg')
        print("seat_4 color value: ", sum_color)
        return sum_color

    def get_seat_5(self):
        '''
        pixel: 873, 536
        '''
        box = (873, 536, 873 + 79, 536 + 12)
        img = ImageOps.grayscale(self.grab.grab(box))
        sum_color = array(img.getcolors())
        sum_color = sum_color.sum()
        img.save(f'{self.img_path}/seat_5.jpg')
        print("seat_5 color value: ", sum_color)
        return sum_color

    def get_seat_6(self):
        '''
        pixel: 999, 536
        '''
        box = (999, 536, 999 + 79, 536 + 12)
        img = ImageOps.grayscale(self.grab.grab(box))
        sum_color = array(img.getcolors())
        sum_color = sum_color.sum()
        img.save(f'{self.img_path}/seat_6.jpg')
        print("seat_6 color value: ", sum_color)
        return sum_color

    def get_all_seat(self):
        self.get_seat_1()
        self.get_seat_2()
        self.get_seat_3()
        self.get_seat_4()
        self.get_seat_5()
        self.get_seat_6()

    def cant_buy_nori(self):
        '''
        pixel: 978, 780
        '''
        box = (978, 780, 978 + 14, 780 + 8)
        img = ImageOps.grayscale(self.grab.grab(box))
        sum_color = array(img.getcolors())
        sum_color = sum_color.sum()
        img.save(f'{self.img_path}/nori.jpg')
        print("nori color value: ", sum_color)
        return sum_color

    def cant_buy_roe(self):
        '''
        pixel: 1081, 790
        '''
        box = (1081, 790, 1081 + 14, 790 + 8)
        img = ImageOps.grayscale(self.grab.grab(box))
        sum_color = array(img.getcolors())
        sum_color = sum_color.sum()
        img.save(f'{self.img_path}/roe.jpg')
        print("roe color value: ", sum_color)
        return sum_color

    def cant_buy_rice(self):
        '''
        pixel: 1040, 781
        '''
        box = (1040, 781, 1040 + 14, 781 + 9)
        img = ImageOps.grayscale(self.grab.grab(box))
        sum_color = array(img.getcolors())
        sum_color = sum_color.sum()
        img.save(f'{self.img_path}/rice.jpg')
        print("rice color value: ", sum_color)
        return sum_color

    def process_bot(self):
        while True:
            self.check_component()
            if self.get_seat_1() in self.sushi_type["onigiri"]:
                self.cook("onigiri")
            elif self.get_seat_1() in self.sushi_type["gunran maki"]:
                self.cook("gunran maki")
            elif self.get_seat_1() in self.sushi_type["california roll"]:
                self.cook("california roll")
            else:
                pass

            self.check_component()
            if self.get_seat_2() in self.sushi_type["onigiri"]:
                self.cook("onigiri")
            elif self.get_seat_2() in self.sushi_type["gunran maki"]:
                self.cook("gunran maki")
            elif self.get_seat_2() in self.sushi_type["california roll"]:
                self.cook("california roll")
            else:
                pass

            self.check_component()
            if self.get_seat_3() in self.sushi_type["onigiri"]:
                self.cook("onigiri")
            elif self.get_seat_3() in self.sushi_type["gunran maki"]:
                self.cook("gunran maki")
            elif self.get_seat_3() in self.sushi_type["california roll"]:
                self.cook("california roll")
            else:
                pass

            self.check_component()
            if self.get_seat_4() in self.sushi_type["onigiri"]:
                self.cook("onigiri")
            elif self.get_seat_4() in self.sushi_type["gunran maki"]:
                self.cook("gunran maki")
            elif self.get_seat_4() in self.sushi_type["california roll"]:
                self.cook("california roll")
            else:
                pass

            self.check_component()
            if self.get_seat_5() in self.sushi_type["onigiri"]:
                self.cook("onigiri")
            elif self.get_seat_5() in self.sushi_type["gunran maki"]:
                self.cook("gunran maki")
            elif self.get_seat_5() in self.sushi_type["california roll"]:
                self.cook("california roll")
            else:
                pass

            self.check_component()
            if self.get_seat_6() in self.sushi_type["onigiri"]:
                self.cook("onigiri")
            elif self.get_seat_6() in self.sushi_type["gunran maki"]:
                self.cook("gunran maki")
            elif self.get_seat_6() in self.sushi_type["california roll"]:
                self.cook("california roll")
            else:
                pass

            self.clean()
