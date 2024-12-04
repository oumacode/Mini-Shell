# Mini Shell

A simple shell program written in Python that supports basic user, file, and process management commands. It simulates a Unix-like shell environment with commands for interacting with the system.

## Features

### User Management Commands
- **`whoami`**: Display the current user.
- **`list users`**: List all users on the system.

### File Management Commands
- **`cd <dir>`**: Change the current working directory to `<dir>`.
- **`ls`**: List files and directories in the current directory.
- **`read <file>`**: Display the contents of the file `<file>`.
- **`mkdir <dir>`**: Create a new directory named `<dir>`.
- **`rmdir <dir>`**: Remove the directory `<dir>`.
- **`mk <file>`**: Create an empty file named `<file>`.
- **`rm <file>`**: Remove the file `<file>`.

### Process Management Commands
- **`ps`**: List all running processes.
- **`start <cmd>`**: Start a new process with the command `<cmd>`.
- **`stop <pid>`**: Terminate a process with the given `<pid>`.

### System Information Commands
- **`systeminfo`**: Display system information (OS details, CPU usage, etc.).
- **`run <path>`**: Execute a script or executable located at `<path>`.
