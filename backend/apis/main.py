import os
import json

from google.auth.transport import requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.apps import meet_v2 as meet

def authorize() -> Credentials:
    """Ensure valid credentials for calling the Meet REST API."""
    CLIENT_SECRET_FILE = "./client_secret.json"
    credentials = None

    if os.path.exists('token.json'):
        credentials = Credentials.from_authorized_user_file('token.json')

    if credentials is None:
        flow = InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRET_FILE,
            scopes=[
                'https://www.googleapis.com/auth/meetings.space.created',
            ])
        flow.run_local_server(port=0)
        credentials = flow.credentials

    if credentials and credentials.expired:
        credentials.refresh(requests.Request())

    if credentials is not None:
        with open("token.json", "w") as f:
            f.write(credentials.to_json())

    return credentials

USER_CREDENTIALS = authorize()

#create meeting space
def create_space() -> meet.Space:
    """Create a meeting space."""
    client = meet.SpacesServiceClient(credentials=USER_CREDENTIALS)
    request = meet.CreateSpaceRequest()
    response = client.create_space(request=request)
    print(response)
    return response

def sample_end_active_conference():
    # Create a client
    client = meet.SpacesServiceClient(credentials=USER_CREDENTIALS)

    # Initialize request argument(s)
    request = meet.EndActiveConferenceRequest(
        name="name_value",
    )

    # Make the request
    client.end_active_conference(request=request)
#import asyncio
# async def sample_create_space():
#     # Create a client
#     client = meet.SpacesServiceAsyncClient()

#     # Initialize request argument(s)
#     request = meet.CreateSpaceRequest(
#     )

#     # Make the request
#     response = await client.create_space(request=request)

#     # Handle the response
#     print(response)
#     return response

meeting = create_space()
# asyncio.run(sample_create_space())

async def sample_list_recordings():
    # Create a client
    client = meet.ConferenceRecordsServiceAsyncClient()

    # Initialize request argument(s)
    request = meet.ListRecordingsRequest(
        parent="parent_value",
    )

    # Make the request
    page_result = client.list_recordings(request=request)

    # Handle the response
    async for response in page_result:
        print(response)


async def sample_get_recording():
    # Create a client
    client = meet.ConferenceRecordsServiceAsyncClient()

    # Initialize request argument(s)
    request = meet.GetRecordingRequest(
        name="name_value",
    )

    # Make the request
    response = await client.get_recording(request=request)

    # Handle the response
    print(response)


async def sample_list_transcripts():
    # Create a client
    client = meet.ConferenceRecordsServiceAsyncClient()

    # Initialize request argument(s)
    request = meet.ListTranscriptsRequest(
        parent="parent_value",
    )

    # Make the request
    page_result = client.list_transcripts(request=request)

    # Handle the response
    async for response in page_result:
        print(response)


async def sample_get_transcript():
    # Create a client
    client = meet.ConferenceRecordsServiceAsyncClient()

    # Initialize request argument(s)
    request = meet.GetTranscriptRequest(
        name="name_value",
    )

    # Make the request
    response = await client.get_transcript(request=request)

    # Handle the response
    print(response)


# WEB API VERSION
# Get meeting: https://meet.googleapis.com/v2/spaces/DOaEBZclZzQB