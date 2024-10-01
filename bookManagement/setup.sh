#!/bin/bash
# This file is meant to be used in a Linux environment.

# Update package list and install python3 if not already installed
echo "Checking for python3..."
if ! dpkg -s python3 &> /dev/null
then
    echo "python3 not found, installing it now..."
    sudo apt update
    sudo apt install -y python3
else
    echo "python3 is already installed."
fi

# Update package list and install python3-venv if not already installed
echo "Checking for python3-venv..."
if ! dpkg -s python3-venv &> /dev/null
then
    echo "python3-venv not found, installing it now..."
    sudo apt update
    sudo apt install -y python3-venv
else
    echo "python3-venv is already installed."
fi

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install the django-related dependencies
echo "Installing Django, django-bootstrap-5, and django-filter..."
pip install django django-bootstrap-v5 django-filter

# Run migrations to initializq the sqlite database based on the model
echo "Running migrations..."
python3 manage.py makemigrations
python3 manage.py migrate

# Run the Django server
echo "Starting the Django development server..."
python3 manage.py runserver
