import os
from shutil import move

def sort_images_by_extension(download_dir):
    if not os.path.exists(download_dir):
        print(f"Directory {download_dir} does not exist.")
        return

    # List all files in the download directory
    files = os.listdir(download_dir)

    for file in files:
        # Check if it's an image file based on extension
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp', '.pdf')):
            file_path = os.path.join(download_dir, file)
            
            # Extract the file extension and create a folder name
            extension = file.split('.')[-1].upper()
            folder_name = f"{extension} Folder"
            folder_path = os.path.join(download_dir, folder_name)

            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Move the file to the appropriate folder
            move(file_path, os.path.join(folder_path, file))
            print(f"Moved {file} to {folder_path}")

# Replace this with your actual Downloads directory path
download_directory = "/Users/andylee/Downloads"

sort_images_by_extension(download_directory)