# django_euf

## Requirements
1. Python 3.9+
2. MariaDB (Latest)
3. Sendgrid email account (for sending emails)

## Installation
Here’s a step-by-step procedure of the installation process for Python 3.9 and Git on Windows, Linux
(Ubuntu), and macOS:

### Python 3:
1. Windows:
   1. Visit the official Python website: `https://www.python.org/downloads/windows/`
   2. Look for Python 3.9.x and click on the appropriate installer (32-bit or 64-bit) for your system.
   3. Download the installer and run it.
   4. Check the box "Add Python 3.9 to PATH" to add Python to your system path.
   5. Click "Install Now" to start the installation process.
   6. Once the installation is complete, open a new Command Prompt and run following to verify the installation:
      ```
      python --version
      ```
2. Linux (Ubuntu):
   1. Open a terminal window.
   2. Run the following commands to update the package lists and install the required dependencies:
      ```
      sudo apt update
      sudo apt install software-properties-common
      ```
   3. Add the deadsnakes PPA repository to your system:
      ```
      sudo add-apt-repository ppa:deadsnakes/ppa
      ```
   4. Update the package lists again:
      ```
      sudo apt update
      ```
   5. Install Python 3.9:
      ```
      sudo apt install python3.9
      ```
   6. Verify the installation by running:
      ```
      python3.9 --version
      ```
3. macOS:
   1. Visit the official Python website:
      ```
      https://www.python.org/downloads/macos/
      ```
   2. Look for Python 3.9.x and click on the macOS installer.
   3. Download the installer and run it.
   4. Follow the prompts to complete the installation.
   5. Once the installation is complete, open a new Terminal window and run following to verify the installation:
      ```
      python3.9 --version
      ```

### MariaDB:
1. Windows:
   1. Visit the MariaDB download page: `https://downloads.mariadb.org/`
   2. Choose the appropriate Windows version (32-bit or 64-bit) for your system.
   3. Download the installer and run it.
   4. Follow the prompts, and set a root password during the installation process.
   5. After installation, open a new Command Prompt and run following to verify the installation:
      ```
      mysql --version
      ```
2. Linux (Ubuntu):
   1. Open a terminal window.
   2. Update the package lists:
      ```
      sudo apt update
      ```
   3. Install MariaDB server:
      ```
      sudo apt install mariadb-server
      ```
   4. Secure the installation:
      ```
      sudo mysql_secure_installation
      ```
   5. Follow the prompts and set a root password.
   6. Verify the installation by running:
      ```
      mysql --version
      ```
3. macOS:
   1. Install Homebrew if it is not already installed:
      ```
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
      ```
   2. Update Homebrew and install MariaDB:
      ```
      brew update
      brew install mariadb
      ```
   3. Start the MariaDB server:
      ```
      brew services start mariadb
      ```
   4. Secure the installation:
      ```
      mysql_secure_installation
      ```
   5. Follow the prompts and set a root password.
   6. After installation, open a new Terminal window and run following to verify the installation:
      ```
      mysql --version
      ```

## Setup
1. Clone the repository
   1. Open a terminal or command prompt.
   2. Navigate to the desired directory where you want to clone the repository.
   3. Run the following command:
      ```
      git clone URL of the repository
      ```

2. Check if the database is running
   1. MariaDB uses port 3306 by default. You can use a tool like `netstat` or `ss` to check if the database is running and listening on the default port:
      ```
      netstat -tuln | grep 3306
      or
      ss -tuln | grep 3306
      ```

3. Change the default MariaDB port (optional)
   1. Locate the MariaDB configuration file, usually named `my.cnf` or `50-server.cnf`, in one of the following directories:
      ```
      /etc/mysql/
      /etc/mysql/mariadb.conf.d/
      /usr/local/etc/ (macOS)
      ```
   2. Open the configuration file in a text editor with administrator privileges.
   3. Look for the [mysqld] section and change the `port` setting to the desired value, for example:
      ```
      port = 3307
      ```
   4. Save the file and restart the MariaDB server for the changes to take effect.

4. Run MariaDB SQL scripts to setup the database
   1. Navigate to the 'mariadb\_scripts' folder inside the cloned repository.
   2. Login to the MariaDB server as the root user or another user with necessary privileges:
      ```
      mysql -u root -p
      ```
   3. Enter your password when prompted.
   4. Execute the `0.sql` script:
      ```
      \. 0.sql
      ```
   5. Execute the `1.sql` script:
      ```
      \. 1.sql
      ```
   6. Exit the MariaDB server by running:
      ```
      exit
      ```

