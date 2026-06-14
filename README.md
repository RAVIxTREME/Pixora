
# 📸 Pixora

> Instagram-style photo sharing web app built with Django & MySQL.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

---

## ✨ Features

- 📷 Photo upload & sharing
- ❤️ Like system (AJAX — no page reload)
- 💬 Comments — add & delete
- 👥 Follow / Unfollow system
- 🔍 Explore page — discover all posts
- 🔐 Register & Login system
- 🌙 Dark theme UI (Instagram style)
- 👤 User profile with post grid

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Database | MySQL |
| Frontend | HTML5, CSS3, Bootstrap 5 |
| Interactivity | JavaScript, AJAX Fetch API |
| Image Handling | Pillow |

---

## 📁 Project Structure

```
pixora/
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── posts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       └── posts/
│           ├── home.html
│           ├── explore.html
│           ├── create_post.html
│           ├── post_detail.html
│           └── profile.html
├── templates/
│   ├── base.html
│   └── registration/
│       ├── login.html
│       └── register.html
├── manage.py
└── .gitignore
```

---

## 🗄️ Database Models

- **Post** — image, caption, user, timestamp
- **Like** — user + post relation
- **Comment** — user + post + text
- **Follow** — follower + following relation

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/RAVIxTREME/pixora.git
cd pixora

# 2. Create virtual environment
python -m venv myenv
myenv\Scripts\activate

# 3. Install dependencies
pip install django mysqlclient pillow

# 4. Create MySQL database
# Run in MySQL: CREATE DATABASE pixora_db;

# 5. Update settings.py with your MySQL password

# 6. Migrate
python manage.py makemigrations posts
python manage.py migrate

# 7. Run server
python manage.py runserver
```

---

## 👨‍💻 Developer

**Ravi Bhosale**
Full Stack Developer | Pune, Maharashtra
📧 ravixtreme7@gmail.com
🔗 [GitHub](https://github.com/RAVIxTREME)

---

> *"Code xtreme, my name RaviXtreme"* 🔥
