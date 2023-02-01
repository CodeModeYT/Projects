import os
import glob

def program():
    files = (glob.glob("D:/Projekte/Python/BulkRenamingUtility/*.txt"))
    for file in files:
        print(f"Removed {file}")
        os.remove(file)

program()
