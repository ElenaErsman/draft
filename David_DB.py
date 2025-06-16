import sys
print("Current Python interpreter:", sys.executable)
from suds.client import Client


def setup_david_client():
    """
    Set up and return a DAVID Web Service client.
    
    Returns:
        Client: A configured DAVID Web Service client
    """
    try:
        # DAVID Web Service URL
        url = "https://david.ncifcrf.gov/webservice/services/DAVIDWebService?wsdl"
        
        # Create the client
        client = Client(url)
        
        email = "a01403527@unet.univie.ac.at"
        # Authenticate with your email address
        auth_response = client.service.authenticate(email)
        print(f"Authentication response: {auth_response}")
        
        return client
    except Exception as e:
        print(f"Error setting up DAVID client: {str(e)}")
        return None

client = setup_david_client()

if client is None:
    print("DAVID client setup failed")
else:
    print("DAVID client setup successful")
    