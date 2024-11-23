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
DB_NAME=task_management
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```
- Save the .env file. The values in this file will now be used by the application.

2. Environment Variables
Here’s a description of each environment variable in the .env file:

DB_NAME: The name of your PostgreSQL database.\
DB_USER: The username used to connect to the database.\
DB_PASSWORD: The password for the database user.\
DB_HOST: The host where your database is located (usually localhost).\
DB_PORT: The port for connecting to the database (usually 5432 for PostgreSQL).

3. To install Required Dependencies
Ensure you have the necessary Python packages installed to load the environment variables and interact with the database. You can install them with:

```bash
pip install -r requirements.txt

```
