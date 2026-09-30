# Harness App

A minimal Flask web application with user profiles and an admin panel.

## Requirements

- Python 3.9+

## Setup

```bash
pip install flask
```

## Run

```bash
python app.py
```

The app starts at http://127.0.0.1:5000.

The database is created automatically on first run. A default admin account is seeded:

- **Username:** `admin`
- **Password:** `admin123`

## Features

- Sign up / login / logout
- View and edit user profiles
- Admin user list with delete
