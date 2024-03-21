# Viblo

Viblo is a web application built with Django, allowing users to create, manage, and share pages/notes seamlessly. Users can personalize their content, download it for offline use, and choose to keep it private or share it with others.

## Getting Started

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/dheerajroy/viblo.git
    ```

2. Install the required packages from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
4. Create super user to access admin panel at `/admin`:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Open your web browser and visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to start using Viblo.

## Usage

1. Sign in or create an account.
2. Explore the features: create pages/notes, download, share and manage privacy settings.
