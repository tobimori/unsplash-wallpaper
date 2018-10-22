# Unsplash Wallpaper
version = "0.1"
# last edited @ 22.10.2018
# by tobimori

import platform
import os
import urllib.request
import time
import ctypes

def get_image():
    directory = os.getcwd() + "/.unsplash"
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Found no temporary directory. Creating one.")
    filepath = directory + "/" + str(time.time()) + ".jpg"
    try:
        urllib.request.urlretrieve("https://source.unsplash.com/random", filepath)
        print(f"We downloaded that image to {filepath}")
        return filepath
    except:
        print("Something failed while downloading the image.")
        exit()

print(f"Unsplash Wallpaper v{version}\n")
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
