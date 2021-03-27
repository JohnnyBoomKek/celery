# Sending Emails with Django and Celery 
learning project with sole purpose of learning celery


About the project: 
    Integrating Django and Celery to have Django send emails through Celery


Getting started:
    #First things first you are going to need to install dependencies:
        - pip install -r requirements.txt
    #Install RabbitMQ (ubuntu linux)
            $sudo apt-get install rabbitmq-server

    #Create .env and change settings.py accordingly 
    for more info please reffer to https://docs.djangoproject.com/en/3.1/topics/email/

    #Run server 
        - python manage.py runserver
    
    #Run Celery
        - celery -A celeryproj worker -l info

    #Navigate to localhost:8000/reviews
    
    #That's it folks