import os
import shell_functions
import time

print("\033[38;2;102;204;204mWelcome to Your Mini Shell!\033[0m")

def welcome_screen():
    print("\nLet's get started! Please select an option below:")
    print("\033[38;2;241;196;15m1. Get Help\033[0m")
    print("\033[38;2;241;196;15m2. Start Shell\033[0m")
    print("\033[38;2;241;196;15m3. Exit Shell\033[0m")
    input_user = input("Please enter the number corresponding to your choice: ")

    if input_user == "1":
        shell_functions.show_help()
        welcome_screen()
    elif input_user == "2":
        load_shell()
    elif input_user == "3":
        print("\033[1;32mExiting Shell. Goodbye!\033[0m") 
        time.sleep(1) 
        exit()
    else:
        print("\033[38;5;124mInvalid choice, please try again.\033[0m")
        welcome_screen()

def load_shell():
    while True:
        input_user = input(f'\033[38;2;123;237;159m{os.getcwd()}>\033[0m')


        args = input_user.split()

        # User Management
        if input_user == "whoami":
            shell_functions.whoami()

        elif input_user == "list users":
            shell_functions.list_users()

        elif input_user == "exit":
            print("\033[1;32mExiting Shell. Goodbye!\033[0m") 
            time.sleep(1)
            break

        elif input_user == "help":
            shell_functions.show_help()

        # File Management
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

        # Process Management
        elif input_user == "ps":
            shell_functions.ps()

        elif args[0] == "launch":
            shell_functions.launch(args[1])

        elif args[0] == "stop":
            shell_functions.stop(args)
            
        elif input_user == "systeminfo":
            shell_functions.systeminfo()
        
        elif args[0] == "run":
            shell_functions.run_script(args)
        
        else:
            print("\033[38;5;124mCommand not recognized. Try 'help' for a list of commands.\033[0m")

welcome_screen()
