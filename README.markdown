README
======

A Dragon Appears (ADA) is a system for building open-source roleplaying games, published under GPLv3 (see `LICENSE.markdown` for more info). It is built for modularity, accessibility, and portability, so that it can tell any story, or involve any player, with as little work as possible. That said, ADA recognizes an important harsh reality: Rules restrict. Thus, no single game could tell every story. Each ADA module has a gameplay goal in mind, to which it aspires, whether that be realistic combat, sophisticated court drama, involved character development, or anything else a designer can conceive of.

## Defunct

This project is currently shelved. If you're looking for the game A Dragon Appears (rather than the system), go [here](https://github.com/garbados/games/blob/master/a_dragon_appears.md)

## Spec

ADA games are built of modules. Build files (denoted by ending with `_build.markdown`) will declare what modules the game consist of like this:

	Game Name
	=========
	Uses:
	-	Core Characters
	-	"Brightest Hour" Combat

What's happening here? The script `ada.py` uses this information to combine modules from the ADA library into one markdown file that constitutes the complete game, and all the rules it will need. This file, the game file, is denoted by ending with `_game.markdown`. The syntax for writing ADA build files goes like this:

	Game Name
	=========
	Uses:
	-	[module] [section]

A module is named after its first-level header. Sections are denoted by second-level headers. Keep it straight in your modules, and `ada.py` will do the rest. If a module or section name contains multiple words, encompass the name in quotes.

`ada.py` assumes everything in the library is written in markdown, so make sure your syntax is up to snuff! You can read all about markdown on [Daring Fireball](http://daringfireball.net/projects/markdown/).