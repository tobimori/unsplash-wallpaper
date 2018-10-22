# Unsplash Wallpaper
__version__ = "0.1"
# last edited @ 22.10.2018
# by tobimori

import platform
import os
import urllib.request
import time
import ctypes


def get_screensize(int):
    try:
        user32 = ctypes.windll.user32
        screensize = f"{user32.GetSystemMetrics(78)*int}x{user32.GetSystemMetrics(79)*int}"
        print(f"Detected screen size {user32.GetSystemMetrics(78)}x{user32.GetSystemMetrics(79)}.")
        if int == 2:
            print(f"Doubling to {screensize} for better quality.")
        return screensize
    except:
        print("Something failed while trying to get your display size.")
        exit()


def get_image():
    directory = os.getcwd() + "/.unsplash"
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Found no temporary directory. Creating one.")
    filepath = directory + "/" + str(time.time()) + ".jpg"
    try:
        screensize = get_screensize(2)
        urllib.request.urlretrieve("https://source.unsplash.com/random/" + screensize, filepath)
        print(f"We downloaded the image from source.unsplash.com/random/{screensize} to {filepath}")
        return filepath
    except:
        print("Something failed while downloading the image.")
        exit()

print(f"Unsplash Wallpaper v{__version__} by tobimori\n")
osvar = platform.system()

if osvar == "Windows":
    print("We found that you're using Windows. Great. Let's do this!")
    filepath_absolute = get_image()
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath_absolute, 0)
    except:
        print("We couldn't set your wallpaper.")
        exit()
else:
    print("Sorry, only supporting Windows right now. Feel free to fork and add support ;)")
