# Importing necessary libraries
import os  # Operating System module for interacting with the file system
import shutil  # Shell Utilities module for high-level file operations
import time  # Module for time-related functions
from watchdog.events import FileSystemEventHandler  # Importing FileSystemEventHandler for handling file system events


# Defining the FileOrganiser class inheriting from FileSystemEventHandler
class FileOrganiser(FileSystemEventHandler):

    # Initializing the class with the folder to track
    def __init__(self, folder_to_track):
        super().__init__()  # Making this class a super class
        self.folder_to_track = folder_to_track  # Setting the directory to track

    # Method to get unique file extensions in the folder
    def get_extension(self):
        unique_ex = []
        for file in os.listdir(self.folder_to_track):  # Looping through all the files in the directory folder to track
            base, ex = os.path.splitext(file)  # Splitting the file name and extension
            ex = ex[1:]  # Getting the extension name and removing the dot before that
            if len(ex) <= 4 and len(
                    ex) > 0 and ex.isnumeric() == False:  # Filtering extensions of less than 4 characters and without numbers
                if ex not in unique_ex:
                    unique_ex.append(ex)
            else:
                continue
        print(unique_ex)

    # Method to get all files in the current directory
    def get_files(self):
        for file in os.listdir(self.folder_to_track):
            print(file)

    # Method to get all unique extensions and all files in the folder
    def get_extensions_and_files(self):
        extensions = set()
        files = []

        for root, dirs, filenames in os.walk(self.folder_to_track):  # Walking through directory tree
            for filename in filenames:
                # Get file extension
                _, ext = os.path.splitext(filename)
                ext = ext[1:]  # Remove the dot from the extension
                extensions.add(ext)  # Adding the extensions to the extensions list

                # Get absolute path of the file
                file_path = os.path.join(root, filename)
                files.append(file_path)

        print(f"Unique extensions: \n{extensions}")

        print("\nAll files:")
        for file in files:
            print(file)

    # Method to organize files into respective folders based on file extension
    def organize_files(self):
        for file in os.listdir(self.folder_to_track):
            base, ex = os.path.splitext(file)
            src = os.path.join(self.folder_to_track, file)

            # Dictionary of destination directories based on file types
            destination_dirs = {
                'Documents': ['.txt', '.doc', '.docx', '.pdf', '.xls', '.xlsx'],
                'Music': ['.mp3', '.wav', '.ogg', '.flac'],
                'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
                'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
                'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
                'Programs': ['.exe', '.msi'],
                'Presentations': ['.ppt', '.pptx'],
                'Spreadsheets': ['.csv'],
                'Code': ['.py', '.java', '.cpp', '.html', '.css', '.js'],
                'Text': ['.rtf'],
                'Ebooks': ['.epub', '.mobi'],
                'Fonts': ['.ttf', '.otf'],
                'Configurations': ['.ini', '.cfg'],
                'Data': ['.dat', '.json', '.xml']
            }

            # Find the destination directory for the file
            destination_dir = None
            for category, extensions in destination_dirs.items():
                if ex in extensions:
                    destination_dir = category
                    break

            # For handling duplicate files
            try:
                if os.path.isfile(src):
                    ex = ex[1:]
                    i = 1
                    while True:
                        new_file_name = f"{base}_{i}.{ex}"
                        new_file_path = os.path.join(self.folder_to_track, new_file_name)

                        if not os.path.exists(new_file_path):
                            break
                        i += 1

                # Move the files if destination directory found
                if destination_dir:
                    destination_folder = os.path.join(self.folder_to_track, destination_dir)  # Destination folder
                    if not os.path.exists(destination_folder):  # If the directory doesn't exist, create one
                        os.makedirs(destination_folder)
                    shutil.move(src, os.path.join(destination_folder,
                                                  file))  # Moving the file to its respective category folder
                    print(f'File {file} moved to {destination_folder} folder')

                else:
                    print(f'No category found for this file {file}')

            except PermissionError as e:
                print(f'PermissionError: {e}. File {file} cannot be moved.')


# Main program
if __name__ == '__main__':
    # Prompting user for their name
    name = input('Enter your name : ')
    print(f'Welcome {name}\n')
    # Prompting user to enter the directory to track

    folder_to_track = input('\nPlease enter the directory to track : ')
    organiser = FileOrganiser(folder_to_track)

    # Menu for user interaction
    while True:
        try:
            choice = int(input(
                '\nPlease select from the following options\n(1) - Unique extension in the directory\n(2) - Display all the files and folders in the current directory\n(3) - Move files to their extension folder (Organise)\n(4) - Displays all files, folders and extensions in root and sub directory\n(5) - Quit\n\n'))
            if choice == 1:
                organiser.get_extension()
            elif choice == 2:
                organiser.get_files()
            elif choice == 3:
                organiser.organize_files()
            elif choice == 4:
                organiser.get_extensions_and_files()
            elif choice == 5:
                print('Goodbye')
                time.sleep(3)
                quit()
            else:
                print('Please enter a valid input\n\n')

        except ValueError:
            print('Please enter a valid input\n\n')
