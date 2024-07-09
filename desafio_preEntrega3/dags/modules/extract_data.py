from modules.data_from_api import exchange_rate_data
from parameters import API_URL

def extract_data(API_URL):
    data = exchange_rate_data(API_URL)
    return data

# from modules.data_from_api import exchange_rate_data
# from parameters import API_URL

# def extract_data():
#     data = exchange_rate_data(API_URL)
#     if data:
#         with open('/tmp/extracted_data.json', 'w') as f:
#             json.dump(data, f)
#     return data
