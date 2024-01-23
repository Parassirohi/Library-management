# Library Management System

The Library Management System is a Django-based web application that allows administrators to manage genres, authors, and books in a library.

## Features

- **Admin Functions:**
  - Add, edit, and delete genres.
  - Add, edit, and delete authors.
  - View details of all authors, including their books.

- **Author Functions:**
  - Sign up with name, phone, email, city, and profile image.
  - Automatically generate a unique registration code based on the city.
  - Add multiple books related to the author.

## Getting Started

### Prerequisites

- Python (3.7 or higher)
- Django (3.x)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Parassirohi/Library-management.git
   cd Library-management
   ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```
    
3. Activate the virtual environment:

    ```bash
    source venv/bin/activate 
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run Migrations:
    ```bash
    python manage.py migrate
    ```

6. Start the server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and navigate to http://localhost:8000/admin/ to log in as the admin.
    - superuser username -- new_user
    - password -- newuser
  
8. For authentication we use Token based authentication Djoser. To login :
    ```bash
    localhost:8000/auth/token/login/
    ```
    - use username -- user1
    - password -- ILOVEDJANGO
  
9. To create an login account:
    ```bash
    localhost:8000/auth/users/
    ```

## API Endpoints

### Genres

- **List all genres:**
  - `GET /api/genres/`

- **Retrieve a specific genre:**
  - `GET /api/genres/{genre_id}/`

- **Create a new genre:**
  - `POST /api/genres/`

- **Update a genre:**
  - `PUT /api/genres/{genre_id}/`

- **Delete a genre:**
  - `DELETE /api/genres/{genre_id}/`

### Admin

- **List all administrators:**
  - `GET /api/admin/`

- **Retrieve a specific administrator:**
  - `GET /api/admin/{admin_id}/`

- **Create a new administrator:**
  - `POST /api/admin/`

- **Update an administrator:**
  - `PUT /api/admin/{admin_id}/`

- **Delete an administrator:**
  - `DELETE /api/admin/{admin_id}/`

### Authors

- **List all authors:**
  - `GET /api/authors/`

- **Retrieve a specific author:**
  - `GET /api/authors/{registration_code}/`

- **Create a new author:**
  - `POST /api/authors/`

- **Update an author:**
  - `PUT /api/authors/{registration_code}/`

- **Delete an author:**
  - `DELETE /api/authors/{registration_code}/`

### Books

- **List all books:**
  - `GET /api/books/`

- **Retrieve a specific book:**
  - `GET /api/books/{book_id}/`

- **Create a new book:**
  - `POST /api/books/`

- **Update a book:**
  - `PUT /api/books/{book_id}/`

- **Delete a book:**
  - `DELETE /api/books/{book_id}/`

## Usage
- Access the admin interface to manage genres, authors, and books.
- Authors can sign up and add books related to them.

## Contributing
- Contributions are welcome! Please follow the contribution guidelines.

## License
- This project is licensed under the MIT License - see the LICENSE file for details.


