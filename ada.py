"""
Script that combines modules into whole games.
"""
import sys, os, re

class Parser:
	"""
	1.) Comprehend the library, storing it in a dictionary.
	2.) Parse the given build file.
	3.) Combine the selected sections from the selected modules into a game file.
	"""
	def __init__(build_file):
		"""
		build_file is a filename, of the form "[a-zA-Z]_build.markdown"
		self.build_file is that file's contents.
		self.cwd is the current working directory, which we'll parse for modules.
		self.game_file is the filename of the file to which we'll write 
		"""
		# quit if the name isn't formatted properly
		if not re.match(r'^.+_build\.markdown$', build_file):
			raise ValueError("Filename %s not formatted properly. Expected file to end with '_build.markdown'" % build_file)

		# TODO validate that the build_file contains data
		with open(build_file,'r') as f:
			self.build_file = f.readlines()

		# TODO allow script to be run outside of the library's directory.
		self.cwd = os.getcwd()

		# TODO prompt for confirmation if file has data already, then clean game_file before continuing
		self.game_file = "%s_game.markdown" % build_file.partition('_build.markdown')[0]

	def parse_build_file():
		"""
		1.) Get each line of the build file starting with "-"
		2.) Break it into "- [module name] [section name]"
		3.) Add it to a dict of dicts, in the form of dict[module][section]
		4.) Return the dict
		"""
		pattern = re.compile(r'-\s+"?(?P<module>[a-zA-Z0-9 ]+)"? "?(?P<section>[a-zA-Z0-9 ]+)"?')
		game_modules = {}
		for line in self.build_file:
			match = pattern.match(line)
			if match:
				if not match['module'] in game_modules:
					game_modules[match['module']] = {}
				game_modules[match['module']][match['section']] = ''
		return game_modules

	def scour_library(sought_modules):
		"""
		1.) Recursively get all filenames ending in ".markdown" (but not build or game files) in the current directory and all sub-directories.
		2.) Parse for modules; if a found module is in sought_modules, parse it for sections; if a found section is in sought_modules[module], add it
		3.) Return modified sought_modules
		"""

	def construct_game(self):
		"""
		1.) Parse build file into dict of module and section names.
		2.) Find markdown files recursively through all folders within the current directory.
		3.) Whenever a markdown file is found, 
		"""
		game_modules = self.parse_build_file()
