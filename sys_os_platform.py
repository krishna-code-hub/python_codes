

import os

# List files in the current directory
print(os.listdir('.'))

# Get current working directory
print(os.getcwd())

# Check if a file exists
print(os.path.exists('somefile.txt'))


import sys

# Print command line arguments
print(sys.argv)


import platform

# Print system/OS name
print(platform.system())

# Detailed platform information
print(platform.platform())

# Python compiler information
print(platform.python_compiler())


# Exit the script with a status code
sys.exit(0)