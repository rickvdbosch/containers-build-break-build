import os
import requests

# Set the API endpoint
API_URL = "https://bootcamp25.azurewebsites.net/get-letter"

# Set the headers for each environment
HEADERS = {
    "local": {
        "X-Source": "local",
        "X-Secret": "local-secret-value"
    },
    "aci": {
        "X-Source": "aci",
        "X-Secret": "aci-secret-value"
    },
    "containerapps": {
        "X-Source": "containerapps",
        "X-Secret": "containerapps-secret-value"
    }
}

def get_letter(environment):
    # Send a request to the API with the appropriate headers
    headers = HEADERS.get(environment)
    if not headers:
        print(f"Invalid environment: {environment}")
        return

    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()
        data = response.json()
        print(f"Letter for {environment}: {data.get('letter')}")
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving letter for {environment}: {e}")

if __name__ == "__main__":
    # Get the environment from the ENVIRONMENT variable, defaulting to "local" if not set
    environment = os.getenv("ENVIRONMENT", "local")
    print(f"DEBUG: Environment variable set to: {environment}")  # Debugging line
    get_letter(environment)
