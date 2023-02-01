import os
import glob

def program():
    for counter in range(10):
        fp = open(f'Testfile{counter}.txt', 'w')
        fp.write(f'File number {counter}')
        fp.close()
        print(f"File number {counter} created")
        counter+=1

program()