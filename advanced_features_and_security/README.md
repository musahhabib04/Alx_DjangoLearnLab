# Permissions & Groups Setup

## Custom Permissions
- Defined in `Book` model (`relationship_app/models.py`):
  - `can_view`
  - `can_create`
  - `can_edit`
  - `can_delete`

## Groups (create in Django Admin)
- **Viewers** → `can_view`
- **Editors** → `can_view`, `can_create`, `can_edit`
- **Admins** → all (`can_view`, `can_create`, `can_edit`, `can_delete`)

## Views Protection
- `book_list` → requires `can_view`
- `book_create` → requires `can_create`
- `book_edit` → requires `can_edit`
- `book_delete` → requires `can_delete`

## Testing
1. Create users with `python manage.py createsuperuser` or in Admin.
2. Assign users to groups (Viewers, Editors, Admins).
3. Log in as each user and test permissions.

## 🔒 HTTPS & Security Settings

This project enforces HTTPS for all traffic and applies several security best practices:

- **SECURE_SSL_REDIRECT = True** → Redirects all HTTP requests to HTTPS
- **HSTS (31536000s)** → Browsers always connect via HTTPS for one year
- **SESSION_COOKIE_SECURE = True** → Session cookies only sent over HTTPS
- **CSRF_COOKIE_SECURE = True** → CSRF cookies only sent over HTTPS
- **X_FRAME_OPTIONS = DENY** → Prevents clickjacking
- **SECURE_CONTENT_TYPE_NOSNIFF = True** → Prevents MIME type sniffing
- **SECURE_BROWSER_XSS_FILTER = True** → Enables browser XSS protection

### Deployment
- Configured web server (e.g., Nginx) with SSL/TLS certificates
- HTTP requests are redirected to HTTPS
- Certificates managed via Let's Encrypt
