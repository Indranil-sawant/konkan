#!/usr/bin/env bash
# exit on error
set -o errexit

echo "==> Upgrading pip and installing Python dependencies..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "==> Building Tailwind CSS..."
if command -v npm >/dev/null 2>&1 && [ -f "package.json" ]; then
    npm install
    npm run build:css || true
fi

echo "==> Collecting static files..."
python manage.py collectstatic --no-input

echo "==> Applying database migrations..."
python manage.py migrate

echo "==> Seeding initial Companion & Tourism CMS data..."
python manage.py seed_companion_data || true

echo "==> Build finished successfully!"
