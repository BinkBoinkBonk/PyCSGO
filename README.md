
# Welcome to PyCSGO!

  

External python cheats for CSGO including Grenade previews, allowing the user to access sv_cheat protected commands such as "cl_showpos", and wallhacks. These hacks should always work with the offsets being updated automatically using [Hazedumper](https://github.com/frk1/hazedumper) and reading the games scan patterns.

  
  

# Files

  

GernadeHelp.py works by bypassing sv_cheats and allowing the user to enable "cl_grenadepreview" in VAC protected servers.

  

ShowPos.py works the same way as GernadeHelp.py by bypassing sv_cheats and editing the games memory to allow "cl_showpos" to be run on VAC protected servers.

  

Wallhack.py works by getting offsets from [Hazedumper](https://github.com/frk1/hazedumper) and then using these offsets to edit the games memory allowing for the glow effect to be enabled on all players.

  

requirements.txt is needed in the installation of the cheats. (uses pip to install the needed libraries to run the .py files)

  

Installation.bat installs the libraries listed in requirements.txt

  

StartAll.bat starts all of the cheats at once. (Walls, Grenade Prediction, cl_showpos unblocked)

  

## Installation

  

Have [python](https://www.python.org/) 3+ version installed on your computer. Run Installation.bat to install the needed libraries for the python files to work.

  

## "Injecting"

  

MAKE SURE THE GAME IS RUNNING. To start the hacks either open each python individually for each cheat you would like to use or run StartAll.bat to run them all at once. (GernadeHelp.py and ShowPos.py will flash quickly then close, and Wallhacks.py will stay open. If you use StartAll.bat one window will open and stay open.)
