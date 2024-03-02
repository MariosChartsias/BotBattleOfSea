# from setuptools import setup, find_packages
# from setuptools.command.install import install as _install
# import shutil
# import os

# # Custom install command to copy files after installation
# class install(_install):
#     def run(self):
#         _install.run(self)
#         # Copy files from docs/appdata/project_files to localappdata
#         source_dir = "docs/appdata/BotBattleOfSea"
#         destination_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'BotBattleOfSea')
#         shutil.copytree(source_dir, destination_dir)

# # Read dependencies from requirements.txt
# with open('requirements.txt') as f:
#     required_packages = f.read().splitlines()

# setup(
#     name='BotBattleOfSea',
#     version='1.0.0',
#     packages=find_packages(),
#     install_requires=required_packages,
#     cmdclass={'install': install},
# )

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

