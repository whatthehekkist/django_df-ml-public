# How to run in localhost




# venv
- delete the hidden directory `.venv` 
- `setting -> python interpreter -> add local interpreter`
  - [success] your terminal will look like `(.venv) C:\Users\<USER_NAME>\<PATH>\django_df-ml-public>`
  - [if fail] in powershell, `.venv\Scripts\activate`
- installation
```python
pip install django~=4.0 django-bootstrap4 bootstrap4 pillow psycopg2 psycopg2-binary postgre binary sqlalchemy pandas
```
# postgres data sourcing
unzip `postgres-dump.zip` and in pgadmin4: 
- create each table using `.sql` file
- import `.csv` accordingly

# chatbot
similarity(pg_trgm): install `CREATE EXTENSION pg_trgm;` in *pgadmin4*

# run server
python manage.py runserver

# if doing from scratch
- init project
  - `django-admin startproject config .`
- create app (folder)
  - python manage.py startapp [app_name]
- migration
  - python manage.py makemigrations 
  - python manage.py migrate
- init migration (optional)
  - python manage.py migrate --fake account zero
- postgres superuser setting (optional)
  - `python manage.py createsuperuser`

