import subprocess

def open_new_terminal():

    subprocess.run(["cmd", "/c", "start", "python", "main.py"])

if __name__ == "__main__":
    open_new_terminal()
