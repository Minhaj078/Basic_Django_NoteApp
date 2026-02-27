# NoteApp — Django Notes Manager

A clean, professional Django notes app with full CRUD, search, and working navigation.

## Features
- ✅ Create, Edit, Delete notes
- ✅ Live search by title or content
- ✅ Delete confirmation modal (no accidental deletions)
- ✅ Flash messages (success / error)
- ✅ Working navbar with dropdown and search
- ✅ About & Help pages
- ✅ Fully responsive (Bootstrap 5)

## Quick Start

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply migrations
python manage.py migrate

# 4. (Optional) Create an admin user
python manage.py createsuperuser

# 5. Run the development server
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser.

## Project Structure

```
NoteApp/
├── manage.py
├── requirements.txt
├── db.sqlite3              ← auto-created after migrate
├── NoteApp/                ← project config
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── notes/                  ← main app
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    ├── migrations/
    └── templates/
        ├── base.html
        ├── components/
        │   ├── navbar.html
        │   ├── footer.html
        │   └── messages.html
        └── notes/
            ├── home.html
            ├── edit_note.html
            ├── about.html
            └── help.html
```
