
import subprocess
import sys

# Read dependencies from requirements.txt
with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

# Install dependencies using pip
subprocess.call([sys.executable, '-m', 'pip', 'install'] + required_packages)

