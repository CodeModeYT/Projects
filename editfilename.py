import os
import glob
import sys


def program():
    filetype =  input("What type of files do you want to rename? (file ending) ")
    name = input ("What should the name of the renamed files be? ")
    try:
        counter= int(input("At what value should the counter start?"))
        path = "D:/Projekte/Python/BulkRenamingUtility/"
        file_count = count_files(path, filetype)
        check=input(f"Are you sure you want to continue and rename {file_count} files? (y/n)")
        if check == "y":
            files = (glob.glob(f"{path}*.{filetype}"))
            for file in files:
                newname = f"{name}{counter}.{filetype}"
                print(f"Renamed {file} to {newname}")
                os.rename(file, newname)
                counter += 1
        elif check =="n":
            print("Exiting...")
            sys.exit()
        else:
            print("This is not a valid option!")
            print("Restarting...")
            program()
    except:
        print("Please enter a valid number!")
        program()

def count_files(path, filetype):
    return len([f for f in os.listdir(path) if f.endswith(f'.{filetype}')])

print ("Welcome to the mass-file editor!")
program()
