import platform
import os
import urllib.request
import time
import ctypes
import traceback
import sys

__title__ = 'Unsplash Wallpaper'
__version__ = "1.2"
__author__ = 'tobimori'
# last edited @ 22.10.2018


def get_screensize(multiplier):
    try:
        user32 = ctypes.windll.user32
        screensize = f"{user32.GetSystemMetrics(78)*multiplier}x{user32.GetSystemMetrics(79)*multiplier}"
        print(f"\r[+] Status: Detected virtual monitor size {user32.GetSystemMetrics(78)}x{user32.GetSystemMetrics(79)}.", end="")
        if multiplier > 1:
            print(f"\r[+] Status: Multiplying to {screensize} for better quality.", end="")
        return screensize
    except:
        print(f"\r[-] Status: Encountered some problems while detecting your display size.", end="")
        traceback.print_exc()
        sys.exit(1)


def get_image(multiplier):
    directory = os.getcwd() + "/.unsplash"
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("\r[+] Status: Create temporary directory", end="")
    filepath = directory + "/" + str(time.time()) + ".jpg"
    print(f"\r[+] Status: Starting download...", end="")
    try:
        screensize = get_screensize(multiplier)
        urllib.request.urlretrieve("https://source.unsplash.com/random/" + screensize, filepath)
        print(f"\r[+] Status: Downloaded image from source.unsplash.com/random/{screensize} to {filepath}", end="")
        return filepath
    except:
        print(f"\r[-] Status: Encountered some problems while downloading the image.", end="")
        traceback.print_exc()
        sys.exit(1)


print(f"\033[32m{__title__} v{__version__} by {__author__}\n")
print("\033[0m")
osvar = platform.system()

if osvar == "Windows":
    print("\r[+] Status: Detected System: Windows", end="")
    print("\033[33m\nWell, I hate Windows, but it was the easiest thing to implement, so let's do this!\n")
    print("\033[0m")
    filepath_absolute = get_image(2)
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath_absolute, 0)
        print("\n[+] Status: Done!", end="")
    except:
        print(f"\r[-] Status: Error - Couldn't set your wallpaper.", end="")
        traceback.print_exc()
        sys.exit(1)
else:
    print("\r[-] Status: Sorry, only supporting Windows right now. Feel free to fork and add support ;)", end="")
