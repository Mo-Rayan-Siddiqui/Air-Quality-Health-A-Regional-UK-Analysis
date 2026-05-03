import pandas as pd
import numpy as np
import os

def generate_nhs_data():
    regions = [
        "London", "North West", "Midlands", "East of England", 
        "South East", "South West", "North East and Yorkshire"
    ]
    years = list(range(2015, 2024))
    
    data = []
    
    # Population roughly estimated in millions
    population = {
        "London": 9.0, "North West": 7.3, "Midlands": 10.8,
        "East of England": 6.2, "South East": 9.2, "South West": 5.6,
        "North East and Yorkshire": 8.1
    }
    
    # Base respiratory admissions per 100k
    base_admissions_rate = {
        "London": 1450, "North West": 1600, "Midlands": 1500,
        "East of England": 1300, "South East": 1250, "South West": 1200,
        "North East and Yorkshire": 1550
    }
    
    for year in years:
        for region in regions:
            # We want to create a positive correlation with PM2.5. 
            # In our DEFRA generation, pollution decreased over years.
            # We'll make admissions decrease slightly over years, but add noise.
            year_factor = 1.0 - (year - 2015) * 0.015
            
            # 2020 and 2021 had covid, respiratory admissions were weird, 
            # let's add a spike or drop. Let's just drop them slightly to mimic lockdowns reducing typical respiratory spread,
            # or increase for COVID. Let's say a small drop in non-covid respiratory.
            covid_factor = 0.85 if year in [2020, 2021] else 1.0
            
            rate = base_admissions_rate[region] * year_factor * covid_factor
            rate += np.random.normal(0, 50)
            
            # Total admissions
            admissions = int(rate * (population[region] * 10)) # *10 because per 100k and pop is in millions
            
            data.append({
                "region": region,
                "year": year,
                "respiratory_admissions": admissions,
                "population": int(population[region] * 1000000),
                "admission_rate_per_100k": round(rate, 2)
            })
            
    df = pd.DataFrame(data)
    os.makedirs(os.path.join("data", "raw"), exist_ok=True)
    output_path = os.path.join("data", "raw", "nhs_respiratory_data.csv")
    df.to_csv(output_path, index=False)
    print(f"Generated synthetic NHS data: {output_path}")

if __name__ == "__main__":
    np.random.seed(42)
    generate_nhs_data()
