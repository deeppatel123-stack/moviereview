# 🎬 Movie Review System

A Movie Review System developed using Django that allows users to explore movies, read reviews, and share their opinions through ratings and comments. The platform provides authentication features and an easy-to-use interface for managing movie reviews.

## 🚀 Features

- User registration and login
- Browse movie listings
- View movie details
- Add reviews and ratings
- Edit and delete reviews
- Responsive user interface
- Secure authentication system
- Admin panel for managing movies and reviews

## 🛠️ Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS
- Bootstrap
- JavaScript

## 📂 Project Structure

```text
moviereview/
│── accounts/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
│── movie/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
│── media/
│   └── movie/images/
│
│── db.sqlite3
│── manage.py
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Move to the project directory

```bash
cd moviereview
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install django
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

### 8. Open the application

```text
http://127.0.0.1:8000/
```

## 📸 Screens Included

- Home page
- Login page
- Registration page
- Movie details page
- Add review page
- Update review page

## 🔮 Future Enhancements

- Search movies
- Filter movies by category
- User profiles
- Favorite movies feature
- Review analytics and statistics

## 👨‍💻 Author

Deep Patel

Developed as a Django-based Movie Review System project.
