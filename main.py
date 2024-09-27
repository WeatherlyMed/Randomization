import sys
import random
import os

# Usage: python main.py dim directory
if len(sys.argv) != 3:
    print("Usage: python main.py <dim> <directory>")
    exit(1)

try:
    dim = int(sys.argv[1])
except ValueError:
    print("Improper dimension; it must be an integer.")
    exit(1)

directory = sys.argv[2]

if not os.path.isdir(directory):
    print(f"The directory '{directory}' does not exist.")
    exit(1)

entries = os.listdir(directory)

for entry in entries:
    # Create the full path for the original file
    original_path = os.path.join(directory, entry)
    
    # Check if it's a file before renaming
    if os.path.isfile(original_path):
        i = random.randrange(dim)
        new_name = f"{i}_{entry}"
        new_path = os.path.join(directory, new_name)
        
        os.rename(original_path, new_path)
        print(f"Renamed '{entry}' to '{new_name}'")
    else:
        print(f"'{entry}' is not a file and will be skipped.")
