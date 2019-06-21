#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os

mod_colonel = "modules/colonel/"
mod_loader  = "modules/loader/"

class Ferret(object):
	def __init__(self):
		parser = argparse.ArgumentParser(
			description = "Build and/or run Ferret and its modules.",
			usage       = """./ferret.py [-h] <command>

The available commands are:
    build   Build Ferret and its modules.
    run     Run Ferret without building.
"""
		)

		parser.add_argument(
			"command",
			help = "Subcommand to run."
		)

		args = parser.parse_args()

		if not hasattr(self, args.command):
			print("Unrecognized command.\n")
			parser.print_help()
			exit(1)
		getattr(self, args.command)()

	def build(self):
		loader_dir_out         = mod_loader + "out"
		loader_file_loader_lit = mod_loader + "loader.lit"

		if not os.path.isdir(loader_dir_out):
			os.mkdir(loader_dir_out)

		os.system("lit --out-dir " + loader_dir_out + " " + loader_file_loader_lit)
		exit(0)

	def run(self):
		exit(0)

if __name__ == "__main__":
	Ferret()
