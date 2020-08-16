import time

from core.bot import Bot
from core.entity import Entity

bot = Bot()

if __name__ == '__main__':
    #bot.mouse_click(Entity.topping_nori)
    time.sleep(1)
    color_nori = bot.grab_img().getpixel(Entity.topping_nori)
    # color_unagi = bot.grab_img().getpixel(Entity.topping_unagi)
    # color_shrimp = bot.grab_img().getpixel(Entity.topping_shrimp)
    print("Entity.topping_nori RGB: ", color_nori)
    # print("Entity.topping_unagi RGB: ", color_unagi)
    # print("Entity.topping_shrimp RGB: ", color_shrimp)

