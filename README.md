# Recipe API Project

This project was developed as part of an API Development Assessment. It involves:
- Parsing a large JSON file of recipes
- Storing the data in MySQL
- Building RESTful APIs using Django REST Framework
- Creating a frontend UI using Bootstrap 5

---

## 🚀 Tech Stack

- **Backend**: Django 5 + Django REST Framework
- **Database**: MySQL (PyMySQL connector)
- **Frontend**: HTML + Bootstrap 5 + JavaScript
- **Language**: Python 3.14
- **JSON Handling**: Raw and cleaned JSON file parser

---

## 🛠️ Project Setup

### 1. Clone the repo
```bash
git clone https://github.com/your-username/recipe-api-project.git
cd recipe-api-project
````

### 2. Setup Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Create a MySQL database and update `backend/recipe_project/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Load Recipe Data

```bash
python manage.py loaddata recipes_fixed.json
```

### 7. Start Server

```bash
python manage.py runserver
```

---

## 🌐 API Documentation

### ✅ API 1: Get All Recipes (Paginated & Sorted)

**URL**: `/api/recipes/`
**Method**: `GET`

#### Query Parameters:

| Parameter | Description                                                 |
| --------- | ----------------------------------------------------------- |
| `page`    | Page number (default = 1)                                   |
| `limit`   | Recipes per page (default = 10)                             |
| `sort_by` | Field to sort: `rating`, `title`, `prep_time`, `total_time` |
| `order`   | `asc` (default) or `desc`                                   |

#### Example:

```
/api/recipes/?page=2&limit=5&sort_by=rating&order=desc
```

#### Response:

```json
{
  "status": "success",
  "data": [ ... ],
  "pagination": {
    "total_pages": 100,
    "current_page": 2,
    "total_recipes": 1000
  }
}
```

---

### ✅ API 2: Search + Filter + Sort + Pagination

**URL**: `/api/recipes/search/`
**Method**: `GET`

#### Query Parameters:

| Parameter        | Description                                 |
| ---------------- | ------------------------------------------- |
| `search`         | Search title/description                    |
| `rating__gte`    | Minimum rating                              |
| `prep_time__lte` | Max preparation time                        |
| `cuisine`        | Exact cuisine match                         |
| `ordering`       | Field: `rating`, `title`, `prep_time`, etc. |
| `page`           | Page number                                 |
| `limit`          | Recipes per page                            |

#### Example:

```
/api/recipes/search/?search=chicken&rating__gte=3&ordering=-rating&page=1
```

#### Response (default DRF style):

```json
{
  "count": 500,
  "next": "...",
  "previous": null,
  "results": [ ... ]
}
```

---

## 💻 Frontend

* Static HTML: `frontend/index.html`
* Powered by Bootstrap 5
* Features:

  * Filter by rating
  * Search by title/description
  * Sort by rating/title
  * Paginated navigation like: `<< 1 2 3 ... >>`

To open the frontend:

1. Run Django server: `python manage.py runserver`
2. Open `frontend/index.html` in browser

   * Or use VS Code "Live Server"

---

## 📂 Files Included

```
recipe-api-project/
├── backend/
│   ├── manage.py, settings.py, views.py, urls.py
├── frontend/
│   └── index.html
├── fix_json.py              # Cleans the raw recipe JSON
├── US_recipes_null.json     # Raw recipe data
├── recipes_fixed.json       # Cleaned JSON
├── requirements.txt
├── README.md
```

---

## ⚠️ Challenges Faced

| Challenge                              | Solution                                                           |
| -------------------------------------- | ------------------------------------------------------------------ |
| JSON file had invalid format           | Wrote `fix_json.py` to clean and convert to valid JSON             |
| NaN/null values in rating/prep\_time   | Handled and stored as `NULL` in DB                                 |
| CORS errors in frontend                | Used `django-cors-headers` and enabled `CORS_ALLOW_ALL_ORIGINS`    |
| Pagination was slow                    | Added DRF `PageNumberPagination` with limit override               |
| Filtering needed multiple query params | Used `django-filter` and `SearchFilter` properly                   |
| Required 2 separate APIs               | Split into `/recipes/` and `/recipes/search/` with different logic |

---


