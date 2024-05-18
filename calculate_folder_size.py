import os


def get_folder_size(f_path):
    total_size = 0
    for path, dirs, files in os.walk(f_path):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)
    # Convert to GB
    return round(total_size / (1024**3), 2)


def path_size(dir_path):
    folder_sizes = {}
    for folder_name in os.listdir(dir_path):
        folder_path = os.path.join(dir_path, folder_name)
        if os.path.isdir(folder_path):
            folder_sizes[folder_name] = get_folder_size(folder_path)

    # Order the dict in desc order
    folder_sizes_sorted = dict(sorted(folder_sizes.items(), key=lambda item: item[1], reverse=True))

    # Print the list
    for folder_name, folder_size in folder_sizes_sorted.items():
        print(f"{folder_name}: {folder_size} GB")


# example use
path_size(r'C:\Users')