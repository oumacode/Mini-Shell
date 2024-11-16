import os
import subprocess
import shell_functions

def load_text_editor():
    while True:
        current_path = os.getcwd()
        input_user = input(f"{current_path}> ").strip()
        args = input_user.split()

        if input_user == "exit":
            print("Exiting mini-shell.")
            break

        elif input_user == "help":
            shell_functions.show_help()

    #gestion fichiers
        elif args[0] == "cd":
            shell_functions.cd(args)

        elif args[0] == "view":
            shell_functions.view(args)

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

        elif args[0] == "ps":
            shell_functions.ps()
        
        elif args[0] == "stop_process":
            shell_functions.stop_process(args)

        else:
            print("Cette commande n'est pas reconnu.")

load_text_editor()

