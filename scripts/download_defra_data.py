import pandas as pd
import numpy as np
import os

def generate_defra_data():
    regions = [
        "London", "North West", "Midlands", "East of England", 
        "South East", "South West", "North East and Yorkshire"
    ]
    years = list(range(2015, 2024))
    
    data = []
    
    # Base pollution levels roughly estimated
    base_pm25 = {
        "London": 12.5, "North West": 10.2, "Midlands": 10.8,
        "East of England": 9.5, "South East": 10.0, "South West": 8.0,
        "North East and Yorkshire": 9.8
    }
    
    for year in years:
        # Pollution slightly decreasing over years
        year_factor = 1.0 - (year - 2015) * 0.02
        
        for region in regions:
            # Adding some random noise
            noise = np.random.normal(0, 0.5)
            pm25 = base_pm25[region] * year_factor + noise
            no2 = pm25 * 2.5 + np.random.normal(0, 2)
            o3 = 60 - pm25 * 1.5 + np.random.normal(0, 3)
            
            data.append({
                "region": region,
                "year": year,
                "PM2.5": max(0, round(pm25, 2)),
                "NO2": max(0, round(no2, 2)),
                "O3": max(0, round(o3, 2))
            })
            
    df = pd.DataFrame(data)
    os.makedirs(os.path.join("data", "raw"), exist_ok=True)
    output_path = os.path.join("data", "raw", "defra_regional_data.csv")
    df.to_csv(output_path, index=False)
    print(f"Generated synthetic DEFRA data: {output_path}")

if __name__ == "__main__":
    np.random.seed(42)
    generate_defra_data()
