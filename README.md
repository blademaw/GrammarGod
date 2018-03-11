# GrammarGod

A fun project with www.github.com/jigg3r about fixing people's grammar.

## Installation

Deploying the project is easy; simply clone or download the GrammarGod.py file, make sure you've installed  *PyEnchant*, *tkinter* and *re*, and run the file.

## How it Works

We're currently experimenting with Python 3's tkinter module for GUIs, practicing our coding with ```.get()``` functions and the sorts alike. We're trying to make the interace as user-friendly as possible for anyone.

### Features and their systems

We're experimenting with a few systems in order to detect false words right now. One of them is PyEnchant's [brilliant dictionary](https://pypi.python.org/pypi/pyenchant/), which we use for detecting incorrect spelling, and suggestions with the helpful implementation of Python's Regular Expressions module, *re*, e.g.:

![Example of incorrect apostrophes](https://cdn.discordapp.com/attachments/355240067322740737/422320614234128396/unknown.png)

## Built With

* [Python 3.6](https://www.python.org/) - Language used
* [tkinter](https://wiki.python.org/moin/TkInter) - GUI module used
* [PyEnchant](https://pypi.python.org/pypi/pyenchant/) - Used for spellchecking
