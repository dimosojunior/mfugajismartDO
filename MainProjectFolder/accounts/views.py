from django.shortcuts import render,redirect


# Create your views here.
from django.shortcuts import render,get_object_or_404
from App.serializers import *
from App.models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages


#REST FRAMEWORK
from rest_framework import status
from rest_framework.response import Response

#---------------------FUNCTION VIEW-------------------------
from rest_framework.decorators import api_view

#------------------------CLASS BASED VIEW-------------------
from rest_framework.views import APIView


#------------------------GENERIC VIEWs-------------------
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


#------------------------ VIEW SETS-------------------
from rest_framework.viewsets import ModelViewSet


#------FILTERS, SEARCH AND ORDERING
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter,OrderingFilter

#------PAGINATION-------------
from rest_framework.pagination import PageNumberPagination




#----------------CREATING A CART------------------------
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from App.serializers import *
from drf_yasg.utils import swagger_auto_schema

from rest_framework import generics,status
from rest_framework.decorators import api_view

# Create your views here.

# class UserView(APIView):

#   def get(self,request, format=None):
#       return Response("User Account View", status=200)

#   def post(self,request, format=None):

#       return Response("Creating User", status=200)


from django.core.mail import send_mail
from django.conf import settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# class RegistrationView(generics.CreateAPIView):
#     queryset = MyUser.objects.all()
#     serializer_class = DjangoReactUserSerializer
#     permission_classes = (permissions.AllowAny,)

# class ReactLoginView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = DjangoReactUserSerializer
    
#     def create(self, request, *args, **kwargs):
#         user = self.get_object()
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authtoken.models import Token






import os

from drf_yasg.utils import swagger_auto_schema

from rest_framework import generics,status
from rest_framework.decorators import api_view
from django.db.models import Sum
from django.db import transaction

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))



import requests
from requests.auth import HTTPBasicAuth  
import requests
from django.http import JsonResponse
#from beem.sms import BeemSms  # Correct import

#from BeemAfrica import Authorize, AirTime, OTP, SMS
from django.utils.timezone import now

#------------FOR TWILIO
from twilio.rest import Client
from dotenv import load_dotenv
import os

import requests

import base64
import requests

# Load environment variables
load_dotenv()






def send_sms(phone_number, message):
    """
    Sends an SMS using Beem Africa API.
    
    :param phone_number: The recipient's phone number in international format (e.g., +255XXXXXXXXX)
    :param message: The message to send
    """
    url = os.getenv("BEEM_ACCOUNT_URL")
    api_key = os.getenv("BEEM_ACCOUNT_API_KEY")  # Replace with your Beem Africa API key
    secret_key = os.getenv("BEEM_ACCOUNT_SECRET_KEY")  # Replace with your Beem Africa secret key
    sender_id = os.getenv("BEEM_ACCOUNT_SENDER_ID")  # Replace with your approved Sender Name

    # Encode API key and secret key in base64
    auth_string = f"{api_key}:{secret_key}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {auth_base64}"
    }
    
    payload = {
        "source_addr": sender_id,
        "encoding": 0,
        "schedule_time": "",
        "recipients": [{"recipient_id": 1, "dest_addr": phone_number}],
        "message": message
    }

    try:
        response = requests.post(url, json=payload, headers=headers)

        # Debugging: Print response details
        print(f"sms sends to {phone_number}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")

        
        response.raise_for_status()  # Raise an error for HTTP codes 4XX/5XX
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending SMS: {e}")
        return None












#----------------HIZI NI KWA AJILI YA APIS ------------------------------
# class RegistrationView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data.get('email')
#             password = serializer.validated_data.get('password')
#             username = serializer.validated_data.get('username')
#             phone = serializer.validated_data.get('phone')
#             # last_name = serializer.validated_data.get('last_name')
            
#             if MyUser.objects.filter(email=email).exists():
#                 return Response({'error': 'email already exists'}, status=status.HTTP_400_BAD_REQUEST)

#             if MyUser.objects.filter(username=username).exists():
#                 return Response({'error': 'username already exists'}, status=status.HTTP_400_BAD_REQUEST)

#             # if MyUser.objects.filter(phone=phone).exists():
#             #     return Response({'error': 'Namba ya simu uliyotumia tayari ipo'}, status=status.HTTP_400_BAD_REQUEST)
            

