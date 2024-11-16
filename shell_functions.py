import os
import signal
import subprocess

def show_help():
    help_text = """
    Mini-Shell Help:

    - exit           : Exit the shell

    gestion fichiers:

    - cd <dir>       : Change the current directory to <dir>
    - view           : List files and directories in the current directory
    - read           : Read the content of a file
    - mkdir <dir>    : Create a new directory <dir>
    - rmdir <dir>    : Remove directory
    - mk <dir>       : Create a file
    - rm <dir>       : Remove a file
    - ps             : Lister tous les processus    

    """
    print(help_text)

# Command: cd (change directory)
def cd(args):
    try:
        os.chdir(args[1]) 
    except IndexError:
        print("cd: missing argument")
    except FileNotFoundError:
        print("no such file or directory.")

# Command: view (List files and directories in the current directory)
def view(args):
    try:
        if len(args) > 1:
            path = args[1]
        else:
            path = '.'
        entries = os.listdir(path)
        print("\n".join(entries))
    except FileNotFoundError:
        print("No such file or directory")

# Command: read (Read the content of a file)
def read(args):
    try:
        with open(args[1], 'r') as file:
            print(file.read())
    except IndexError:
        print("read: missing argument.")
    except FileNotFoundError:
        print("No such file")

# Command: mkdir (make directory)
def mkdir(args):
    try:
        os.mkdir(args[1])  
        print("Directory is created")
    except IndexError:
        print("mkdir: missing argument")
    except FileExistsError:
        print("Directory already exists.")

# Command: rmdir (remove directory)
def rmdir(args):
    try:
        os.removedirs(args[1]) 
        print("Directory is removed")
    except IndexError:
        print("rmdir: missing argument")
    except FileNotFoundError:
        print("Directory does not exists.")  

# Command: mk (create a file)
def mk(args):
    if len(args) < 2:  
        print("mk: missing argument")
        return
    try:
        with open(args[1], 'w') as file:
            pass 
        print(f"File '{args[1]}' is created.")
    except Exception as e: 
        print(f"Error creating file: {e}")

# Command: rm (remove file)
def rm(args):
    try:
        os.remove(args[1]) 
        print("File is removed")
    except IndexError:
        print("mkdir: missing argument")
    except FileExistsError:
        print("Directory does not exists.") 


#Gestion processus 

#Command: ps (lister tous les processus)
def ps():
    os.system("tasklist")





