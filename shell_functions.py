import os
import signal
import subprocess

#Gestion utilisateurs
def whoami():
    print(os.getlogin())

def list_users():
    try:
        result = subprocess.run(['net', 'user'], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la récupération des utilisateurs : {e}")
    except Exception as e:
        print(f"Erreur inconnue : {e}")
        
def show_help():
    help_text = """
    Mini-Shell Help:

    - exit           : Exit the shell

    gestion fichiers:

    - cd <dir>       : Change the current directory to <dir>
    - ls             : List files and directories in the current directory
    - read           : Read the content of a file
    - mkdir <dir>    : Create a new directory <dir>
    - rmdir <dir>    : Remove directory
    - mk <dir>       : Create a file
    - rm <dir>       : Remove a file
    - ps             : Lister tous les processus 
    - launch         : launch un processus
    - stop           : Terminer l'excution un processus   

    """
    print(help_text)
 
#Gestion fichiers
def cd(args):
    try:
        os.chdir(args[1]) 
    except IndexError:
        print("cd: missing argument")
    except FileNotFoundError:
        print("no such file or directory.")

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
        print("Directory does not exists.")  

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
        print("mkdir: missing argument")
    except FileExistsError:
        print("Directory does not exists.") 

#Gestion processus 
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
        print(f"Processus {pid} terminé avec succès.")
    except ProcessLookupError:
        print(f"Le processus {pid} n'existe pas.")
    except PermissionError:
        print(f"Permission refusée pour tuer le processus {pid}.")
    except Exception as e:
        print(f"Erreur inconnue: {e}")





