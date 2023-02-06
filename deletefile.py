import os
import glob
import sys

def start():
    filetype = input("Please input the filetype (without the dot): ")
    dir_path = "D:Path/to/file/"
    file_count = count_txt_files(dir_path, filetype)
    check=input(f"Are you sure you want to continue and delete {file_count} files? (y/n)")
    if check == "y":
        files = (glob.glob(f"D:Path/to/file/*.{filetype}"))
        for file in files:
            os.remove(file)
            print(f"Removed {file}")
    elif check == "n":
        print("Exiting...")
        sys.exit()
    else:
        print("This is not a valid option!")
        start()

def count_txt_files(dir_path, filetype):
    return len([f for f in os.listdir(dir_path) if f.endswith(f'.{filetype}')])



print("Welcome to the mass file deleter.")
start()
