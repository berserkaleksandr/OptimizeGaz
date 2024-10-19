import numpy as np
from gas_tracker import get_historical_gas_data

def predict_optimal_time():
    data = get_historical_gas_data()
    
    gas_prices = [entry['price'] for entry in data]
    optimal_price_index = np.argmin(gas_prices) 
    
    optimal_time = data[optimal_price_index]['timestamp']
    return optimal_time

def recommend_time_for_transaction():
    try:
        optimal_time = predict_optimal_time()
        print(f"Time: {optimal_time}")
    except Exception as e:
        print(f"Error: {e}")
