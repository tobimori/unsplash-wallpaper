import platform
import sys
import os
import urllib.request
import time
import dbus

def get_desktop_environment():
    # From http://stackoverflow.com/questions/2035657/what-is-my-current-desktop-environment
    # and http://ubuntuforums.org/showthread.php?t=652320
    # and http://ubuntuforums.org/showthread.php?t=652320
    # and http://ubuntuforums.org/showthread.php?t=1139057
    if sys.platform in ["win32", "cygwin"]:
        return "windows"
    elif sys.platform == "darwin":
        return "mac"
    else:  # Most likely either a POSIX system or something not much common
        desktop_session = os.environ.get("DESKTOP_SESSION")
        if desktop_session is not None:  # easier to match if we doesn't have  to deal with caracter cases
            desktop_session = desktop_session.lower()
            if desktop_session in ["gnome", "unity", "cinnamon", "mate", "xfce4", "lxde", "fluxbox",
                                   "blackbox", "openbox", "icewm", "jwm", "afterstep", "trinity", "kde"]:
                return desktop_session
            ## Special cases ##
            # Canonical sets $DESKTOP_SESSION to Lubuntu rather than LXDE if using LXDE.
            # There is no guarantee that they will not do the same with the other desktop environments.
            elif "xfce" in desktop_session or desktop_session.startswith("xubuntu"):
                return "xfce4"
            elif desktop_session.startswith("ubuntu"):
                return "unity"
            elif desktop_session.startswith("lubuntu"):
                return "lxde"
            elif desktop_session.startswith("kubuntu"):
                return "kde"
            elif desktop_session.startswith("razor"):  # e.g. razorkwin
                return "razor-qt"
            elif desktop_session.startswith("wmaker"):  # e.g. wmaker-common
                return "windowmaker"
        if os.environ.get('KDE_FULL_SESSION') == 'true':
            return "kde"
        elif os.environ.get('GNOME_DESKTOP_SESSION_ID'):
            if not "deprecated" in os.environ.get('GNOME_DESKTOP_SESSION_ID'):
                return "gnome2"
        # From http://ubuntuforums.org/showthread.php?t=652320
        elif self.is_running("xfce-mcs-manage"):
            return "xfce4"
        elif self.is_running("ksmserver"):
            return "kde"
    return "unknown"

def get_image():
    #dirvar = os.path.join(".unsplash")
    #if not os.path.exists(dirvar):
    #    os.makedirs(dirvar)
    filename = str(time.time()) + ".jpg"
    urllib.request.urlretrieve("https://source.unsplash.com/daily",  filename)
    return filename

version = "0.1"

print(f"Unsplash Wallpaper v{version}\n")
de = get_desktop_environment()
osvar = platform.system()
print(f"You are using {osvar} with {de.upper()} installed.")


if osvar == "Linux":
    if de == "kde":
        filename = get_image()
    #    currdir = os.getcwd()
    #    bus = dbus.SessionBus()
    #    remote_object = bus.get_object("org.kde.plasmashell","/PlasmaShell")
    #    remote_object.evaluateScript('var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = "org.kde.image";d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");d.writeConfig("Image", "file://' + currdir + '/pictures/' + filename + '.jpg' + '")}', dbus_interface = "org.kde.PlasmaShell")

    else:
        print("Sorry, currently only supporting KDE.")
else:
    print("Sorry, only supporting some limited DEs on Linux right now. Feel free to fork and add support ;)")