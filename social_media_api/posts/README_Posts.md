# Posts App - Social Media API

## 📘 Overview
The **Posts App** is part of the `social_media_api` Django project.  
It allows authenticated users to **create, view, update, and delete posts and comments** within the social media platform.

This module builds upon the user authentication system created in the `accounts` app.

---

## ⚙️ Features
- Create, view, update, and delete posts.
- Add, edit, and delete comments on posts.
- Pagination and filtering support for large datasets.
- Permission control so users can only modify their own content.
- Integrated with Django REST Framework for API endpoints.

---

## 🧩 Models
### **Post**
| Field | Type | Description |
|-------|------|-------------|
| author | ForeignKey (User) | The creator of the post |
| title | CharField | Title of the post |
| content | TextField | Body/content of the post |
| created_at | DateTimeField | Auto timestamp when created |
| updated_at | DateTimeField | Auto timestamp when updated |

### **Comment**
| Field | Type | Description |
|-------|------|-------------|
| post | ForeignKey (Post) | Post that this comment belongs to |
| author | ForeignKey (User) | The user who made the comment |
| content | TextField | Comment text |
| created_at | DateTimeField | Auto timestamp when created |
| updated_at | DateTimeField | Auto timestamp when updated |

---

## 🧠 API Endpoints

### **Posts**
| Method | Endpoint | Description |
|---------|-----------|-------------|
| GET | `/api/posts/` | List all posts |
| POST | `/api/posts/` | Create a new post |
| GET | `/api/posts/{id}/` | Retrieve a single post |
| PUT | `/api/posts/{id}/` | Update an existing post |
| DELETE | `/api/posts/{id}/` | Delete a post |

### **Comments**
| Method | Endpoint | Description |
|---------|-----------|-------------|
| GET | `/api/comments/` | List all comments |
| POST | `/api/comments/` | Create a new comment |
| GET | `/api/comments/{id}/` | Retrieve a single comment |
| PUT | `/api/comments/{id}/` | Update a comment |
| DELETE | `/api/comments/{id}/` | Delete a comment |

---

## 🔐 Authentication
All endpoints require authentication using **Token Authentication** from the `accounts` app.

Include your token in the request headers:

```
Authorization: Token <your_token_here>
```

---

## 🧪 Example Requests

### Create a Post
```json
POST /api/posts/
{
    "title": "My First Post",
    "content": "This is an example post."
}
```

### Add a Comment
```json
POST /api/comments/
{
    "post": 1,
    "content": "Great post!"
}
```

---

## 🧭 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/social_media_api
   ```

2. Activate the virtual environment:
   ```bash
   source venv/Scripts/activate   # On Windows
   ```

3. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the server:
   ```bash
   python manage.py runserver
   ```

5. Access the API at:  
   👉 `http://127.0.0.1:8000/api/posts/`

---

## 🧾 Credits
Developed as part of the **ALX Django Learn Lab Project** — Social Media API.  
Author: **Habib Musah**  
GitHub: [habibmusah](https://github.com/habibmusah)  
LinkedIn: [Habib Musah](https://www.linkedin.com/in/habib-musah-5498bb161)
