import csv
from django.core.mail import send_mail
from django.shortcuts import render
# Create your views here.
def send_emails(request):
    csv_file_path=r'D:\2-2\PFSD\pythonProject\djangoprojects\TTM\static\mailfile.csv'
    with open(csv_file_path,'r') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            recipient_email=row['email']
            subject='Hello KLUian'
            message_body='Hey, Welcome to PFSD Class, Hope u have a great time with python'
            send_mail(
                subject,
                message_body,
                '2200030912cseh@gmail.com',
                [recipient_email],
                fail_silently=False,
            )
            print(f'Sent email to {recipient_email}')
    return render(request, 'Emails_sent_successfully.html')