5. Rename .env.sample to .env 
   1. Locate the .env.sample file in the project's root folder and rename it to .env. It will have a structure like this:
      ```
      MYSQL_USER=
      MYSQL_DB=
      MYSQL_PASS=
      MYSQL_HOST=
      MYSQL_PORT=
    
      EMAIL_HOST_PASSWORD=
      DEFAULT_FROM_EMAIL=
      EMAIL_HOST_USER=apikey
      EMAIL_HOST=smtp.sendgrid.net
      EMAIL_PORT=587
      EMAIL_USE_TLS=True
    
      DJANGO_SECRET=
      ```
   2. You will use and edit this file later.

6. Generate Django secret key 
   1. Visit `https://djecrety.ir/` and click on the `Generate` button.
   2. You will get a unique secret key. Copy and paste it into the .env file where it says `DJANGO_SECRET`.
      ```
      DJANGO_SECRET=3n8$sb-qtudexj*da&*eyf87%-srom(od65y65%w)e!@5cn0gh
      ```
7. Set up environment variables
   1. Locate the `.env` file in the repository folder or create one if it does not exist.
   2. Open the `.env` file in a text editor.
   3. Set the environment variables as required, for example:
      ```
      MYSQL_USER=your_username
      MYSQL_DB=django_euf
      MYSQL_PASS=your_password
      MYSQL_HOST=localhost
      MYSQL_PORT=your_port
      ```
   4. Save and close the file.

8. Set up SendGrid account and API key 
   1. Visit the SendGrid website at `https://sendgrid.com/` and sign up for a free account.
   2. Once you have created an account and logged in, navigate to the "API Keys" page in the dashboard, which can be found under "Settings" on the left-hand side menu.
   3. Click the "Create API Key" button at the top-right corner of the page.
   4. Give your API key a name and select the appropriate level of permissions (e.g., "Full Access" for complete control).
   5. Click the "Create \& View" button to generate your API key.
   6. Copy the API key to your clipboard, as it will not be shown again for security reasons.
   7. Open the .env file in your project folder with a text editor.
   8. Add a new line to the file to set the SendGrid API key environment variable, for example:
      ```
      EMAIL_HOST_PASSWORD=your_sendgrid_api_key
      DEFAULT_FROM_EMAIL=your_sendgrid_email
      EMAIL_HOST_USER=apikey
      EMAIL_HOST=smtp.sendgrid.net
      EMAIL_PORT=587
      EMAIL_USE_TLS=True
      ```
   9. Replace your\_sendgrid\_api\_key and your\_sendgrid\_email with the actual API key you obtained from SendGrid and your SendGrid email address.
   10. Save and close the .env file.

9. Install requirements 
   1. Navigate to the root directory of the cloned repository.
   2. Install the required packages from the `requirements.txt` file by running the following command:
      ```
      python -m pip install -r requirements.txt
      ```

10. Default superuser created by MariaDB scripts 
    1. The MariaDB scripts provided in the `mariadb_scripts` folder contain a default superuser for your Django application. This superuser has the ability to manage all aspects of the application, including adding, modifying, and deleting data, as well as managing other users and their permissions. 
    2. To log in to your application using the default superuser, use the following credentials:
       ```
       Username: euf_admin
       Password: asdASD123!
       ```
    3. Make sure to change the default password for the superuser after logging in for the first time to ensure the security of your application.

11. Creating a new superuser using django (optional)
    1. If you want to create a new superuser for your Django application, follow these steps:
    2. Make sure you are in the root directory of the cloned repository.
    3. Run the following command to create a new superuser:
       ```
       python manage.py createsuperuser
       ```
    4. You will be prompted to enter a username, email address, and password for the new superuser. Provide the necessary information and confirm the password.
    5. Once the superuser is created, you can log in to your application using the new credentials.

12. Run the Django application
    1. Make sure you are in the root directory of the cloned repository.
    2. Run the following command to start the Django application:
       ```
       python manage.py runserver
       or
       python manage.py runserver_plus
       ```
    3. By default, the Django application will run on IP address `127.0.0.1` (localhost) and port `8000`. You can access the application in your web browser by navigating to `http://127.0.0.1:8000`.

13. Change the default IP address and port (optional)
    1. If you want to run the Django application on a different IP address or port, you can provide the desired values as arguments when running the `runserver` command. For example, to run the application on IP address `192.168.1.2` and port `8080`, use the following command:
       ```
       python manage.py runserver 192.168.1.2:8080
       ```
    2. Access the application in your web browser by navigating to the specified IP address and port, for example, `http://192.168.1.2:8080`.


## Configuration
1. Make sure you have virtual environment installed and ready. If not, run following:
```
python -m venv venv
source venv/bin/activate
```



- Follow the official documentation if you want to use a new database:
```
https://docs.djangoproject.com/en/4.1/ref/databases/
```

## Usage
1. By default, your website will run at:
```
http://localhost:8000/
```
2. Admin panel access (login with superuser credentials):
```
http://localhost:8000/admin/
```
3. Account access:
```
http://localhost:8000/account/login/?next=/
```