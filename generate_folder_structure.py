import os

# Folders to exclude
exclude_folders = {'venv', 'mariadb_scripts', 'apicore', 'api-mongo-test', 'static', 'migrations', '.git', '.idea',
                   '__pycache__'}


def print_directory_structure(root_folder, indent=0):
    if root_folder in exclude_folders:
        return

    for item in os.listdir(root_folder):
        item_path = os.path.join(root_folder, item)

        if os.path.isdir(item_path):
            if item not in exclude_folders:
                print('  ' * indent + f'- {item}')
                print_directory_structure(item_path, indent + 1)
        else:
            continue
            # If you want to print files as well, use the code below
            # print('  ' * indent + f'  - {item}')


root_folder_path = "C:\\Users\\P70074418\\PycharmProjects\\django_euf"
print_directory_structure(root_folder_path)
