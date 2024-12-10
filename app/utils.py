import pandas as pd  

def load_combined_data():  
    """Load combined solar farm data from CSV and ensure the 'Timestamp' is in datetime format."""  
    data = pd.read_csv("data/combined_solar_data.csv")
    data["Timestamp"] = pd.to_datetime(data["Timestamp"])  # Ensure Timestamp is in datetime format
    return data  

def generate_summary_statistics(data):  
    """Generate summary statistics grouped by country."""  
    return data.groupby("Country").describe()
