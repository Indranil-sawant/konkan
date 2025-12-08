# Explore Ratnagiri - Project Guide

## Project Overview
This is a production-ready Django project for "Explore Ratnagiri", a tourism website. It features destinations, reviews, and user accounts.

## Setup Instructions

### 1. Run Locally
```bash
# Install dependencies (if any new ones are added, currently standard Django + Whitenoise)
pip install django whitenoise pillow psycopg2-binary

# Run Migrations
python manage.py migrate

# Create Superuser (Already created: admin/admin)
# python manage.py createsuperuser

# Run Server
python manage.py runserver
```

### 2. Project Structure
- `config/`: Main settings and configuration.
- `core/`: Homepage and static pages.
- `destinations/`: Destination models and views.
- `reviews/`: Review system.
- `accounts/`: User authentication.
- `templates/`: HTML templates.
- `static/`: Static files (CSS, JS, Images).
- `media/`: User uploaded content.

### 3. Admin Panel
- URL: `/admin/`
- Username: `admin`
- Password: `admin`

### 4. Deployment (Render/Hostinger)
- **Render**:
    - Connect GitHub repo.
    - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
    - Start Command: `gunicorn config.wsgi:application`
    - Add Environment Variables: `SECRET_KEY`, `DEBUG=False`, `DATABASE_URL`.

## Features Implemented
- **Homepage**: Hero section, Featured destinations, Trending Forts.
- **Destinations**: List view with search & category filter, Detail view with gallery & map.
- **Reviews**: User ratings and comments.
- **Accounts**: Login/Register.
