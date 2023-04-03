import sys

amount = 0
name = "File"
filetype = "txt"

def start():
    name=input("What name should the files have? ")
    filetype=input("What should the type of file be? ")
    try:
        amount=int(input("How many files should be created? "))
        check=input(f"""Are you sure you want to create {amount} files with the name "{name}" of with the filetype (ending) {filetype}? (y/n)""")
        if check == "y":
            if filetype == "txt":
                for counter in range(amount):
                    fp = open(f'{name}{counter}.{filetype}', 'w')
                    fp.write(f'File number {counter}')
                    fp.close()
                    print(f"File number {counter} created")
                    counter+=1
            else:
                for counter in range(amount):
                    fp = open(f'{name}{counter}.{filetype}', 'w')
                    fp.close()
                    print(f"File number {counter} created")
                    counter+=1
        elif check == "n":
            print("Exiting...")
            sys.exit()
        else:
            print("Not a valid choice. Please try again:")
            start()
    except:
        print("Please enter a valid number!")
        start()

print("Welcome to the mass file creator.")
start()
