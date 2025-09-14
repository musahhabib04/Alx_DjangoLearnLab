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
