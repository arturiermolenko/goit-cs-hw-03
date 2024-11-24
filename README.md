# goit-cs-hw-03

## Setting Up the Environment
To set up the environment variables for the project, follow these steps:

1. Create a .env file
In the root of the project, you will find a file named .sample.env.
- Copy the .sample.env file and rename it to .env:

```bash
cp .sample.env .env
```

- Open the newly created .env file in a text editor.

- Modify the values of the environment variables to match your local configuration. Below is an example of the content in .sample.env:

```plaitext
task_1:
DB_NAME=task_management
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

task_2
MONGO_USER=your_mongo_username
MONGO_PASS=your_mongo_pass
APP_NAME=name_of_the_application
```
- Save the .env file. The values in this file will now be used by the application.

2. Environment Variables
Here’s a description of each environment variable in the .env file:

### task_1
DB_NAME: The name of your PostgreSQL database.\
DB_USER: The username used to connect to the database.\
DB_PASSWORD: The password for the database user.\
DB_HOST: The host where your database is located (usually localhost).\
DB_PORT: The port for connecting to the database (usually 5432 for PostgreSQL).

### task_2
MONGO_USER: Your username
MONGO_PASS: Your password
APP_NAME: Name of the application


3. Install Required Dependencies
Ensure you have the necessary Python packages installed to load the environment variables and interact with the database. 
You can install them with(go to the tasks folder to find requirements for needed project):

```bash
pip install -r requirements.txt

```
