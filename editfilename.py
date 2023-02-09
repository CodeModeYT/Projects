import os
import glob
import sys


def program():
    counter=1
    files = (glob.glob("D:/Path/to/file/*.txt"))
    for file in files:
        print(f"Renamed {file}")
        os.rename(file, f"Textfile-{counter}.txt")
        counter += 1

program()
