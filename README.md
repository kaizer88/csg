CSG Candidate Skills Assessment

Requirements:
Python3, pip

Step to run project:

Clone to your computer directory
Create a virtual environment for it and activate it - cd to directory in the terminal and in macOS, I used python3 -m venv env and windows is python -m venv env
Install requirements.txt file buy running 'pip install -r requirements.txt'
I was using postgres, if you have one, create a database. my database is called 'csg'
Change your local_settings.py file to your settings, normally I do not add it to the project, it remains to gitignore file
Then you need to cd to directory where there is manage.py file under github
Run 'python manage.py migrate'
For the test create a user(teacher/admin) by running 'python manage.py createsuperuser'
Fill username, email and password on each user
Then you can run the app with the command 'python manage.py runserver'

About the app:

This app has a login feature where a user needs to login and add class names, students, and capture attendance. To login you use your username and password. 

After capturing all the features above you can go to reports and select which repot you want to generate.
All generated reports are pdfs.
