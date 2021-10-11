# Flask Rest API Template
![GitHub last commit](https://img.shields.io/github/last-commit/Kaspary/nubank_savemoney_integration)

## About The Project
Simple Rest API flask template, to start build API.

### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Flask-JWT](https://pythonhosted.org/Flask-JWT/)


## Getting Started

### Prerequisites
### Installation

1. Cloning this repository.
    ```sh
    $ git clone https://github.com/Kaspary/simple-flask-api-template.git
    ```

2. Creating and activate a python virtual environment, with your favorite tool.
    ```sh
    $ virtualenv env && source env/bin/activate
    ```

3. Install all dependencies.
    ```sh
    $ pip install -r requirements.txt
    ```

4. Creating a file named `.env`, into the project (using `example.env` as example).

5. Run project
    ```sh
    $ flask run
    ```

### Database migration

1. Run migration to create database schema.
    ```sh
    $ flask db init
    ```
## Usage
### User cli manager

#### Commands
- **flask user create**: Create new user;
Examples:
    ```sh
    $ flask user create my_user
    ```
    ```sh
    $ flask user create my_admin_user --admin
    ```
    ```sh
    $ flask user create my_new_user --auto-pass
    ```
- **flask user list**: List all users:
    - Example:
    ```sh
    $ flask user list
    ```
- **flask user delete**: Delete a user by id;
    - Example:
    ```sh
    $ flask user delete 1
    ```
- **flask user activation**: Set a user as active by id;
    - Example:
    ```sh
    $ flask user activation 1
    ```
- **flask user newpassword**: Set new password to user by id.
    - Example:
    ```sh
    $ flask user newpassword 1
    ```
    ```sh
    $ flask user newpassword 1 --auto-pass
    ```

#### Flags
- **--admin**: Set user as admin on `create` command;
    ```sh
    $ flask user create my_user --admin
    ```
- **--auto-pass**: Using to generete a random pass on `newpassword` or `create` command.
    ```sh
    $ flask user create my_user --auto-pass
    ```

### Run project
After instalation, run this command:
```sh
$ flask run
```
Access API on `http://127.0.0.1:5000`.

### Using API
To understed how to using the API, access `http://127.0.0.1:5000/documentation` and get documentation.
A postman collection is accessible on `http://127.0.0.1:5000/documentation/postman`.


#### Documentation
Web Documentation is generatig using [Docgen](https://github.com/thedevsaddam/docgen) project.

<p align="right">(<a href="#top">back to top</a>)</p>
