# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build

# # Define the scope
# SCOPES = ['https://www.googleapis.com/auth/calendar.events']

# # Create OAuth 2.0 flow
# flow = InstalledAppFlow.from_client_secrets_file(
#     'apis/client_secret_o_auth.json', SCOPES)

# # Run the local server to get the authorization code
# credentials = flow.run_local_server(port=0)

# # Save the credentials for later use
# with open('token.json', 'w') as token:
#     token.write(credentials.to_json())

# # Load credentials from the saved file
# creds = Credentials.from_authorized_user_file('token.json', SCOPES)



# Oauth flow
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from google_auth_oauthlib.flow import Flow
from django.contrib.auth.models import User
# from .models import UserToken
from rest_framework.permissions import IsAuthenticated
import os
import json
from rest_framework_simplejwt.tokens import RefreshToken

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # Only for local development

flow = Flow.from_client_secrets_file(
    'apis/client_secret_o_auth.json',
    scopes=['https://www.googleapis.com/auth/calendar.events'],
    redirect_uri='http://localhost:8000/oauth2callback'
)

class OAuth2InitView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        authorization_url, state = flow.authorization_url()
        request.session['state'] = state
        #keep track of the state
        print(authorization_url)
        #pass this to react front end
        return redirect('http://localhost:3000')
    
    def post(self, request):
        authorization_url, state = flow.authorization_url()
        user = request.user
        # request.session['state'] = state
        #keep track of the state
        print(authorization_url)
        #pass this to react front end
        return Response({'auth_url': authorization_url, 'state': state, 'user': request.user.pk})

class OAuth2CallbackView(APIView):
    def get(self, request):
        flow.fetch_token(authorization_response=request.build_absolute_uri())

        #compare the state
        if request.session['state'] != request.GET.get('state'):
            return Response({'error': 'State does not match!'}, status=400)

        credentials = flow.credentials
        user = request.user
        print(credentials)
        # Save the credentials to the database
        # user_token, created = UserToken.objects.get_or_create(user=user)
        # user_token.token = credentials.to_json()
        # user_token.save()

        return Response({'message': 'OAuth 2.0 authentication successful!'})
