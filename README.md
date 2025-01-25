# Django CRUD Operations 🛠️

This repository demonstrates basic Create, Read, Update, and Delete (CRUD) operations using the Django framework with an SQLite database. The project is built with Django 4.x and uses SQLite as the database backend for simplicity.

## Features ✨

- **Create**: Add new records to the database. 📝
- **Read**: View records from the database. 🔍
- **Update**: Modify existing records in the database. ✏️
- **Delete**: Remove records from the database. 🗑️

## Requirements ⚙️

- Python 3.8 or higher 🐍
- Django 4.x 📦

## Installation 🚀

Follow these steps to get the project up and running:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/rahull0328/django-crud.git
    cd django-crud
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:
    
        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:
    
        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    Now, the application will be running on [http://127.0.0.1:8000](http://127.0.0.1:8000). 🎉
