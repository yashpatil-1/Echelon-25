import os
from azure.communication.networktraversal import CommunicationRelayClient
from azure.identity import DefaultAzureCredential
from azure.communication.identity import CommunicationIdentityClient

try:
    print("Azure Communication Services - Access Relay Configuration  Quickstart")
    # Quickstart code goes here
    # You can find your endpoint and access token from your resource in the Azure Portal
    connection_string = "endpoint=https://com-service1.unitedstates.communication.azure.com/;accesskey=BhFDRXGYbh7S5bjihU+rySt5EYa98PB+gUIq5RHHF5Ow8VBHhXLxB1872G6fcskbZKmsasPDajq4s2fDBp9ZRQ=="
    endpoint = "https://com-service1.unitedstates.communication.azure.com/"

    # To use Azure Active Directory Authentication (DefaultAzureCredential) make sure to have
    # AZURE_TENANT_ID, AZURE_CLIENT_ID and AZURE_CLIENT_SECRET as env variables.
    # We also need Identity client to get a User Identifier
    identity_client = CommunicationIdentityClient(endpoint, DefaultAzureCredential())
    relay_client = CommunicationRelayClient(endpoint, DefaultAzureCredential())

    #You can also authenticate using your connection string
    identity_client = CommunicationIdentityClient.from_connection_string(connection_string)
    relay_client = CommunicationRelayClient.from_connection_string(connection_string)
except Exception as ex:
    print("Exception:")
    print(ex)

user = identity_client.create_user()
relay_configuration = relay_client.get_relay_configuration(user=user)

for iceServer in relay_configuration.ice_servers:
    assert iceServer.username is not None
    print('Username: ' + iceServer.username)

    assert iceServer.credential is not None
    print('Credential: ' + iceServer.credential)
    
    assert iceServer.urls is not None
    for url in iceServer.urls:
        print('Url:' + url)