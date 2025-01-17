# Django Chat

This is a real-time chat application built using Django and Django Channels. The purpose of this project is to provide a platform where users can communicate with each other in real-time through web sockets.

## Purpose

The main purpose of this project is to demonstrate the use of Django Channels to implement real-time features in a Django application. It includes user authentication, real-time messaging, and a simple user interface for chatting.

## Tech Stack

- **Backend**: Django, Django Channels
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **WebSockets**: Django Channels
- **ASGI Server**: Daphne

## Features

- User authentication (login, logout, register)
- Real-time messaging
- User-friendly chat interface
- Message notifications

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:

   ```sh
   git clone https://github.com/JaiSwarup/django-chat.git
   cd chat_app
   ```

2. **Create a virtual environment**:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply the migrations**:

   ```sh
   python manage.py migrate
   ```

5. **Create a superuser**:

   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server**:

   ```sh
   python manage.py runserver
   ```

7. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Project Structure

- : Main Django application
- : Chat application
- : User management application
- : Static files (CSS, JavaScript, Images)
- : HTML templates
- : SQLite database file
- : Django management script
- `requirements.txt`: Python dependencies

## Configuration

The main configuration for the project is located in . Here you can configure the database, installed apps, middleware, and other settings.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a pull request

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Django Channels](https://channels.readthedocs.io/en/stable/)
- [Bootstrap](https://getbootstrap.com/)
