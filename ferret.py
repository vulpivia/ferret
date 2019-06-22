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
		loader_dir_bin         = mod_loader + "bin/"
		loader_dir_out         = mod_loader + "out/"
		loader_file_loader_asm = loader_dir_out + "loader.asm"
		loader_file_loader_ld  = loader_dir_out + "loader.ld"
		loader_file_loader_lit = mod_loader + "loader.lit"
		loader_file_loader_o   = loader_dir_out + "loader.o"

		if not os.path.isdir(loader_dir_out):
			os.mkdir(loader_dir_out)
		if not os.path.isdir(loader_dir_bin):
			os.mkdir(loader_dir_bin)

		# Compile Literate to HTML + source code
		os.system("lit --out-dir " + loader_dir_out + " " + loader_file_loader_lit)
		# Assemble source code
		os.system("nasm -felf32 " + loader_file_loader_asm + " -o " + loader_file_loader_o)
		# Link to binary
		os.system("ld -m elf_i386 --script=" + loader_file_loader_ld + " -o " + loader_dir_bin + "loader " + loader_file_loader_o)
		exit(0)

	def run(self):
		# TODO: loader.o is object file, needs ld
		os.system("qemu-system-i386 -kernel modules/loader/bin/loader")
		exit(0)

if __name__ == "__main__":
	Ferret()
