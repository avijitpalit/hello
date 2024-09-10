import os

# Specify the directory path
directory_path = 'C:/Users/Administrator/Pictures/Screenshots'

# Get all files in the directory
files_list = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

# Optionally, filter to only include files (exclude directories)
#files_list = [f for f in files_list if os.path.isfile(os.path.join(directory_path, f))]

print(files_list)