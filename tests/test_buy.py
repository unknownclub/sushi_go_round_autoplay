import time

import win32api
import win32con

from core.bot import Bot
from core.entity import Entity

bot = Bot()

def test_get_path():
    print("=== test path ===")
    print("bot.main_path: ", bot.main_path)
    print("bot.img_path: ", bot.img_path)


def test_grab_image():
    print("=== test grab image ===")
    bot.grab_img()
    print("=== grab image OK! ===")


def test_mouse_click():
    print("=== test mouse click ===")
    cord = (50, 50)
    print("mouse click at (x, y): ", cord)
    bot.mouse_click(cord)


def test_start_game():
    print("=== test start game ===")
    bot.start_game()


def test_cook_onigiri():
    print("=== test cooking onigiri ===")
    bot.cook('onigiri')


def test_cook_california_roll():
    print("=== test cooking california roll ===")
    bot.cook('california roll')


def test_cook_gunran_maki():
    print("=== test cooking gunran maki ===")
    bot.cook('gunran maki')

if __name__ == '__main__':
    '''
    bot.buy("nori")
    win32api.SetCursorPos(Entity.topping_nori)
    color = bot.grab_img().getpixel(Entity.topping_nori)
    print("topping_nori", color)
    time.sleep(1)
    bot.mouse_click(Entity.dia_down_phone)
    time.sleep(1)

    bot.buy("nori")
    win32api.SetCursorPos(Entity.topping_salmon)
    color = bot.grab_img().getpixel(Entity.topping_salmon)
    print("topping_salmon", color)
    time.sleep(1)
    bot.mouse_click(Entity.dia_down_phone)
    time.sleep(1)

    bot.buy("nori")
    win32api.SetCursorPos(Entity.topping_fish_egg)
    color = bot.grab_img().getpixel(Entity.topping_fish_egg)
    print("topping_fish_egg", color)
    time.sleep(1)
    bot.mouse_click(Entity.dia_down_phone)
    time.sleep(1)

    bot.buy("nori")
    win32api.SetCursorPos(Entity.topping_unagi)
    color = bot.grab_img().getpixel(Entity.topping_unagi)
    print("topping_unagi", color)
    time.sleep(1)
    bot.mouse_click(Entity.dia_down_phone)
    time.sleep(1)

    bot.buy("nori")
    win32api.SetCursorPos(Entity.topping_shrimp)
    color = bot.grab_img().getpixel(Entity.topping_shrimp)
    print("topping_shrimp", color)
    time.sleep(1)
    bot.mouse_click(Entity.dia_down_phone)
    time.sleep(1)
    '''

    '''
    topping_nori (88, 68, 57)
    topping_salmon (174, 101, 48)
    topping_fish_egg (225, 181, 105)
    topping_unagi (208, 168, 97)
    topping_shrimp (225, 181, 105)
    '''

    while True:
        test_get_path()
        test_grab_image()
        # test_mouse_click()
        test_start_game()
        time.sleep(2)
        test_cook_onigiri()
        time.sleep(2)
        test_cook_california_roll()
        time.sleep(2)
        test_cook_gunran_maki()

        bot.buy('nori')
        bot.buy('salmon')
        bot.buy('fish egg')
        bot.buy('unagi')
        bot.buy('shrimp')

        test_get_path()
        test_grab_image()
        # test_mouse_click()
        test_start_game()
        time.sleep(2)
        test_cook_onigiri()
        time.sleep(2)
        test_cook_california_roll()
        time.sleep(2)
        test_cook_gunran_maki()

        bot.clean()


