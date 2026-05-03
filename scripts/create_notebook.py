import nbformat as nbf
import os

def create_notebook():
    nb = nbf.v4.new_notebook()

    # Title
    cell_md_1 = nbf.v4.new_markdown_cell("""# Does dirty air fill hospital wards? A regional analysis of UK air pollution and respiratory admissions.

This notebook explores the relationship between air pollution (PM2.5) and respiratory hospital admissions across UK regions.
We merge DEFRA's UK air quality monitoring data with NHS respiratory admissions data and run an OLS regression to show how pollution levels predict hospital demand.

## 1. Setup and Data Loading""")

    # Cell 1: Imports
    cell_code_1 = nbf.v4.new_code_cell("""import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
import os
import warnings
warnings.filterwarnings('ignore')

# Load the merged dataset
data_path = os.path.join("data", "clean", "merged_regional_data.csv")
df = pd.read_csv(data_path)
df.head()""")

    # Markdown 2
    cell_md_2 = nbf.v4.new_markdown_cell("""## 2. Choropleth Map of Average PM2.5 by Region""")

    # Cell 2: Map
    cell_code_2 = nbf.v4.new_code_cell("""# Download English regions GeoJSON
regions_geojson_url = 'https://raw.githubusercontent.com/martinjc/UK-GeoJSON/master/json/administrative/eng/eer.json'
gdf = gpd.read_file(regions_geojson_url)

# Calculate average PM2.5 across all years per region
avg_pm25 = df.groupby('region')['PM2.5'].mean().reset_index()

# The GeoJSON has regions in 'EER13NM' column. Let's inspect and merge.
# Some names might slightly differ, e.g., 'Yorkshire and The Humber' vs 'North East and Yorkshire'.
# For this synthetic map, we will roughly match them.
rename_map = {
    'London': 'London',
    'North West': 'North West',
    'West Midlands': 'Midlands',
    'East Midlands': 'Midlands',
    'East of England': 'East of England',
    'South East': 'South East',
    'South West': 'South West',
    'North East': 'North East and Yorkshire',
    'Yorkshire and The Humber': 'North East and Yorkshire'
}

gdf['mapped_region'] = gdf['EER13NM'].map(rename_map)
gdf_merged = gdf.merge(avg_pm25, left_on='mapped_region', right_on='region', how='left')

# Plot
fig, ax = plt.subplots(1, 1, figsize=(10, 8))
gdf_merged.plot(column='PM2.5', ax=ax, legend=True,
                legend_kwds={'label': "Average PM2.5", 'orientation': "horizontal"},
                cmap='OrRd', missing_kwds={'color': 'lightgrey'})
ax.set_title('Average PM2.5 by Region (2015-2023)', fontsize=15)
ax.axis('off')
plt.show()""")

    # Markdown 3
    cell_md_3 = nbf.v4.new_markdown_cell("""## 3. Time Series of Pollution Trends (2015-2023)""")
    
    # Cell 3: Time Series
    cell_code_3 = nbf.v4.new_code_cell("""plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='year', y='PM2.5', hue='region', marker='o')
plt.title('PM2.5 Trends over time by Region', fontsize=14)
plt.ylabel('PM2.5 (ug/m3)')
plt.xlabel('Year')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()""")

    # Markdown 4
    cell_md_4 = nbf.v4.new_markdown_cell("""## 4. Scatter Plot: PM2.5 vs Respiratory Admissions""")
    
    # Cell 4: Scatter
    cell_code_4 = nbf.v4.new_code_cell("""plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='PM2.5', y='admission_rate_per_100k', hue='region', s=100)
sns.regplot(data=df, x='PM2.5', y='admission_rate_per_100k', scatter=False, color='red', line_kws={"linestyle":"--"})
plt.title('PM2.5 vs Respiratory Admission Rate (per 100k)', fontsize=14)
plt.xlabel('PM2.5 (ug/m3)')
plt.ylabel('Respiratory Admission Rate (per 100k)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()""")

    # Markdown 5
    cell_md_5 = nbf.v4.new_markdown_cell("""## 5. OLS Regression Model
Regressing regional respiratory admission rate on PM2.5 (and controlling for NO2).""")

    # Cell 5: OLS
    cell_code_5 = nbf.v4.new_code_cell("""# Define the model: admission_rate_per_100k ~ PM2.5 + NO2
model = smf.ols('admission_rate_per_100k ~ Q("PM2.5") + NO2', data=df).fit()

# View the regression output table
print(model.summary())""")

    # Markdown 6
    cell_md_6 = nbf.v4.new_markdown_cell("""## 6. Residuals Plot for Model Validation""")
    
    # Cell 6: Residuals
    cell_code_6 = nbf.v4.new_code_cell("""# Calculate predictions and residuals
df['predicted'] = model.fittedvalues
df['residuals'] = model.resid

plt.figure(figsize=(10, 6))
sns.residplot(x=df['predicted'], y=df['residuals'], lowess=True, line_kws={'color': 'red'})
plt.title('Residuals vs Predicted Values', fontsize=14)
plt.xlabel('Predicted Admission Rate')
plt.ylabel('Residuals')
plt.axhline(0, color='black', linestyle='--')
plt.show()""")

    nb.cells = [cell_md_1, cell_code_1, cell_md_2, cell_code_2, cell_md_3, cell_code_3, 
                cell_md_4, cell_code_4, cell_md_5, cell_code_5, cell_md_6, cell_code_6]

    with open('blog.ipynb', 'w', encoding='utf-8') as f:
        nbf.write(nb, f)

if __name__ == '__main__':
    create_notebook()
    print("Created blog.ipynb")
