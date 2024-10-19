import requests

def get_current_gas_price():
    url = "https://api.base.org/gasprice"
    response = requests.get(url)
    
    if response.status_code == 200:
        gas_data = response.json()
        return gas_data.get("standard", None)  
    else:
        raise Exception("Error")

def get_historical_gas_data():
    url = "https://api.base.org/gashistory"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error")
