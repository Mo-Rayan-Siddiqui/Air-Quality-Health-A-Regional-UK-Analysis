import nbformat

with open('blog.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

code1 = """import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
import os
import warnings
warnings.filterwarnings('ignore')

# Set a beautiful modern theme for all plots
sns.set_theme(style='whitegrid', context='notebook')
plt.rcParams['figure.titlesize'] = 16
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

# Load the merged dataset
data_path = os.path.join("data", "clean", "merged_regional_data.csv")
df = pd.read_csv(data_path)
df.head()"""

code3 = """# Load local English regions GeoJSON
regions_geojson_path = 'eer.json'
gdf = gpd.read_file(regions_geojson_path)

# Calculate average PM2.5 across all years per region
avg_pm25 = df.groupby('region')['PM2.5'].mean().reset_index()

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

# Plot setup
fig, ax = plt.subplots(1, 1, figsize=(10, 8), dpi=100)
gdf_merged.plot(column='PM2.5', ax=ax, legend=True,
                legend_kwds={'label': "Average PM2.5 (μg/m³)", 'orientation': "horizontal", 'shrink': 0.6},
                cmap='YlOrBr', edgecolor='gray', linewidth=0.5, missing_kwds={'color': 'whitesmoke'})

ax.set_title('Average PM2.5 by Region (2015-2023)\\nSpatial distribution of air pollution across England', loc='left', pad=20)
ax.axis('off')
plt.tight_layout()
plt.show()"""

code5 = """plt.figure(figsize=(12, 6), dpi=100)
ax = sns.lineplot(data=df, x='year', y='PM2.5', hue='region', 
                  marker='o', markersize=8, linewidth=2.5, palette='husl')

plt.title('PM2.5 Trends Over Time by Region', loc='left', pad=15)
plt.ylabel('PM2.5 (μg/m³)')
plt.xlabel('Year')
sns.despine(left=True, bottom=True)
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', frameon=False, title='Region')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()"""

code7 = """plt.figure(figsize=(10, 6), dpi=100)

# Scatter points
sns.scatterplot(data=df, x='PM2.5', y='admission_rate_per_100k', 
                hue='region', s=120, alpha=0.8, edgecolor='w', linewidth=0.8, palette='husl')

# Regression line
sns.regplot(data=df, x='PM2.5', y='admission_rate_per_100k', 
            scatter=False, color='crimson', line_kws={"linestyle": "--", "linewidth": 2})

plt.title('PM2.5 vs Respiratory Admission Rate', loc='left', pad=15)
plt.xlabel('PM2.5 (μg/m³)')
plt.ylabel('Respiratory Admission Rate (per 100k)')
sns.despine(left=True, bottom=True)
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', frameon=False, title='Region')
plt.tight_layout()
plt.show()"""

code11 = """# Calculate predictions and residuals
df['predicted'] = model.fittedvalues
df['residuals'] = model.resid

plt.figure(figsize=(10, 6), dpi=100)
sns.residplot(x=df['predicted'], y=df['residuals'], lowess=True, 
              scatter_kws={'alpha': 0.7, 's': 80, 'edgecolor': 'w', 'linewidth': 0.5, 'color': 'steelblue'},
              line_kws={'color': 'crimson', 'linewidth': 2})

plt.title('Residuals vs Predicted Values (Model Validation)', loc='left', pad=15)
plt.xlabel('Predicted Admission Rate (per 100k)')
plt.ylabel('Residuals')
plt.axhline(0, color='gray', linestyle='--', linewidth=1)
sns.despine(left=True, bottom=True)
plt.tight_layout()
plt.show()"""

code_cells = [i for i, c in enumerate(nb.cells) if c.cell_type == 'code']
nb.cells[code_cells[0]].source = code1
nb.cells[code_cells[1]].source = code3
nb.cells[code_cells[2]].source = code5
nb.cells[code_cells[3]].source = code7
nb.cells[code_cells[5]].source = code11

with open('blog.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print("Notebook updated using nbformat successfully.")
