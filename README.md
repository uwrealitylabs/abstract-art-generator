# Abstract Art Generator

The Abstract Art Generator does exactly what it sounds like - it's designed to generate random abstract images through a Blender script. Assets in the /assets/ folder are imported into Blender, given random values for position, rotation and material, and then are rendered at a random camera position and focal length.

Here's what one render might look like:

![Example Abstract Art Generated Render](images/example.png)

## Setting up the environment

Clone the repository.

### Install Blender

Download and install Blender from the official Blender website: [Blender Download](https://www.blender.org/download/)

We used the Blender 3.6 LTS version. In the render.py file, the example directories for "blender_python_path" MUST be changed if you are using a different version or have installed in a different directory.

### Open Visual Studio Code

If you don't have Visual Studio Code installed, download and install it from the official website: [Visual Studio Code Download](https://code.visualstudio.com/)

Install the "Blender Development" extension for Visual Studio Code. Open the Extensions view (Ctrl+Shift+X) and search for "Blender Development." Install the extension.

![Blender Development Extension](images/extension.png)

### Locate Blender Python Interpreter

Find the path to Blender's Python interpreter, typically located within the Blender application package (e.g. on macOS, /Applications/Blender.app/Contents/Resources/3.10/python/bin/python3.10).

### Configure Python Interpreter in Visual Studio Code

Open Visual Studio Code, go to the command palette (Ctrl+Shift+P), and run the command "Python: Select Interpreter." Choose the Blender Python interpreter path.

### Restart Visual Studio Code

Restart Visual Studio Code to apply the changes.

### Add Blender to your PATH environment

#### Windows

1. Find the path to your Blender installation (usually `C:\Program Files\Blender Foundation\Blender 3.6`).

2. Copy the path to the Blender directory. Don't copy the executable path, just the file directory.

3. Hit the Windows key and search for 'env'. You should see "Edit the system environment variables".

4. Click or select it by pressing Enter. This should open the Advanced tab of System Properties.

5. Click the "Environment Variables..." button in the lower right.

6. In the "System variables" section, scroll down and find the "Path" variable. Select it and click "Edit."

7. Click "New" and paste the path to the Blender directory.

8. Click "OK" to close each window.

9. Open a new command prompt and type `blender` to verify that Blender launches.

#### macOS and Linux

1. Open a terminal.

2. Find the path to your Blender installation (e.g., `/Applications/Blender.app/Contents/MacOS` on macOS or `/opt/blender/blender [version]/` on Linux).

3. Open your shell profile file (`~/.bashrc`, `~/.bash_profile`, `~/.zshrc`, etc.) using a text editor like `nano`, `vim`, or `gedit`.

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

## Run the script

You should now be able to run the python script using `blender -b art.blend -P scripts/render.py`. This command should be run inside the cloned repository folder. Alternatively, if the steps above did not work for you, you can run the script inside of Blender's built-in script editor.
