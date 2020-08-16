import time

from core.bot import Bot
from core.entity import Entity

bot = Bot()

if __name__ == '__main__':
    color = bot.grab_img().getpixel(Entity.topping_unagi)
    print("Entity.topping_unagi RGB: ", color)
