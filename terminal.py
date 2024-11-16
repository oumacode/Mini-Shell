import subprocess

def open_new_terminal():
    # Provide the full path to the script
    script_path = "C:\\Users\\G7\\OneDrive\\Documents\\Projects\\OS_project\\main.py"
    subprocess.run(["wt", "new-tab", "python", script_path])

if __name__ == "__main__":
    open_new_terminal()
