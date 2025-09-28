# Advanced API Project – Custom and Generic Views

This module implements CRUD operations for the `Book` model using Django REST Framework’s generic views.

## Endpoints
- GET `/api/books/` → List all books
- GET `/api/books/<id>/` → Retrieve book by ID
- POST `/api/books/create/` → Create new book (authenticated only)
- PUT/PATCH `/api/books/<id>/update/` → Update book (authenticated only)
- DELETE `/api/books/<id>/delete/` → Delete book (authenticated only)

## Permissions
- Read operations → Open to all
- Write operations → Restricted to authenticated users
- Custom permissions available (e.g., `IsOwnerOrReadOnly`).
