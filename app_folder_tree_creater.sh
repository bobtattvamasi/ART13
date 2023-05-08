#!/bin/bash

# Create app directory and files
mkdir app
touch app/Dockerfile
touch app/manage.py
mkdir app/myapp
touch app/myapp/__init__.py
touch app/myapp/settings.py
touch app/myapp/urls.py
touch app/myapp/wsgi.py

# Create task_loader directory and files
mkdir task_loader
touch task_loader/Dockerfile
touch task_loader/task_loader.py

# Create a DB-slot
mkdir db
touch db/Dockerfile

# Create a redis slot
mkdir redis
touch redis/Dockerfile

# Create chatbot directory and files
mkdir chatbot
touch chatbot/Dockerfile
touch chatbot/chatbot.py
