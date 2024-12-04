# django_df-ml-public
- data framing and movie recommendation (svd, nmf, mf) tutorial using batch movie data
  - chatbot | video
  - recommendation
  - chart visualization

[![login/signup](https://github.com/user-attachments/assets/3be7a872-aeed-41e5-b5a9-c7837a27fa23)](https://www.youtube.com/watch?v=BaqTMrfTRPE)

[![employees crud](https://github.com/user-attachments/assets/a34c0c14-6934-4abb-8077-5448989aacba)](https://www.youtube.com/shorts/F4vZxrI2nDc)

[![chatbot](https://github.com/user-attachments/assets/e7394266-5831-4ee7-8e73-b6d350114e33)](https://www.youtube.com/shorts/1PPDPNJcwkg)

[![recommendation](https://github.com/user-attachments/assets/3b97c2ce-ed5c-4e66-b0f9-e518b28ee4ec)](https://www.youtube.com/shorts/JN8ZsU7MMTA)

[![chart visualization](https://github.com/user-attachments/assets/ba4ea1da-fa07-4693-a404-6ebf6287fbcc)](https://www.youtube.com/shorts/lZxrXENAO7c)


<link rel="stylesheet" href="https://cdn.statically.io/gh/mdlavin/bootstrap-carousel-standalone/292657fcb31f3c21cc7147816ab66e2191466f67/css/bootstrap.css" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-1.9.1.min.js"  crossorigin="anonymous"></script>
<script src="https://cdn.statically.io/gh/mdlavin/bootstrap-carousel-standalone/292657fcb31f3c21cc7147816ab66e2191466f67/js/bootstrap.js" crossorigin="anonymous"></script>

<div id="myCarousel" class="carousel slide" data-ride="carousel" data-interval="false" style="text-align:center;">
    <!-- Indicators -->
    <ol class="carousel-indicators">
      <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
      <li data-target="#myCarousel" data-slide-to="1"></li>
    </ol>
    <!-- Wrapper for slides -->
    <div class="carousel-inner">
      <div class="item active">
        <img style="box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); margin: 0 auto;" src="https://github.com/user-attachments/assets/b920cfe4-d23b-4d9c-9c76-c19e7a7b3eb8" alt="System architecture"/>
        <span style="color:darkgrey; font-size:small;">System architecture</span>
      </div>
      <div class="item">
        <img style="box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); margin: 0 auto;" src="https://github.com/user-attachments/assets/36981def-c432-4bd8-b124-eded1b6edde8" alt="dash board"/>
        <span style="color:darkgrey; font-size:small;">dash board</span>
      </div>
      <div class="item">
        <img style="box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); margin: 0 auto;" src="https://github.com/user-attachments/assets/ef750614-0e05-48b5-bebf-a532b1f9606b" alt="Engine Flow Chart"/>
        <span style="color:darkgrey; font-size:small;">Engine Flow Chart</span>
      </div>
      <div class="item">
        <img style="box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); margin: 0 auto;" src="https://github.com/user-attachments/assets/4fa0491a-19fa-4031-9ed6-1b5b114d889b" alt="Thread Flow Chart"/>
        <span style="color:darkgrey; font-size:small;">Thread Flow Chart</span>
      </div>
      <div class="item">
        <img style="box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); margin: 0 auto;" src="https://github.com/user-attachments/assets/4dbeeb29-6d0b-4e55-ad91-5c41a6a58c64" alt="class-diagram"/>
        <span style="color:darkgrey; font-size:small;">Class diagram</span>
      </div>
    </div>
    <!-- Left and right controls -->
    <a class="left carousel-control" href="#myCarousel" data-slide="prev">
      <span class="glyphicon glyphicon-chevron-left"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="right carousel-control" href="#myCarousel" data-slide="next">
      <span class="glyphicon glyphicon-chevron-right"></span>
      <span class="sr-only">Next</span>
    </a>
</div>

# env
- pycharm community
- postgres
- pgadmin4

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

