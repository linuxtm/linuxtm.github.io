---
title: Script pentru modificarea datei fisierelor pe disk
author: linuxtm
layout: post
permalink: /script-modificare-data-fisiere/
categories:
  - Scripturi
tags:
  - comenzi linux
  - tutoriale linux
  - scripturi linux
  - script modificare data
  - script schimbare data in baza exif
  - script schimbare data poza pe disk
---


Scriptul se foloseste de exiftool ca sa extraga CreateDate din metadatele pozelor si seteaza acea data ca fiind ModifiedDate pe disk.

<pre>
#!/usr/bin/env python3
#Gets the CreateDate from EXIF data and sets the date as modified for the files inside a folder
#example usage
# ./set-modified-date.py folder/
#More at https://linuxtm.ro

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
</pre>


Scriptul de mai jos schimba data fisierelor dintr-un folder.


<pre>
#!/bin/bash

# usage example
# ./set-time.sh folder/  "2023-03-06 14:30:00"
#More at https://linuxtm.ro
  
# Check if at least two arguments are provided
if [ "$#" -lt 2 ]; then
    echo "Usage: $0 <folder> <date>"
    exit 1
fi

folder="$1"
specified_date="$2"

# Check if the folder exists
if [ -d "$folder" ]; then
    # Loop through each file in the folder
    for file in "$folder"/*; do
        # Check if the item is a file (not a directory)
        if [ -f "$file" ]; then
            # Set the creation and modification times of the file
            touch -d "$specified_date" "$file"
            echo "File $file created on disk with date $specified_date"
        fi
    done
else
    echo "Error: Folder not found - $folder"
fi
</pre>

