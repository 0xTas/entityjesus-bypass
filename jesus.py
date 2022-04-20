##########################################
#   2b2t EntityJesus Bypass/Workaround   #
#                                        #
#           Author: 0x_Tas               #
#          Discord: Tas#5187             #
#            License: MIT                #
##########################################

##########################################
#  This script generates quick repeated  #
#  keypresses when Minecraft is set as   #
#         your active window.            #
#                                        #
#  It is basically just a fancy macro.   #
##########################################


# This script was written for Python 3.10.2, but should be compatible with all recent versions of Python 3.
import os
from time import sleep
if os.name != 'nt':
    print('Sorry, the solution used to generate keyboard events for this bypass only works on Windows.\nConsider researching an alternate solution for generating low-latency keypresses on Linux/Mac.')
    raise SystemExit(1)
try:
    import pygetwindow as gw
except ImportError:
    try:
        import subprocess
        subprocess.call(['pip3','install','pygetwindow'])
        os.system('python jesus.py')
    except KeyboardInterrupt:
        raise SystemExit(1)
    except Exception as err:
        print(f'Could not import pygetwindow module.\nError: {err}\nExiting..')
        raise SystemExit(1)
try:
    import keyboard
except ImportError:
    try:
        import subprocess
        subprocess.call(['pip3','install','keyboard'])
        os.system('python jesus.py')
    except KeyboardInterrupt:
        raise SystemExit(1)
    except Exception as err:
        print(f'Could not import Keyboard module. \nError: {err}\nExiting..')
        raise SystemExit(1)
try:
    import schedule
except ImportError:
    try:
        import subprocess
        subprocess.call(['pip3','install','schedule'])
        os.system('python jesus.py')
    except KeyboardInterrupt:
        raise SystemExit(1)
    except Exception as err:
        print(f'Could not import schedule module.\nError: {err}\nExiting..')
        raise SystemExit(1)
from sys import argv as args
import ctypes
from ctypes import wintypes


#################################################################################################
#                                                                                               #
#  Borrowed From: https://stackoverflow.com/questions/13564851/how-to-generate-keyboard-events  #
#                   Using Ctypes because the Keyboard module alone is too slow.                 #
#                                                                                               #
#################################################################################################
user32 = ctypes.WinDLL('user32', use_last_error=True)
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008
INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2
MAPVK_VK_TO_VSC = 0

VKEY_K = 0x4B # This is our virtual key variable, it is currently set to 'K'. Change this if you use a different Jesus toggle hotkey other than 'K'.
# Microsoft virtual key hexcodes: https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure): # Unused for our purposes
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure): # Class for generating virtual keyboard events.
    _fields_ = (("wVk",         wintypes.WORD),
            ("wScan",       wintypes.WORD),
            ("dwFlags",     wintypes.DWORD),
            ("time",        wintypes.DWORD),
            ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk, MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure): # Unused for our purposes
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure): # Input Class
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize

# Functions

def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
#############################################################
#                                                           #
#                   End Borrowed Code.                      #
#                                                           #
#############################################################

os.system('cls')

switch = False
isPaused = False
debug = False

# Parse args for optional debug mode.
for arg in args:
    if arg == '-d' or arg.lower() == '--debug':
        debug = True


def stfu(): # Enables "do this if that else pass" if statements on one line, since 'pass' won't work in these single-line statements for some reason but we also can't eschew 'else' so...
    pass
def die(code):
    raise SystemExit(code)


def isFocused():
    try:
        if gw.getActiveWindow().title == 'Minecraft 1.12.2' or 'Lambda' in gw.getActiveWindow().title:
            return True
        else:
            return False
    except AttributeError:
        stfu() # Ignore harmless AttributeError from switching active windows.
        return False


def jesus():
    global switch
    try:
        print(gw.getActiveWindow().title) if debug else stfu() # Use debug mode to troubleshoot by checking that your window title matches the following logic.

        if not switch and not isPaused: # MIGHT NEED TO CHANGE BELOW THIS LINE IF YOUR MINECRAFT WINDOW HAS A DIFFERENT TITLE
            if gw.getActiveWindow().title == 'Minecraft 1.12.2' or 'Lambda' in  gw.getActiveWindow().title: # If using a different set-up, your window title may differ from these 2!
                PressKey(VKEY_K)
                sleep(0.003)
                ReleaseKey(VKEY_K)
            else:
                return
    except AttributeError:
        stfu()            # Ignore harmless AttributeError from switching active windows.
    except Exception as err:
        print(f'Errored: {err}.') # Report unhandled errors.
        try:
            ReleaseKey(VKEY_K)
            die(1)
        except:
            die(1)


schedule.every(0.32).seconds.do(jesus) # Main interval for our toggle speed. You may need or wish to adjust this number slightly or depending on your Client.
print('Running EntityJesus Bypass..')

try:
    while True:
        if isFocused():

            # Prevent the script from continuously spamming when we open chat menus or client menus.
            if (keyboard.is_pressed('t') or keyboard.is_pressed('/') or keyboard.is_pressed(';') or keyboard.is_pressed('y') or keyboard.is_pressed('right_shift')) and not switch: 
                
                # This way we can still type. Hotkey macro is disabled while switch boolean is True.
                switch = True 
                print('Paused Bypass.') if not isPaused else stfu()
                sleep(.420) # Brief sleep to prevent script from racing between paused/resumed.

            # Resume auto-toggle once we exit from chat or client-menu. Right-shift is missing here because it doesn't also close the client menu, at least for Future.
            elif (keyboard.is_pressed('enter') or keyboard.is_pressed('escape') or keyboard.is_pressed('y')) and switch: 
                print('Resumed Bypass.') if not isPaused else stfu()
                switch = False
                sleep(.420)

            elif keyboard.is_pressed('grave'): # Manual pause-mode toggle. You can change the pause hotkey here, default 'grave' is the '~' key.
                if isPaused:
                    isPaused = False
                    print('Resumed Bypass.')
                    sleep(.420)

                elif not isPaused:
                    isPaused = True
                    print('Paused Bypass.')
                    sleep(.420)

        schedule.run_pending()
        sleep(0.001)
except KeyboardInterrupt: # Control-C to terminate the script.
    die(0)
