import shutil
import os

source_dir = "directory/data/text"
dest_dir = "directory/data/photos"

# Make sure destination exists
os.makedirs(dest_dir, exist_ok=True)

# Files to move/copy
file_to_move = os.path.join(source_dir, "file1.txt")
file_to_copy = os.path.join(source_dir, "file2.txt")

# 1. Move file
if os.path.exists(file_to_move):
    shutil.move(file_to_move, dest_dir)
    print("file1.txt moved to processed folder.")
else:
    print("file1.txt not found.")

# 2. Copy file
if os.path.exists(file_to_copy):
    shutil.copy(file_to_copy, dest_dir)
    print("file2.txt copied to processed folder.")
else:
    print("file2.txt not found.")

# 3. Show final contents
print("\nContents of processed folder:")
for item in os.listdir(dest_dir):
    print(item)