from core.bot import Bot

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


if __name__ == '__main__':
    test_get_path()
    test_grab_image()
    # test_mouse_click()
    test_start_game()
