#!/usr/bin/python3
""" This module translates markdown to html."""
if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)
    if os.path.exists(sys.argv[1]) == False:
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        exit(1)
  
    else:
        print()
        exit(0)
