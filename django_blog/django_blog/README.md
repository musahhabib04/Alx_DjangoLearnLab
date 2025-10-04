# 📝 Django Blog Project

A simple blog app built with **Django**, part of the **Alx_DjangoLearnLab**.  
It demonstrates models, templates, authentication, and profile management.

---

## 🚀 Features
- User registration, login, and logout  
- Profile management for authenticated users  
- `Post` model with title, content, author, and published date  
- CSRF protection & secure password handling  
- Ready for CRUD blog functionality  

---

## 🏗️ Setup Instructions
1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/django_blog
   ```
2. Create virtual environment & install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   pip install django
   ```
3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Start server:
   ```bash
   python manage.py runserver
   ```
   Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧩 Models
**Post**
```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
```

---

## 🔐 Authentication
- **Register** → `/register/`  
- **Login** → `/login/`  
- **Logout** → `/logout/`  
- **Profile** → `/profile/` (authenticated users only)  

---

## 🧪 Testing
Run all tests:
```bash
python manage.py test
```

---

## 👨‍💻 Author
**Habib Musah**  
[LinkedIn](https://www.linkedin.com/in/habib-musah-5498bb161)  

---
