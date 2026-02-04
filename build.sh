#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python3 manage.py collectstatic --no-input

echo "Running migrations..."
python3 manage.py migrate

echo "Build script finished successfully!"
