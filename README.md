# NSITHackathon
A/B Testing

This is a framework implemented in python for A/B testing of verions of websites.

Key features:
1. Compare as many versions of a website as the user wants to (Multivariate). User can provide the number of versions to be tested at runtime.

2. Time period for which the analysis will be done can be provided by the user at runtime.
 
3. Traffic can be multivariably splitted by providing a list of comma separated percentages within a single line.
 
4. Once a version is declared better than other versions it is automatically used as the default version and all the traffic is routed to that version now.


Steps to use this framework.

1. You need django installed in your system to run this framework.
 
2. You will need to install python and pip to be able to install django.
 
3. Run pip install django in linux/mac to install the django system at runtime.
 
4. You will need to setup a mysql database to do be able to use this framework.
 
5. Install mysql through the terminal and then make a database named "hackathon".
 
6. Now go to the the directory where manage.py file is present and run python manage.py makemigrations and then python manage.py migrate.

7. Once the database has been set up and synced with django the framework is ready to be used.

8. Now run django manage.py createsuperuser and create a superuser.
 
9. Finally run the python manage.py runserver to run the server at 127.0.0.1:8000 and the fraemwork is ready to be used :)
