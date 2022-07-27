# WheatKernel
Wheat Kernel Classification Machine Learning Projects

### Project Structure for Django Frameworks

```
├── docker-compose.yml
├── nginx
│   ├── Dockerfile
│   └── sites-enabled
│       └── django_project
├── production.yml
└── web
    ├── Dockerfile
    ├── docker_django
    │   ├── __init__.py
    │   ├── apps
    │   │   ├── __init__.py
    │   │   └── todo
    │   │       ├── __init__.py
    │   │       ├── admin.py
    │   │       ├── models.py
    │   │       ├── templates
    │   │       │   ├── _base.html
    │   │       │   └── home.html
    │   │       ├── tests.py
    │   │       ├── urls.py
    │   │       └── views.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── requirements.txt
    └── static
        └── main.css
```
### Machine Learnings Project Structure:
```
parent dir
    |
    |--- app.py
    |--- Dockerfile
    |--- templates
    |         |--- static
    |               |--- css
    |               |--- js
    |               |--- media
    |                       |--- images
    |                       |--- videos
    |--- project
    |       |--- configuration
    |       |           |--- configured.py
    |       |--- constants
    |       |         |--- constant.py
    |       |--- utils
    |       |      |--- utils.py
    |       |--- components
    |       |         |--- Dataingestion
    |       |         |--- DataValidation
    |       |         |--- Datatransformation
    |       |         |--- Model Training
    |       |         |--- Model Evaluating
    |       |         |--- Model Pusher
    |       |--- ModelFactory
    |       |         |--- ModelFactory     
    |       |         |--- ModelEstimator 
    |       |         |--- ModelPredictor
    |       |--- pipeline          
    |       |       |--- pipeline.py 
    |       |--- entity        
    |       |       |--- configuration entity  
    |       |       |--- artifact entity 
    |       |--- Exception
    |       |         |--- exception.py 
    |       |--- Logger
    |              |--- logging.py
    |--- saved_models
    |--- config_files
    |--- logs_fils
    |--- Procfile
    |--- requirments.txt
    |--- practice.py
    |--- .flaskenv
    |--- .gitignore
    |--- .dockerignore
    |--- .env
```