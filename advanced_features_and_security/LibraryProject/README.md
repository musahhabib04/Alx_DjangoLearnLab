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

## Security Enhancements

This project applies Django security best practices:

- `DEBUG = False` in production
- `SECURE_BROWSER_XSS_FILTER = True`
- `X_FRAME_OPTIONS = "DENY"`
- `SECURE_CONTENT_TYPE_NOSNIFF = True`
- `CSRF_COOKIE_SECURE = True` and `SESSION_COOKIE_SECURE = True` (cookies sent only over HTTPS)
- `SECURE_HSTS_*` settings for strict HTTPS enforcement
- All forms include `{% csrf_token %}` to prevent CSRF
- ORM used for queries, preventing SQL injection
- Content Security Policy (CSP) enabled to block inline scripts and untrusted sources
