import os
import shutil
import datetime

def backup_directory(source, destination):
    date = datetime.datetime.now().strftime("%Y%m%d")
    backup_folder = os.path.join(destination, f"backup_{date}")
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    
    try:
        shutil.copytree(source, backup_folder)
        print(f"Backup of {source} completed successfully.")
    except Exception as e:
        print(f"Error during backup: {e}")

if __name__ == "__main__":
    SOURCE_DIR = "/path/to/source/directory"
    DESTINATION_DIR = "/path/to/backup/directory"
    backup_directory(SOURCE_DIR, DESTINATION_DIR)
