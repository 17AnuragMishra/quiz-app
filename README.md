# Quiz Web Application

Welcome to the **Quiz Web Application**! This is a simple application for user to take quiz based on random questions built with **Django** for the backend and **HTML, CSS, and JavaScript** for the frontend. It allows users to answer quiz questions, track scores, and view results.

---

## Features

- 🎯 **Dynamic Questions**: Randomly fetch quiz questions from the backend.
- ✅ **Interactive Feedback**: Highlight correct and incorrect answers.
- 📊 **Score Tracking**: View real-time score updates and progress.
- 🔒 **User Authentication**: Secure user sessions via Django login.
- 📱 **Responsive UI**: Built with Bootstrap for mobile responsiveness.

---

## Requirements

Make sure the following tools are installed on your system:

- **Python** (>= 3.8)
- **pip** (Python package manager)
- **Virtualenv** (optional but recommended)
- **Django** (installed via requirements.txt)

---

## Setup Instructions

Follow the steps below to set up and run the application:

### 1. Clone the  Repository
```bash
git clone https://github.com/yourusername/quiz-web-app.git
cd quiz-web-app

 2. Set Up a Virtual Environment
Create and activate a virtual environment for dependency isolation.
For Windows:
pip install virtualenv
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
Install all required Python packages from the requirements.txt file:
pip install -r requirements.txt

4. Database Setup
Run the following commands to set up the database schema:
python manage.py makemigrations
python manage.py migrate

5. Superuser for adding questions
user : test
pass: test

6: Run the Server
python manage.py runserver

