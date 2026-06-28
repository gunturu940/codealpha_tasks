# StyleHub — E-Commerce Store

> **CodeAlpha Internship | Task 1 | Full Stack Development**

StyleHub is a fully responsive e-commerce web application where users can browse products, add items to a cart, and manage their shopping experience. Built using Django on the backend and HTML/CSS/JavaScript with Bootstrap on the frontend.

---

## 🚀 Features

- 🏠 **Home Page** — Hero banner, featured products, category highlights
- 🛍️ **Product Listing** — Browse all available products with images and pricing
- 📄 **Product Detail Page** — Individual product view with description and add-to-cart
- 🛒 **Shopping Cart** — Add, remove, and review selected items
- 🔐 **User Authentication** — Register and login functionality
- 📱 **Responsive Design** — Works on mobile, tablet, and desktop

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
CodeAlpha_StyleHub/
├── stylehub_backend/        # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── store/                   # Main Django app
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── templates/               # HTML templates
│   ├── index.html
│   ├── products.html
│   ├── product_detail.html
│   ├── cart.html
│   ├── login.html
│   └── register.html
├── static/                  # CSS, JS, Images
├── manage.py
└── requirements.txt
```

---

## ⚙️ Setup & Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/gunturu940/codealpha_tasks.git
cd codealpha_tasks/CodeAlpha_StyleHub

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start the server
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 📸 Pages Overview

| Page | URL |
|------|-----|
| Home | `/` |
| Products | `/products/` |
| Cart | `/cart/` |
| Login | `/login/` |
| Register | `/register/` |

---

## 👩‍💻 Developer

**Pallavi Gunturu** — CodeAlpha Intern (CA/DF1/107803)  
GitHub: [@gunturu940](https://github.com/gunturu940)