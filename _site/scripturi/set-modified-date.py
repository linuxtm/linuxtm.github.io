#!/usr/bin/env python3
#Gets the CreateDate from EXIF data and sets the date as modified for the files inside a folder
#example usage
# ./set-modified-date.py folder/

import os
import subprocess
from datetime import datetime

def get_creation_date(file_path):
    # Use exiftool to get creation date
    command = ['exiftool', '-CreateDate', '-d', '%Y:%m:%d %H:%M:%S', '-s3', file_path]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()

    if process.returncode == 0:
        creation_date_str = output.strip()
        if creation_date_str:
            try:
                creation_date = datetime.strptime(creation_date_str, '%Y:%m:%d %H:%M:%S')
                return creation_date.timestamp()
            except ValueError as e:
                print(f"Error converting creation date for {file_path}: {e}")
        else:
            print(f"Creation date not found for {file_path}")
    else:
        print(f"Error extracting creation date for {file_path}: {error}")

    return None

def set_modified_date(file_path, modified_time):
    # Set the modification time of the file
    os.utime(file_path, times=(modified_time, modified_time))

def main(folder_path):
    # Iterate through all files in the specified folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Get creation date of the file using exiftool
        creation_date = get_creation_date(file_path)

        if creation_date is not None:
            # Set the creation date as the modified date
            set_modified_date(file_path, creation_date)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/your/folder")
        sys.exit(1)

    folder_path = sys.argv[1]
    main(folder_path)
