# WinuxShell

**WinuxShell** is a project that brings popular Linux commands to the Windows environment, enabling users to interact with their system in a Linux-like manner. The commands implemented in this project aim to replicate the behavior of Linux tools such as `cat`, `ls`, `touch`, `wget`, and more, making Windows more developer-friendly!

## Features

- **`cat`**: View the contents of a file, just like on Linux.
- **`ls`**: List files and directories in the current directory.
- **`touch`**: Create an empty file or update the timestamp of an existing file.
- **`wget`**: Download files from a URL, just like the Linux `wget` command.
- **`jav`**: A simplified way to run Java files using `jav <filename-with-extension>`.
- **`github`**: Easily commit and push code to GitHub. Usage: `github "<commit-message>" <remote-url-name> <branch-name>`.
- **`custom`**: Customize commands and activate a virtual environment by specifying `custom <name-of-environment>`.

## Commands Overview

### `cat`
Displays the contents of a file.

**Usage**:
```bash
cat <filename>
```

### `ls`
Lists the files and directories in the current directory.

**Usage**:
```bash
ls
```

### `touch`
Creates a new empty file or updates the timestamp of an existing file.

**Usage**:
```bash
touch <filename>
```

### `wget`
Downloads files from a given URL.

**Usage**:
```bash
wget <url>
```

### `jav`
Compiles and runs Java files directly.

**Usage**:
```bash
jav <filename-with-extension>
```

### `github`
Commits and pushes code to GitHub with ease.

**Usage**:
```bash
github "<commit-message>" <remote-url-name> <branch-name>
```

### `custom`
Beautifies your Windows command shell (CMD) and starts any specified virtual environment.

**Usage**:
```bash
custom <name-of-environment>
```

## Installation

To use **WinuxShell**, follow these steps:

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Add the project folder to your system’s `PATH`:

    - **On Windows**:
      1. Right-click on **This PC** and select **Properties**.
      2. Click on **Advanced system settings** and then **Environment Variables**.
      3. Under **System variables**, find the `Path` variable and select it. Click **Edit**.
      4. In the **Edit Environment Variable** dialog, click **New** and add the path to the folder containing your commands (e.g., `C:\path\to\WinuxShell`).
      5. Click **OK** and close the dialogs.

    - **On Linux/macOS** (if applicable):
      Add the following line to your `.bashrc` or `.zshrc` file:
      ```bash
      export PATH="$PATH:/path/to/WinuxShell"
      ```

3. Restart your terminal for the changes to take effect.

## Contributing

Contributions are welcome! If you have ideas to enhance or extend the functionality, feel free to submit a pull request.
