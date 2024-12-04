# django_df-ml-public
- data framing and movie recommendation (svd, nmf, mf) tutorial using batch movie data
- click the following images to see video

[![login/signup](https://github.com/user-attachments/assets/3be7a872-aeed-41e5-b5a9-c7837a27fa23)](https://www.youtube.com/watch?v=BaqTMrfTRPE)

[![employees crud](https://github.com/user-attachments/assets/a34c0c14-6934-4abb-8077-5448989aacba)](https://www.youtube.com/shorts/F4vZxrI2nDc)

[![chatbot](https://github.com/user-attachments/assets/e7394266-5831-4ee7-8e73-b6d350114e33)](https://www.youtube.com/shorts/1PPDPNJcwkg)

[![recommendation](https://github.com/user-attachments/assets/3b97c2ce-ed5c-4e66-b0f9-e518b28ee4ec)](https://www.youtube.com/shorts/JN8ZsU7MMTA)

[![chart visualization](https://github.com/user-attachments/assets/26efa633-93fd-4856-8fcf-1a9818b9b60d)](https://www.youtube.com/shorts/lZxrXENAO7c)

[//]: # ([![chart visualization]&#40;https://github.com/user-attachments/assets/ba4ea1da-fa07-4693-a404-6ebf6287fbcc&#41;]&#40;https://www.youtube.com/shorts/lZxrXENAO7c&#41;)

# How to run in localhost
- git clone `https://github.com/whatthehekkist/django_df-ml-public.git`

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
download and unzip [postgres-dump.zip](https://drive.google.com/file/d/1l3ngJ7TeubYSmN4B3iyhOWv0Ke8omBT8/view?usp=sharing) 
, and in pgadmin4: 
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

