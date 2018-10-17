# conference-site

This website for a ficticious conference was developed using a Django backend as part of a Web and Database applications course.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for viewing, development, and testing purposes.

### Prerequisites

Must have Python and Django installed:

For Python, visit: 

https://www.python.org/downloads/

After installing Python, install Django via the command line using:
```
pip install django
```

### Installing

A step by step series of examples that tell you how to get a development env running
  1. download the conference-site-django project folder
  2. open the command line and cd to the project root folder:
  ```
  cd <PATH>/conference-site-django
  ```
  3. Run the Django development server: 
  ```
  python manage.py runserver
  ```
  This should give an output similar to the following:
  ```
  Performing system checks...

  System check identified no issues (0 silenced).
  <DATE> - <TIME>
  Django version <VERSION>, using settings 'conference-site-django.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.
  ```
  4. navigate browser to web address displayed in above step:
  ```
  http://127.0.0.1:8000/
  ```
  5. When done, quit the server using CONTROL-C at the command line
