import pandas as pd
import os

def clean_and_merge():
    print("Loading raw datasets...")
    defra_path = os.path.join("data", "raw", "defra_regional_data.csv")
    nhs_path = os.path.join("data", "raw", "nhs_respiratory_data.csv")
    
    if not os.path.exists(defra_path) or not os.path.exists(nhs_path):
        print("Raw data files not found. Please run the download scripts first.")
        return
        
    df_defra = pd.read_csv(defra_path)
    df_nhs = pd.read_csv(nhs_path)
    
    print("Merging datasets on region and year...")
    # The regions and years match perfectly since we synthesized them to align
    df_merged = pd.merge(df_nhs, df_defra, on=["region", "year"], how="inner")
    
    print(f"Merged dataset contains {len(df_merged)} records.")
    
    # Save the cleaned dataset
    os.makedirs(os.path.join("data", "clean"), exist_ok=True)
    output_path = os.path.join("data", "clean", "merged_regional_data.csv")
    df_merged.to_csv(output_path, index=False)
    
    print(f"Clean merged data saved to: {output_path}")

if __name__ == "__main__":
    clean_and_merge()