#             user = MyUser.objects.create_user(email=email, password=password, username=username, phone=phone)
#             if user:
#                 token, created = Token.objects.get_or_create(user=user)
#                 return Response({'token': token.key}, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({'error': 'Registration failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            username = serializer.validated_data.get('username')
            phone = serializer.validated_data.get('phone')
            expo_push_token = request.data.get('expo_push_token')  # Get Expo push token from request

            Mkoa_id = request.data.get('Mkoa')

            # Check if email or username already exists
            if MyUser.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
            if MyUser.objects.filter(username=username).exists():
                return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

            Mkoa = None
            if Mkoa_id:
                try:
                    Mkoa = Mikoa.objects.get(id=Mkoa_id)
                except Mikoa.DoesNotExist:
                    return Response({'error': 'Invalid Mkoa ID'}, status=status.HTTP_400_BAD_REQUEST)


            # Create user
            user = MyUser.objects.create_user(
                email=email, 
                password=password, 
                username=username, 
                phone=phone,
                Mkoa=Mkoa,
                expo_push_token=expo_push_token  # Save Expo push token
            )
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Registration failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):

        #kupata informations za user anayejaribu kuaupdate informations zake ili
        #kuziatach kwenye email kwenda kwa admin
        user = request.user
        username = request.user.username
        email = request.user.email
        phone = request.user.phone
        link = "https://mfugajismart.net/MfugajiSmart/"
        myemail = "nemoomary3@gmail.com"

        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            # Update related DukaLako instances
            DukaLako.objects.filter(username=username).update(
                username=user.username,
                email=user.email,
                phone=user.phone,
                Location=user.Location,
                company_name=user.company_name,
                profile_image=user.profile_image,
                LevelImage=user.LevelImage,
                UserRole=user.Role.Role,
                expo_push_token=user.expo_push_token

            )

            # Update related KumbushoLaChanjo instances
            KumbushoLaChanjo.objects.filter(username=username).update(
                username=user.username,
                email=user.email,
                phone=user.phone,
                Location=user.Location
                
            )

            # Update related KumbushoLaUatamiajiWaMayai instances
            KumbushoLaUatamiajiWaMayai.objects.filter(username=username).update(
                username=user.username,
                email=user.email,
                phone=user.phone,
                Location=user.Location
                
            )


            # Update related KumbushoUsafishajiBanda instances
            KumbushoUsafishajiBanda.objects.filter(username=username).update(
                username=user.username,
                email=user.email,
                phone=user.phone,
                Location=user.Location
                
            )


            ChatMessage.objects.filter(sender=username).update(
                sender=user.username,
                SenderEmail=user.email,
                SenderPhone=user.phone,
                SenderWilaya=user.Location,
                SenderImage=user.profile_image
                
            )

            #----Email Sent to Admin

            subject = "Mfugaji Smart"
            message = f"Hello Admin, Mtumiaji mwenye jina: {username} na mwenye email: {email}, simu namba: {phone} amefanya mabadiliko kwenye taarifa zake za awali. \n \n Hivyo unapaswa kuhakiki taarifa zake kupitia link hapo chini. \n \n {link}"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [myemail]

            

            send_mail(subject, message, from_email, recipient_list, fail_silently=True)


            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








class ReactLoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)





class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            Token.objects.filter(user=user).delete()
            return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)





class UserDataView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        # Assuming you have a serializer for User data
        serializer = UserDataSerializer(user)
        return Response(serializer.data)






class SendOTPView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = MyUser.objects.get(email=email)
            except MyUser.DoesNotExist:
                return Response({'error': 'Mtumiaji mwenye email hii teyari yupo.'}, status=status.HTTP_400_BAD_REQUEST)

            otp_instance = OTP.objects.create(user=user)

            subject = "Mfugaji Smart"
            message = f"OTP codes zako kutoka Mfugaji Smart \n \n {otp_instance.otp}"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)
            
            phone = user.phone.lstrip('0')  
            phone_number = f"255{phone}"
            try:
                sms_response = send_sms(phone_number, f"Hello {user.username}, {message}")
                if sms_response:
                    print(f"SMS sent successfully to {user.username}.")
                else:
                    print(f"Failed to send SMS to {user.username}.")
            except Exception as e:
                print(f"Error during SMS sending to {user.username}: {e}")

                
            print(f"OTP : {otp_instance.otp}")

            return Response({'message': 'OTP codes zimetumwa kwenye email yako.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VerifyOTPView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Umefanikiwa kubadilisha password yako kikamilifu'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)