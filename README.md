# Abstract Art Generator

Abstract Art Generator is made to do exactly what it sounds like: generate random images by scripting and automating Blender.

## Setting up the environment

Install Blender:
Download and install Blender from the official Blender website: https://www.blender.org/download/

Open Visual Studio Code (this guide only provides instructions for this IDE):
If you don't have Visual Studio Code installed, download and install it from the official website: https://code.visualstudio.com/

Install the "Blender Development" extension for Visual Studio Code. Open the Extensions view (Ctrl+Shift+X) and search for "Blender Development." Install the extension.

![This is what the extension should look like.](images/extension.png)

This is what the extension should look like.

Locate Blender Python Interpreter:
Find the path to Blender's Python interpreter. This is typically located within the Blender application package. For example: /Applications/Blender.app/Contents/Resources/3.10/python/bin/python3.10

Configure Python Interpreter in VSCode:
Open Visual Studio Code, go to the command palette (Ctrl+Shift+P) and run the command "Python: Select Interpreter." Choose the Blender Python interpreter path.

Restart VSCode:
Restart Visual Studio Code to apply the changes.

Next, add Blender to your PATH environment (optional). Below are general instructions for Windows, macOS, and Linux:

### Windows:

1. Find the path to your Blender installation. This is typically something like `C:\Program Files\Blender Foundation\Blender` or `C:\Program Files\Blender Foundation\Blender [version]`.

2. Copy the path to the Blender directory.

3. Right-click on "This PC" or "Computer" on your desktop or in File Explorer and select "Properties."

4. Click on "Advanced system settings" on the left.

5. Click the "Environment Variables" button.

6. In the "System variables" section, scroll down and find the "Path" variable. Select it and click "Edit."

7. Click "New" and paste the path to the Blender directory.

8. Click "OK" to close each window.

9. Open a new command prompt and type `blender` to verify that Blender launches.

### macOS and Linux:

1. Open a terminal.

2. Find the path to your Blender installation. This is typically something like `/Applications/Blender.app/Contents/MacOS` on macOS or `/opt/blender/blender [version]/` on Linux.

3. Open your shell profile file. This could be `~/.bashrc`, `~/.bash_profile`, `~/.zshrc`, or similar, depending on your shell. Use a text editor like `nano`, `vim`, or `gedit` to edit the file. For example:

   ```bash
   nano ~/.bashrc
   ```

4. Add the following line to the end of the file, replacing `/path/to/blender` with the actual path to your Blender installation:

   ```bash
   export PATH=$PATH:/path/to/blender
   ```

5. Save the file and exit the text editor.

6. In the terminal, type `source ~/.bashrc` (or the corresponding command for your shell) to apply the changes to the current session.

7. Open a new terminal and type `blender` to verify that Blender launches.

Keep in mind that the exact steps may vary depending on your system configuration and the specific shell you're using.

