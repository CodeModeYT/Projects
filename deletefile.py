import os
import glob
import sys

def count_txt_files(dir_path):
    return len([f for f in os.listdir(dir_path) if f.endswith('.txt')])

def program():
    files = (glob.glob("D:/Path/to/file/*.txt"))
    for file in files:
        print(f"Removed {file}")
        os.remove(file)

def start():
    dir_path = "D:/Path/to/file/"
    txt_file_count = count_txt_files(dir_path)
    check=input(f"Are you sure you want to continue and delete {txt_file_count} files? (y/n)")
    if check == "y":
        program()
    elif check == "n":
        print("Exiting...")
        sys.exit()
    else:
        print("This is not a valid option!")
        start()

print("Welcome to the mass file deleter.")
start()
