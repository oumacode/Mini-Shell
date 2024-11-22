import os
import signal
import subprocess

def show_help():
    print("\n\033[38;5;98mUser Management Commands:\033[0m")

    print("- whoami     : print the current user")
    print("- list users : list all users")

    print("\n\033[38;5;98mFile Management Commands:\033[0m")

    print("- cd <dir>   : Change the current directory to <dir>")
    print("- ls         : List files and directories in the current directory")
    print("- read <file>: Read the content of a file")
    print("- mkdir <dir>: Create a new directory <dir>")
    print("- rmdir <dir>: Remove directory <dir>")
    print("- mk <file>  : Create an empty file <file>")
    print("- rm <file>  : Remove a file <file>")

    print("\n\033[38;5;98mProcess Management Commands:\033[0m")
    
    print("- ps         : List all running processes")
    print("- launch <cmd>: Launch a process <cmd>")
    print("- stop <pid> : Terminate a process by its <pid>")
    
# User Management
def whoami():
    print(os.getlogin())

def list_users():
    try:
        result = subprocess.run(['net', 'user'], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving users: {e}")
    except Exception as e:
        print(f"Unknown error: {e}")
        
# File Management
def cd(args):
    try:
        os.chdir(args[1]) 
    except IndexError:
        print("cd: missing argument")
    except FileNotFoundError:
        print("No such file or directory.")

def ls(args):
    try:
        if len(args) > 1:
            path = args[1]
        else:
            path = '.'
        entries = os.listdir(path)
        print("\n".join(entries))
    except FileNotFoundError:
        print("No such file or directory")

def read(args):
    try:
        with open(args[1], 'r') as file:
            print(file.read())
    except IndexError:
        print("read: missing argument.")
    except FileNotFoundError:
        print("No such file")

def mkdir(args):
    try:
        os.mkdir(args[1])  
        print("Directory is created")
    except IndexError:
        print("mkdir: missing argument")
    except FileExistsError:
        print("Directory already exists.")

def rmdir(args):
    try:
        os.removedirs(args[1]) 
        print("Directory is removed")
    except IndexError:
        print("rmdir: missing argument")
    except FileNotFoundError:
        print("Directory does not exist.")  

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

def rm(args):
    try:
        os.remove(args[1]) 
        print("File is removed")
    except IndexError:
        print("rm: missing argument")
    except FileExistsError:
        print("Directory does not exist.") 

# Process Management 
def ps():
    os.system("tasklist")

def launch(args):
    try:
        process = subprocess.Popen(args, shell=True)
        print(f"Process '{args}' started with PID {process.pid}")
        return process.pid
    except Exception as e:
        print(f"Error launching process: {e}")

def stop(args):
    try:
        pid = int(args[1])
        os.kill(pid, signal.SIGTERM)
        print(f"Process {pid} successfully terminated.")
    except ProcessLookupError:
        print(f"Process {pid} does not exist.")
    except PermissionError:
        print(f"Permission denied to kill process {pid}.")
    except Exception as e:
        print(f"Unknown error: {e}")

