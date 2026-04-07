import os
import requests

def secure_api_request():
    """
    Demonstrates secure and responsible API usage with proper authentication
    and error handling.
    """
    # Retrieve API key from environment variable
    api_key = os.getenv('API_KEY')
    
    if not api_key:
        print("Error: API_KEY environment variable not set")
        return
    
    # Define the API endpoint
    url = "https://api.example.com/data"
    
    # Prepare headers with Bearer token authentication
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        # Send GET request
        response = requests.get(url, headers=headers, timeout=10)
        
        # Handle status codes
        if response.status_code == 200:
            print("Success:")
            print(response.json())
        elif response.status_code == 429:
            print("Rate limit reached. Try again later.")
        else:
            print(f"Request failed with status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

if __name__ == "__main__":
    secure_api_request()