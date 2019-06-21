#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

class Ferret(object):
	def __init__(self):
		parser = argparse.ArgumentParser(
			description="Build and/or run Ferret and its modules.",
			usage="""./ferret.py [-h] <command>

The available commands are:
    build   Build Ferret and its modules.
    run     Run Ferret without building.
"""
		)

		parser.add_argument(
			"command",
			help="Subcommand to run."
		)

		args = parser.parse_args()

		if not hasattr(self, args.command):
			print("Unrecognized command.\n")
			parser.print_help()
			exit(1)
		getattr(self, args.command)()

	def build(self):
		exit(0)

	def run(self):
		exit(0)

if __name__ == "__main__":
	Ferret()
