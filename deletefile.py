import os
import glob

def program():
    files = (glob.glob("D:/Path/to/file/*.txt"))
    for file in files:
        print(f"Removed {file}")
        os.remove(file)

program()
