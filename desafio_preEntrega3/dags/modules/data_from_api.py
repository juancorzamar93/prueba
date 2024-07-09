    
import requests
from parameters import API_KEY

def exchange_rate_data(api_url):
    headers = {"apikey": API_KEY}
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud a la API: {e}")
        return None
