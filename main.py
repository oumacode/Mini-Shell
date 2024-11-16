import os
import subprocess
import shell_functions

def load_shell():
    while True:
        current_path = os.getcwd()
        input_user = input(f"{current_path}> ")
        args = input_user.split()

        if input_user == "exit":
            print("Exiting mini-shell.")
            break

        elif input_user == "help":
            shell_functions.show_help()

    #gestion fichiers
        elif args[0] == "cd":
            shell_functions.cd(args)

        elif args[0] == "ls":
            shell_functions.ls(args)

        elif args[0] == "read":
            shell_functions.read(args)

        elif args[0] == "mkdir":
            shell_functions.mkdir(args)

        elif args[0] == "rmdir":
            shell_functions.rmdir(args)

        elif args[0] == "mk":
            shell_functions.mk(args)

        elif args[0] == "rm":
            shell_functions.rm(args)

    #gestion processus
        elif args == "ps":
            shell_functions.ps()
        
        elif args[0] == "launch":
            shell_functions.launch(args[1])
        
        elif args[0] == "stop":
            shell_functions.stop(args)
        
        else:
            print("Cette commande n'est pas reconnu.")

load_shell()

