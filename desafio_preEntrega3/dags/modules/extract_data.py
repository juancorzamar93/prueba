
# from modules.data_from_api import exchange_rate_data

# def extract_data(api_url):
#     data = exchange_rate_data(api_url)
#     return data

from modules.data_from_api import exchange_rate_data
from parameters import API_URL

def extract_data():
    data = exchange_rate_data(API_URL)
    if data:
        with open('/tmp/extracted_data.json', 'w') as f:
            json.dump(data, f)
    return data
