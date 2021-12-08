#!/usr/bin/python3
"""This script checks if file exists."""

import sys
import os

if len(sys.argv) != 3:
  print("Usage: ./markdown2html.py README.md README.html")

if os.path.exists("file.txt") == False:
  print("Missing {}".format(sys.argv[1]))
  exit (1)
  
else:
  print()
  exit (0)