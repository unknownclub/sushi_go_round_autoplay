from core.bot import Bot
import threading
import os
import keyboard
import time
import sys
import psutil


def handle_kb_exit(delay):
    while True:
        time.sleep(delay)
        if keyboard.is_pressed('q'):
            print("Program ready to exit.")
            current_system_pid = os.getpid()
            process = psutil.Process(current_system_pid)
            process.terminate()


bot = Bot()
if __name__ == '__main__':
    try:
        threading.Thread(target=handle_kb_exit, args=(1,)).start()
        bot.start_game()
        bot.process_bot()
    except Exception as e:
        print(e)
        sys.exit()
