import os
import glob

amount = 10
name = "File"
filetype = "txt"

def program():
    for counter in range(amount):
        fp = open(f'{name}{counter}.{filetype}', 'w')
        fp.write(f'File number {counter}')
        fp.close()
        print(f"File number {counter} created")
        counter+=1

print("Welcome to the mass file creator.")
name=input("What name should the files have?")
filetype=input("What should the type of file be? (soon, currently only supporting txt)")
program()
