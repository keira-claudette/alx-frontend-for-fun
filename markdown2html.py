#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    if os.path.exists(sys.argv[1]) == False:
        print("Missing {}".format(sys.argv[1]))
        exit(1)
  
    else:
        print()
        exit(0)
