import shutil
import os
import subprocess
import sys

# Function to copy files after installation
def copy_files():
    # Copy files from docs/appdata/project_files to localappdata
    source_dir = "docs/appdata/BotBattleOfSea"
    destination_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'BotBattleOfSea')
    shutil.copytree(source_dir, destination_dir)

# Read dependencies from requirements.txt
with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

# Install dependencies using pip
subprocess.call([sys.executable, '-m', 'pip', 'install'] + required_packages)

# Copy files after installation
copy_files()

