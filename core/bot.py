import time

import win32api
import win32con
from PIL import ImageGrab
from numpy import *


class Bot:
    def __init__(self):
        self.grab = ImageGrab
        self.main_path = os.path.dirname(__file__)
        self.img_path = os.path.join(self.main_path, 'img')
        self.box = ()
        self.current_mouse_pos = ()

    def grab_img(self):
        self.box = (337, 458, 1134, 1056)
        img = self.grab.grab(self.box)
        img.save(f'{self.img_path}/test.jpg')

    def mouse_click(self, cord):
        self.current_mouse_pos = cord
        win32api.SetCursorPos((cord[0], cord[1]))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def start_game(self):
        pass