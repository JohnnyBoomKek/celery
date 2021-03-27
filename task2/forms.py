from django.forms import *
from task2.tasks import send_review_email_task

class ReviewForm(Form):
    name = CharField( max_length=50, label='Firstname')
    email = EmailField(max_length=200)
    review = CharField()


    def send_email(self):
        send_review_email_task.delay(
            self.cleaned_data['name'], self.cleaned_data['email'], self.cleaned_data['review']
        )