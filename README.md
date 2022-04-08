# jesus-bypass
## An automation script to bypass stricter EntityJesus behaviors on the anarchy Minecraft server 2b2t.

On April 4th or 5th, 2022, Hausemaster patched various forms of movement including BoatSpeed and EntityJesus. 
EntitySpeed for horses still works fine on many clients, but most forms of EntityJesus became borderline unusable, causing insane rubberbanding and disconnects.

After playing with the changes for some time, I realized that the rubberbanding and disconnects can be largely mitigated by rapidly toggling EntityJesus on-and-off.
Since this isn't a built-in feature on any of the clients that I use, I wrote a python script to do it for me.

This script generates rapid keypresses of a single key only while Minecraft is detected as your active window.
Setting your client's Jesus toggle hotkey to the same key (by default: 'k') will cause EntityJesus to toggle automatically, allowing you to ride your horse over water with roughly 90% less rubberbanding than any current configs for Future and Lambda can accomplish.
The script automatically pauses its keyspamming when Minecraft is not the active window, and also whenever you open the chat, because that was annoying.
Be aware that if you open your chat with some key other than 't','/', or ';', you will need to add this to the script to compensate.

The bypass may work with additional clients, but I only tested it with Future and Lambda.
I have a feeling that this wouldn't be enough to fix Impact's garbage, so I didn't even test it. Let me know if I'm wrong.

### Setup

The script only works in Windows, on account of the use of ctypes/wintypes.
You may be able to workaround this by using the keyboard module exclusively on Linux, but for Windows I selected Ctypes as it was faster.

If you don't have python 3 set up in your path, [fix that first.](https://datatofish.com/add-python-to-windows-path/) 
Then you can run this script either by click-opening it, or via a console with 'python jesus.py'.

On the first run, the script may install a few Python modules, these are:
1. 'pygetwindow' - to check the actively focused window so it doesn't spam the hotkey while you are alt-tabbed doing other things.
2. 'schedule' - to run our scheduled keypress events while Minecraft is detected as your active window.
3. 'keyboard' - to detect other times when we need to pause keyspamming (when you open/close the chat).

If this process doesn't work, please ensure that 'pip3' is in your path, or install the modules manually.

Afterwards, this script **will not** install any additional packages, update itself, or make any network connections.

### Troubleshooting

If the script doesn't work, the most likely issue is the title of your Minecraft window, especially if you aren't using Lambda or Forge with Future.
Run the script in debug mode 'python jesus.py -d' or 'python jesus.py --debug' to see the title of your active window.
Then you can change the if statement logic in the Jesus function to match your Minecraft window title.
