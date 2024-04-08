
# File Organiser

File Organiser is a Python script designed to help you organize your files automatically based on their file extensions. This script scans a specified directory, identifies files based on their extensions, and moves them to corresponding folders.

## Features

- **Automatic Organization**: Automatically organizes files into folders based on their file extensions.
- **Extension Detection**: Identifies and categorizes files by their file extensions.
- **Customizable Categories**: Users can customize categories and corresponding file extensions according to their needs.
- **Duplicate Handling**: Handles duplicate files by renaming them with numerical suffixes.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone the repository to your local machine:

git clone https://github.com/your-username/file-organiser.git

css
Copy code

2. Navigate to the project directory:

cd file-organiser

markdown
Copy code

### Usage

1. Run the script by executing the `FileOrganiser.py` file:

python FileOrganiser.py

markdown
Copy code

2. Follow the on-screen instructions to specify the directory to be organized and choose from available options.

### Customization

You can customize the categories and corresponding file extensions by editing the `organize_files()` method in the `FileOrganiser` class within `FileOrganiser.py`.

## Example

Suppose you have a directory named `Downloads` containing various files:

Downloads/
├── document1.txt
├── music.mp3
├── image.jpg
└── archive.zip

sql
Copy code

Running the `FileOrganiser` script would result in the following directory structure:

Downloads/
├── Documents/
│ └── document1.txt
├── Music/
│ └── music.mp3
├── Images/
│ └── image.jpg
└── Archives/
└── archive.zip
