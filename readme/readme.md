
# BH Sticky Notes Application

## Description

BH Sticky Notes is a simple Django application that allows users to create, view, update, and delete notes.

## Features

- User authentication (register, login, logout)
- Create a new note
- View a list of all notes
- View details of a single note
- View a list of notes created by the logged-in user
- Update an existing note
- Delete a note

## Setup and Installation

### Prerequisites

- Python 3.x
- Django

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/ben-head/sticky_notes.git
   cd sticky_notes
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```sh
   python manage.py migrate
   ```

5. Create a superuser to access the Django admin:

   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```sh
   python manage.py runserver
   ```

7. Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the application.

## Running Tests

To run the unit tests, use the following command:

   ```sh
   python manage.py test posts
   ```

## License

This project is licensed under the MIT License.
