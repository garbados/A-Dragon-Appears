README
======
A Dragon Appears (ADA) is an open-source roleplaying game. It is built for modularity, accessibility, and portability, so that it can tell any story, or involve any player, with as little work as possible. That said, ADA recognizes an important harsh reality: Rules restrict. Thus, no single game could tell every story. Each ADA module has a gameplay goal in mind, to which it aspires, whether that be realistic combat, sophisticated court drama, involved character development, or anything else a designer can conceive of.

ADA games are built of modules. Games will declare them at the outset like this:

	Game Name
	=========
	Uses:
	-	Core Characters
	-	Brightest_Hour Combat

What's happening here? The script `ada.py` uses this information to combine modules from the ADA library into one markdown file that constitutes the complete game, and all the rules it will need. The syntax goes like this:

	Game Name
	=========
	Uses:
	-	[module] [section]

A module is named after its first-level header. Sections are denoted by second-level headers. Keep it straight in your modules, and `ada.py` will do the rest.