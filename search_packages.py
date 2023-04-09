import os

# Get the path of the virtual environment
venv_path = os.path.join(os.getcwd(), 'venv')

# Get a list of installed packages in the virtual environment
installed_packages = os.popen(f'{venv_path}\\Scripts\\pip freeze').read().splitlines()

# Get a list of required packages in the requirements.txt file
with open('requirements.txt', 'r') as f:
    required_packages = f.read().splitlines()

# Print the list of installed packages and whether they are required
for package in installed_packages:
    package_name = package.split('==')[0]
    if package_name in required_packages:
        pass
        # print(f'{package_name}: Required')
    else:
        print(f'{package_name}: Not required')
