from core.bot import Bot

bot = Bot()

if __name__ == '__main__':
    print("=== test path ===")
    print("bot.main_path: ", bot.main_path)
    print("bot.img_path: ", bot.img_path)

    print("=== test grab image ===")
    bot.grab_img()
    print("=== grab image OK! ===")

    print("=== test mouse click ===")
    cord = (50, 50)
    print("mouse click at (x, y): ", cord)
    bot.mouse_click(cord)