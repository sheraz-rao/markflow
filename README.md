# MarkFlow API Documentation

## Overview

This is the backend API for MarkFlow, an online Markdown editor. It allows users to create, edit, and manage their Markdown documents. The API is built using Django REST Framework and uses JWT for user authentication.

## Endpoints

### User Authentication

* **Login** (`POST /api/users/<id>/login/`)
    * Path Parameter: `id` (integer) - The ID of the user to log in.
    * Payload:
        ```json
        {
            "password": "securepassword"
        }
        ```
    * Response (Success - HTTP 200 OK):
        ```json
        {
            "refresh": "<refresh_token>",
            "access": "<access_token>"
        }
        ```
    * Response (Failure - HTTP 401 Unauthorized):
        ```json
        {
            "error": "Invalid credentials"
        }
        ```
    * Response (Failure - HTTP 404 Not Found):
        ```json
        {
            "error": "Invalid User ID."
        }
        ```
    * Response (Failure - id missing from url):
        ```json
        {
            "error": "User ID is required."
        }
        ```
    * Response (Failure - missing body):
        ```json
        {
            "error": "Password is required."
        }
        ```

### Documents

* **Create Document** (`POST /api/documents/`)
    * Headers: `Authorization: Bearer <access_token>`
    * Payload:
        ```json
        {
            "title": "My First Document",
            "content": "# Hello Markdown",
            "tag_ids": [1, 2] // Optional: List of tag IDs to associate
        }
        ```
    * Response (Success - HTTP 201 Created):
        ```json
        {
          "id": 4,
          "title": "My First Document",
          "content": "# Hello Markdown",
          "created_at": "2025-04-29T14:36:30.163345Z",
          "updated_at": "2025-04-29T14:36:30.163381Z",
          "tags": [
              {
                  "id": 1,
                  "name": "python"
              },
              {
                  "id": 2,
                  "name": "django"
              }
          ]
        }
        ```

* **Fetch All Documents** (`GET /api/documents/`)
    * Headers: `Authorization: Bearer <access_token>`
    * Query Parameters (Optional):
        * `ordering`: `created_at` , `updated_at`
        * `tags__id`: Filter by tag ID. Example: `/api/documents/?tags__id=1` 
    * Response (Success - HTTP 200 OK):
        ```json
        [
            {
            "id": 1,
            "title": "test",
            "content": "this is a test doc",
            "created_at": "2025-04-29T13:55:35.405703Z",
            "updated_at": "2025-04-29T13:55:44.562160Z",
            "tags": [
                {
                    "id": 1,
                    "name": "python"
                },
                {
                    "id": 2,
                    "name": "django"
                }
            ]
        },
            ...
        ]
        ```

* **Retrieve Specific Document** (`GET /api/documents/<id>/`)
    * Headers: `Authorization: Bearer <access_token>`
    * Path Parameter: `id` (integer) - The ID of the document.
    * Response (Success - HTTP 200 OK):
        ```json
        {
            "id": 1,
            "title": "test",
            "content": "this is a test doc",
            "created_at": "2025-04-29T13:55:35.405703Z",
            "updated_at": "2025-04-29T13:55:44.562160Z",
            "tags": [
                {
                    "id": 1,
                    "name": "python"
                },
                {
                    "id": 2,
                    "name": "django"
                }
            ]
        }
        ```

* **Update Existing Document** (`PATCH /api/documents/<id>/`)
    * Headers: `Authorization: Bearer <access_token>`
    * Path Parameter: `id` (integer) - The ID of the document to update.
    * Payload (Partial updates are allowed):
        ```json
        {
            "title": "Updated Document Title",
            "content": "New content here",
            "tag_ids": [3] // Replace existing tags with tag ID 3
        }
        ```
    * Response (Success - HTTP 200 OK):
        ```json
        {
            "id": 2,
            "title": "Updated Document Title",
            "content": "New content here",
            "created_at": "2025-04-29T13:56:02.324949Z",
            "updated_at": "2025-04-29T14:39:19.756939Z",
            "tags": [
                {
                    "id": 3,
                    "name": "django-rest"
                }
            ]
        }
        ```

* **Delete Document** (`DELETE /api/documents/<id>/`)
    * Headers: `Authorization: Bearer <access_token>`
    * Path Parameter: `id` (integer) - The ID of the document to delete.
    * Response (Success - HTTP 204 No Content):
      ```json
        {'message': 'Document deleted'}
      ```

## Steps to Run the Project Locally

1.  **Clone the repository:**
    ```bash
    git clone <your_github_repo_url>
    cd <your_repo_name>
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    # venv\Scripts\activate
    # On macOS and Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    
4.  **Make migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

    The API will be accessible at `http://127.0.0.1:8000/api/`.

## .gitignore

Create a file named `.gitignore` in the root of your project with the following content:
