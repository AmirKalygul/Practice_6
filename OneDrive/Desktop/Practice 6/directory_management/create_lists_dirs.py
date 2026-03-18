import os
import glob

# 1. Create nested directories
os.makedirs("directory/data/text", exist_ok=True)
os.makedirs("directory/data/photos", exist_ok=True)

print("Nested directories created.\n")

# 2. Create some sample files for testing
with open("directory/data/text/file1.txt", "w") as f:
    f.write("Sample text file 1")

with open("directory/data/text/file2.txt", "w") as f:
    f.write("Sample text file 2")

with open("directory/data/text/file3.csv", "w") as f:
    f.write("Sample csv file")

print("Sample files created.\n")

# 3. List files and folders
print("Contents of 'directory/data/text':")
items = os.listdir("directory/data/text")
for item in items:
    print(item)

# 4. Find files by extension (.txt)
txt_files = glob.glob("directory/data/text/*.txt")

print("\nText files found:")
for file in txt_files:
    print(file)