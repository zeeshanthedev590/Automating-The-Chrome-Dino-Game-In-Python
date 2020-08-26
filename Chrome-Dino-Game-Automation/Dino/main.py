import pyautogui
from PIL import ImageGrab
import time


def hit(key):
    pyautogui.press(key)
    return


def is_collide(data):
    # Rectangle for birds
    for i in range(230, 265):
        for j in range(275, 378):
            if data[i, j] < 100:
                hit('down')
                return

    # Rectangle for cactus
    for i in range(230, 265):
        for j in range(380, 455):
            if data[i, j] < 100:
                hit('up')
                return
    return


if __name__ == "__main__":
    print("Hey...  Dino game is about to start in 3 seconds...")
    time.sleep(3)
    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        is_collide(data)
