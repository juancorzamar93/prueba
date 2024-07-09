from modules.data_from_api import exchange_rate_data
from parameters import API_URL

def extract_data(API_URL):
    data = exchange_rate_data(API_URL)
    return data

