import os
import zipfile
import datetime

# Define the path to your Django project folder
project_path = r'C:\Users\P70074418\PycharmProjects\django_euf'

# Define the path to the folder where you want to save the backup archive
backup_path = r'C:\Users\P70074418\PycharmProjects'

# Define the name of the backup archive
backup_filename = 'django_euf_complete_backup_' + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"))+'.zip'

# Define the name of the MySQL database
database_name = 'django_euf'

# Define the path to the mysqldump executable (assuming it's in your PATH)
mysqldump_path = 'mysqldump'
username = 'root'
password = 'asdasdasd'

# Ask the user whether they want to take backups of files and database
take_file_backup = input("Do you want to take a backup of your project files? (yes/no): ")
take_database_backup = input("Do you want to take a backup of your database? (yes/no): ")

# Create a compressed backup archive of your Django project folder
if take_file_backup.lower() == 'yes':
    backup_file = os.path.join(backup_path, backup_filename)
    with zipfile.ZipFile(backup_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(project_path):
            for file in files:
                zipf.write(os.path.join(root, file))
    print(f'Backup of project files saved at {backup_file}')
else:
    print('Project files backup skipped')

# Create a backup of your MySQL database
if take_database_backup.lower() == 'yes':
    database_file = os.path.join(backup_path,
                                 f'{database_name}_{str(datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"))}.sql')
    os.system(f'{mysqldump_path} --user={username} --password={password} --databases {database_name} > "{database_file}"')
    print(f'Backup of database saved at {database_file}')
else:
    print('Database backup skipped')
