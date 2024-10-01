# This file is meant to be used in Windows Powershell.

# Create a virtual environment
Write-Host "Creating virtual environment..."
python -m venv venv

# Activate the virtual environment
Write-Host "Activating virtual environment..."
& .\venv\Scripts\Activate.ps1

# Install the django-related dependencies
Write-Host "Installing Django, django-bootstrap-5, and django-filter..."
pip install django django-bootstrap-v5 django-filter

# Run migrations to initializq the sqlite database based on the model
Write-Host "Running migrations..."
python manage.py makemigrations
python manage.py migrate

# Run the Django server
Write-Host "Starting the Django development server..."
python manage.py runserver
