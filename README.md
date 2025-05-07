# 🎯 QuizCraze

**QuizCraze** is a Django-based web application designed for creating, managing, and participating in online quizzes. It provides a user-friendly interface for both quiz creators and participants.

---

## 📌 Features

- 🧠 Create and manage quizzes
- ✍️ Add multiple-choice questions
- 👨‍🎓 Participate in quizzes and submit answers
- 📊 View results and scores
- 🔐 User authentication (Login & Register)
- 🖥️ Responsive UI using Django templates

---

## ⚙️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap (via Django templates)
- **Database:** SQLite (default with Django)
- **Version Control:** Git + GitHub

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone git@github.com:SaliniSundaran2002/QuizCraze.git
cd QuizCraze
```
### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Run the Development Server
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your browser to view the app.

## 📁 Project Structure
```bash
QuizCraze/
├── quizapp/              # Main app
│   ├── models.py         # DB Models
│   ├── views.py          # App logic
│   ├── urls.py           # App routes
│   └── templates/        # HTML templates
├── QuizCraze/            # Project settings
├── db.sqlite3            # SQLite database
└── manage.py             # Django CLI entry point
└── requirements.txt                   
```

## Screenshots

### Screenshot 1
![Screenshot 1](assets/images/screenshot1.png)

### Screenshot 2
![Screenshot 2](assets/images/screenshot2.png)


## Screen Recording

### Demo Video:
![Demo Video](assets/videos/demo.mp4)





