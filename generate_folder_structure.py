import os

# Folders to exclude
exclude_folders = {'venv', 'mariadb_scripts', 'apicore', 'api-mongo-test', 'static', 'migrations', '.git', '.idea',
                   '__pycache__'}


def print_directory_structure(root_folder, indent=0, output_file=None):
    if root_folder in exclude_folders:
        return

    for item in os.listdir(root_folder):
        item_path = os.path.join(root_folder, item)

        if os.path.isdir(item_path):
            if item not in exclude_folders:
                folder_name = f'- {item}\n'
                print('  ' * indent + folder_name.strip())

                if output_file is not None:
                    output_file.write('  ' * indent + folder_name)

                print_directory_structure(item_path, indent + 1, output_file)
        else:
            file_name = f'  - {item}\n'
            print('  ' * indent + file_name.strip())

            if output_file is not None:
                output_file.write('  ' * indent + file_name)


root_folder_path = "C:\\Users\\P70074418\\PycharmProjects\\django_euf"

output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                f'{os.path.basename(root_folder_path)}_folder_structure.txt')
with open(output_file_path, 'w') as output_file:
    print_directory_structure(root_folder_path, output_file=output_file)

print(f'\nResults saved to: {output_file_path}')
