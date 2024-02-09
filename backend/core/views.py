from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserForm
from .serializers import UserFormSerializer
import smtplib
import ssl
from email.message import EmailMessage

def send_email(email):
    email_sender = 'akshayasalaskar12345@gmail.com'
    email_password = 'leug wffb kvoh tlls'
    email_receiver = email

    # Set the subject and body of the email
    subject = 'Conguralation'
    body = """
    Welcome and Congo for the joining!
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Log in and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(email_sender, email_password)
        smtp.send_message(em)  
        print("message sent")


class SubmitForm(APIView):
    def post(self, request):
        try:
            serializer = UserFormSerializer(data=request.data)
            if serializer.is_valid():
                send_email(request.data["email"])
                serializer.save()
                # Code to send email upon successful form submission
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetUser(APIView):
    def get(self, request, user_id):
        try:
            user = UserForm.objects.get(pk=user_id)
            serializer = UserFormSerializer(user)
            return Response(serializer.data)
        except UserForm.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
