import os
import glob



def program():
    counter=1
    files = (glob.glob("D:/Projekte/Python/BulkRenamingUtility/*.txt"))
    for file in files:
        print(f"Renamed {file}")
        os.rename(file, f"Textfile-{counter}.txt")
        counter += 1

program()