
import os
def generate_file():

    cwd = os.getcwd
    print("this is the current working directory %s" %(cwd))
    for letter in range(65,92):
        file = chr(letter)+'.txt'

        with open(file,'w') as f1:
            f1.write(f"this is the fname {file}")

    print("files is created from a  to z")



generate_file()

