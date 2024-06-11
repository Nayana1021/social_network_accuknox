# Social Network API

This is a social networking application API built using Django, Django Rest Framework, and MongoDB (with djongo).

## Features

- User Signup
- User Login
- Search Users by Email or Name
- Send/Accept/Reject Friend Requests
- List Friends
- List Pending Friend Requests

## Installation

### Prerequisites

- Python 3.8+
- MongoDB
- Virtualenv (optional but recommended)

### Steps

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Nayana1021/social_network_api.git
    cd social_network_api
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up MongoDB:**
    Make sure MongoDB is installed and running. By default, the application is configured to connect to MongoDB on `localhost:27017`. You can adjust the database settings in `social_network/settings.py` if needed.

5. **Apply database migrations:**
    ```sh
    python manage.py migrate
    ```

6. **Create a superuser (optional, for accessing the Django admin site):**
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

    The API will be available at `http://127.0.0.1:8000/`.

### Docker Setup

Alternatively, you can run the application using Docker.

1. **Build and run the containers:**
    ```sh
    docker-compose up --build
    ```

    The API will be available at `http://localhost:8000/`.

## API Endpoints

### User Signup
- **Method:** POST
- **URL:** `/api/signup/`
- **Body:**
    ```json
    {
        "username": "test_user",
        "email": "test@example.com",
        "password": "password123"
    }
    ```

### User Login
- **Method:** POST
- **URL:** `/api/login/`
- **Body:**
    ```json
    {
        "email": "test@example.com",
        "password": "password123"
    }
    ```

### Search Users
- **Method:** GET
- **URL:** `/api/search/?query=test`

### Send Friend Request
- **Method:** POST
- **URL:** `/api/friend-request/`
- **Body:**
    ```json
    {
        "to_user": "<user_id>"
    }
    ```

### Respond to Friend Request
- **Method:** POST
- **URL:** `/api/friend-request/<request_id>/<response>/`
- **Parameters:** Replace `<request_id>` with the ID of the friend request, and `<response>` with either `accept` or `reject`.

### List Friends
- **Method:** GET
- **URL:** `/api/friends/`

### List Pending Friend Requests
- **Method:** GET
- **URL:** `/api/pending-requests/`

## Postman Collection

A Postman collection for testing the API endpoints is included in the repository as `social_network_api.postman_collection.json`.

## License

This project is licensed under the MIT License.

