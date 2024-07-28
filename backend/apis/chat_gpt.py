from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse
from google_auth_oauthlib.flow import Flow
import os
import jwt
import datetime
from datetime import timedelta
# Add your client secret JSON file path and the redirect URI
GOOGLE_OAUTH2_CLIENT_SECRETS_FILE = './client_secret.json'
GOOGLE_OAUTH2_SCOPES = ['https://www.googleapis.com/auth/calendar']
GOOGLE_OAUTH2_REDIRECT_URI = 'http://localhost:8000/oauth2callback/'

def index(request):
    return HttpResponse('<a href="/authorize/">Authorize with Google</a>')

def authorize(request):
    flow = Flow.from_client_secrets_file(
        GOOGLE_OAUTH2_CLIENT_SECRETS_FILE, scopes=GOOGLE_OAUTH2_SCOPES)

    flow.redirect_uri = GOOGLE_OAUTH2_REDIRECT_URI

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')

    # Create a JWT token with the state parameter
    jwt_token = jwt.encode({'state': state, 'exp': datetime.utcnow() + timedelta(minutes=10)}, settings.JWT_SECRET_KEY, algorithm='HS256')

    # Add the JWT token to the URL
    authorization_url_with_jwt = f"{authorization_url}&jwt_token={jwt_token}"

    return redirect(authorization_url_with_jwt)

    print(state)

    return redirect(authorization_url)

def oauth2callback(request):
    state = request.session['state']

    flow = Flow.from_client_secrets_file(
        GOOGLE_OAUTH2_CLIENT_SECRETS_FILE, scopes=GOOGLE_OAUTH2_SCOPES, state=state)
    flow.redirect_uri = GOOGLE_OAUTH2_REDIRECT_URI

    authorization_response = request.build_absolute_uri()
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials
    request.session['credentials'] = credentials_to_dict(credentials)

    return redirect(reverse('index'))

def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }
