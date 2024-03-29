# jesus-bypass
## An automation script to bypass stricter EntityJesus behaviors on the anarchy Minecraft server 2b2t.

## OUTDATED AS OF 2023.
As of 2023 this script no longer serves any purpose and will remain archived.<br>
Future updated their Jesus module, and the strict mode works fine these days. If you have that, use it.<br>
Additionally, the release of Lambda 3.3.0 saw a Jesus rewrite which disabled EntityJesus altogether.<br>
If you need a free solution for EntityJesus, my [Lambda](https://github.com/lambda-client/lambda) plugin [Oasis](https://github.com/0xTas/oasis) has an EntityJesus module on-par with Future's.


### History

On April 4th or 5th, 2022, Hausemaster patched various forms of movement including BoatSpeed and EntityJesus. 
EntitySpeed for horses still works fine on many clients, but most forms of EntityJesus became borderline unusable, causing insane rubberbanding and disconnects.

After playing with the changes for some time, I realized that the rubberbanding and disconnects can be largely mitigated by rapidly toggling EntityJesus on-and-off.
Since this isn't a built-in feature on any of the clients that I use, I wrote a python script to do it for me.

This script generates rapid keypresses of a single key only while Minecraft is detected as your active window.
Setting your client's Jesus toggle hotkey to the same key (by default: 'k') will cause EntityJesus to toggle automatically, allowing you to ride your horse over water with around 97% less rubberbanding on Lambda, and at least 50% less rubberbanding with Future.

The script automatically pauses its keyspamming when Minecraft is not the active window, and also whenever you open the chat, because that was annoying.
Be aware that if you open your chat with some key other than 't','/', or ';', you will need to add this to the script to compensate.

I recommend using the free [Lambda client's](https://github.com/lambda-client/lambda) Jesus module with this script for the best experience.
It works okay on Future, but I still rubberband or get kicked off my horse occasionally, whereas that happens almost never with Lambda.
The script may work with additional clients, but I only tested it with Future and Lambda.
I have a feeling that this wouldn't be enough to fix Impact's situation, so I didn't even test it. Let me know if I'm wrong.

I would have made this into a Lambda plugin but I don't know how to write Java yet and I was too lazy to learn just for this.

### Setup

The script only works in Windows, on account of the use of ctypes/wintypes and pygetwindow.
You may be able to workaround this by using the keyboard module exclusively on Linux, but for Windows I selected Ctypes as keyboard alone was too slow.

If you don't have python 3 set up in your path, [fix that first.](https://datatofish.com/add-python-to-windows-path/) 
Then you can run this script either by click-opening it, or via a console with 'python jesus.py'.

On the first run, the script may install a few Python modules, these are:
1. ['pygetwindow'](https://pypi.org/project/PyGetWindow/) - to check the actively focused window so it doesn't spam the hotkey while you are alt-tabbed doing other things.
2. ['schedule'](https://schedule.readthedocs.io/en/stable/) - to run our scheduled keypress events while Minecraft is detected as your active window.
3. ['keyboard'](https://pypi.org/project/keyboard/) - to detect other times when we need to pause keyspamming (like when you open/close the chat).

It is recommended to install these dependencies manually with the included 'requirements.txt' file.
To do this, make sure pip/pip3 is installed and type 'pip3 install -r requirements.txt'.

If this process doesn't work, please ensure that 'pip3' is in your path, or install the modules manually.

Afterwards, this script **will not** install any additional packages, update itself, or make any network connections.

### Usage

In game, you'll want to set your Client's Jesus module to solid mode, and then assign the proper hotkey to it for the script to toggle ('k' is the default).
If you're using Future client, strict and solid mode both work, but neither are quite perfect like Lambda's Solid Jesus is.
You can play with the timings in the script to maybe improve the behavior. The line to change is "schedule.every(0.32).seconds.do(jesus)".
The default 0.32 works perfectly for Lambda, while Future seems to like a slightly smaller timing like 0.29.

The script will automatically stop spamming the hotkey if you open your chat or client menu, and resume once you close it again.
You can also manually pause and resume the script using a hotkey without needing to alt-tab. By default, this is the grave key: '~'.


### Troubleshooting

If the script isn't working, the most likely issue is the title of your Minecraft window, especially if you aren't using Lambda or Forge with Future.
Run the script in debug mode: 'python jesus.py -d' or 'python jesus.py --debug', to see the title of your active window.
Then you can change the if statement logic in the "isFocused" function to match your Minecraft window title.
