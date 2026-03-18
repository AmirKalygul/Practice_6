import shutil
import os

source_file = "sample.txt"
backup_file = "backup_sample.txt"

# Copying and creating a backup file

if os.path.exists(source_file):
    shutil.copy(source_file, backup_file)
    print("File copied successfully.")
else:
    print("Source file does not exist.")

# Checking if the backup file was created successfully
if os.path.exists(backup_file):
    print("Backup file exists.")
else:
    print("Backup failed.")

# Checking if the user wants to delete the backup file

confirm1 = input("Do you want to delete the backup file? (yes/no): ").lower()

if confirm1 == "yes":
    if os.path.exists(backup_file):
        os.remove(backup_file)
        print("Backup file deleted.")
    else:
        print("File already deleted or not found.")
else:
    print("File was not deleted.")

# Checking if the user wants to delete the source file


confirm2 = input("Do you want to delete the source file? (yes/no): ").lower()

if confirm2 == "yes":
    if os.path.exists(source_file):
        os.remove(source_file)
        print("Source file deleted.")
    else:
        print("File already deleted or not found.")
else:
    print("File was not deleted.")