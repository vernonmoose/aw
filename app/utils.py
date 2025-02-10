import random
import string
from django.core.mail import EmailMessage

class Email:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'], 
            body=data['email_body'],
            to=[data['to_email']],
        )
        email.send()

def generate_username(name):
    name = name.lower().replace(" ", "")
    random_number = random.randint(100, 999)
    random_letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(2))
    username = f"{name}{random_letters}{random_number}"
    return username