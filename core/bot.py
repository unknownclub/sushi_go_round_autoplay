from PIL import ImageGrab
import os
import time
from numpy import *


class Bot:
    def __init__(self):
        self.grab = ImageGrab
        self.main_path = os.path.dirname(__file__)
        self.img_path = os.path.join(self.main_path, 'img')
        self.box = ()

    def grab_img(self):
        self.box = (337, 458, 1134, 1056)
        img = self.grab.grab(self.box)
        img.save(f'{self.img_path}/test.jpg')
