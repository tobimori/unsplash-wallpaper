# Unsplash Wallpaper
__version__ = "1.1"
# last edited @ 22.10.2018
# by tobimori

import platform
import os
import urllib.request
import time
import ctypes
import traceback

def get_screensize(multiplier):
    try:
        user32 = ctypes.windll.user32
        screensize = f"{user32.GetSystemMetrics(78)*multiplier}x{user32.GetSystemMetrics(79)*multiplier}"
        print(f"Detected virtual monitor size {user32.GetSystemMetrics(78)}x{user32.GetSystemMetrics(79)}.")
        if multiplier > 1:
            print(f"Multiplying to {screensize} for better quality.")
        return screensize
    except:
        print(f"Encountered some problems while detecting your display size.")
        traceback.print_exc()
        exit()


def get_image(multiplier):
    directory = os.getcwd() + "/.unsplash"
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Found no temporary directory. Creating one.")
    filepath = directory + "/" + str(time.time()) + ".jpg"
    print(f"Starting download...")
    try:
        screensize = get_screensize(multiplier)
        urllib.request.urlretrieve("https://source.unsplash.com/random/" + screensize, filepath)
        print(f"Downloaded image from source.unsplash.com/random/{screensize} to {filepath}")
        return filepath
    except:
        print(f"Encountered some problems while downloading the image.")
        traceback.print_exc()
        exit()


print(f"Unsplash Wallpaper v{__version__} by tobimori\n")
osvar = platform.system()

if osvar == "Windows":
    print("Found that you're using Windows.")
    print("Well, I hate Windows, but it was the easiest thing to implement, so let's do this!\n")
    filepath_absolute = get_image(2)
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath_absolute, 0)
        print("\nDone!")
        exit()
    except:
        print(f"Couldn't set your wallpaper.")
        traceback.print_exc()
        exit()
else:
    print("Sorry, only supporting Windows right now. Feel free to fork and add support ;)")
