# ProjectManager — Kanban Project Management App

> **CodeAlpha Internship | Task 3 | Full Stack Development**

ProjectManager is a full-featured project management web application with a Kanban-style board. Users can create projects, assign tasks with priorities and deadlines, collaborate with team members, and track progress through To Do → In Progress → Done stages.

---

## 🚀 Features

- 📊 **Dashboard** — Overview of all your projects and recent activity
- 📁 **Project Management** — Create, edit, and delete projects
- ✅ **Task Management** — Add tasks with title, description, priority, and deadline
- 🗂️ **Kanban Board** — Drag-and-drop style task status: To Do / In Progress / Done
- 👥 **Team Collaboration** — Assign tasks to project members
- 💬 **Comments System** — Comment on tasks for team communication
- 🔐 **User Authentication** — Secure register, login, and logout
- 📱 **Responsive Design** — Works seamlessly on all screen sizes

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3, Django |
| Frontend | HTML5, CSS3, JavaScript |
| UI Framework | Bootstrap 5 |
| Database | SQLite |
| Icons | Font Awesome |

---

## 📂 Project Structure

```
CodeAlpha_ProjectManager/
├── projectmanager/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── projects/                # Main Django app
│   ├── models.py            # Project, Task, Comment models
│   ├── views.py             # All CRUD views
│   ├── urls.py
│   └── forms.py
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── project_list.html
│   ├── project_detail.html
│   ├── kanban.html
│   ├── task_detail.html
│   ├── login.html
│   └── register.html
├── static/
├── manage.py
└── requirements.txt
```

---

## ⚙️ Setup & Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/gunturu940/codealpha_tasks.git
cd codealpha_tasks/CodeAlpha_ProjectManager

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. (Optional) Create superuser for admin panel
python manage.py createsuperuser

# 6. Start the server
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 📸 Pages Overview

| Page | URL |
|------|-----|
| Dashboard | `/` |
| Projects List | `/projects/` |
| Project Detail | `/projects/<id>/` |
| Kanban Board | `/projects/<id>/kanban/` |
| Task Detail | `/tasks/<id>/` |
| Login | `/login/` |
| Register | `/register/` |

---

## 🗂️ Task Priority Levels

- 🔴 **High** — Urgent tasks
- 🟡 **Medium** — Normal priority
- 🟢 **Low** — Nice to have

---

## 👩‍💻 Developer

**Pallavi Gunturu** — CodeAlpha Intern (CA/DF1/107803)  
GitHub: [@gunturu940](https://github.com/gunturu940)