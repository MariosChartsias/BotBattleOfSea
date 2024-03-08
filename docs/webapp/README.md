# WebBattleOfSea

## Setting Up Virtual Environment and Installing Packages

This guide will walk you through setting up a virtual environment using the Visual Studio Code (VSCode) terminal with administrative permissions and then installing packages using `setup.py` in Python.

### Creating Virtual Environment

1. Open Visual Studio Code (VSCode).

2. Open a new terminal by selecting Terminal > New Terminal from the VSCode menu.

3. In the terminal, navigate to your project directory (you probably have not to do that if you are already in this path):
   ```bash
   cd path/to/your/project.

4. To create a virtual environment with administrative permissions, use the following commands:

   - **Windows**:
      ```bash
      cd src/webapp
      ``` 

      ```bash
      python -m venv venv --prompt venv
      ```

   - **macOS/Linux**:
     ```bash
     sudo python3 -m venv venv --prompt venv
     ```

4. Activate the virtual environment on:

   - **Windows**:
   ```bash
     Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
     ```
     ```bash
     .\venv\Scripts\activate.ps1
     ```

   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

5. Install the packages using setup.py by running the following command:
     ```bash
     python setup.py
     ```