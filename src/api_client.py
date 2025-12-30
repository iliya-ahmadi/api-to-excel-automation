import requests

def fetch_products(api_url: str) -> list:
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e :
        print(f'API error: {e}')
        return []
            
