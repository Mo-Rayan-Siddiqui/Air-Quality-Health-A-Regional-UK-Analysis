# Does dirty air fill hospital wards? A regional analysis of UK air pollution and respiratory admissions.

This notebook explores the relationship between air pollution (PM2.5) and respiratory hospital admissions across UK regions.
We merge DEFRA's UK air quality monitoring data with NHS respiratory admissions data and run an OLS regression to show how pollution levels predict hospital demand.

## 1. Setup and Data Loading


```python
import pandas as pd
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
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>region</th>
      <th>year</th>
      <th>respiratory_admissions</th>
      <th>population</th>
      <th>admission_rate_per_100k</th>
      <th>PM2.5</th>
      <th>NO2</th>
      <th>O3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>London</td>
      <td>2015</td>
      <td>132735</td>
      <td>9000000</td>
      <td>1474.84</td>
      <td>12.75</td>
      <td>31.59</td>
      <td>42.82</td>
    </tr>
    <tr>
      <th>1</th>
      <td>North West</td>
      <td>2015</td>
      <td>116295</td>
      <td>7300000</td>
      <td>1593.09</td>
      <td>10.96</td>
      <td>26.94</td>
      <td>42.86</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Midlands</td>
      <td>2015</td>
      <td>165497</td>
      <td>10800000</td>
      <td>1532.38</td>
      <td>11.59</td>
      <td>30.51</td>
      <td>41.21</td>
    </tr>
    <tr>
      <th>3</th>
      <td>East of England</td>
      <td>2015</td>
      <td>85321</td>
      <td>6200000</td>
      <td>1376.15</td>
      <td>9.77</td>
      <td>23.50</td>
      <td>43.95</td>
    </tr>
    <tr>
      <th>4</th>
      <td>South East</td>
      <td>2015</td>
      <td>113922</td>
      <td>9200000</td>
      <td>1238.29</td>
      <td>10.12</td>
      <td>21.48</td>
      <td>39.64</td>
    </tr>
  </tbody>
</table>
</div>



## 2. Choropleth Map of Average PM2.5 by Region


```python
# Load local English regions GeoJSON
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

ax.set_title('Average PM2.5 by Region (2015-2023)\nSpatial distribution of air pollution across England', loc='left', pad=20)
ax.axis('off')
plt.tight_layout()
plt.show()
```


    
![png](blog_files/blog_3_0.png)
    


## 3. Time Series of Pollution Trends (2015-2023)


```python
plt.figure(figsize=(12, 6), dpi=100)
ax = sns.lineplot(data=df, x='year', y='PM2.5', hue='region', 
                  marker='o', markersize=8, linewidth=2.5, palette='husl')

plt.title('PM2.5 Trends Over Time by Region', loc='left', pad=15)
plt.ylabel('PM2.5 (μg/m³)')
plt.xlabel('Year')
sns.despine(left=True, bottom=True)
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', frameon=False, title='Region')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()
```


    
![png](blog_files/blog_5_0.png)
    


## 4. Scatter Plot: PM2.5 vs Respiratory Admissions


```python
plt.figure(figsize=(10, 6), dpi=100)

# Scatter points
sns.scatterplot(data=df, x='PM2.5', y='admission_rate_per_100k', 
                hue='region', s=120, alpha=0.8, edgecolor='w', linewidths=0.8, palette='husl')

# Regression line
sns.regplot(data=df, x='PM2.5', y='admission_rate_per_100k', 
            scatter=False, color='crimson', line_kws={"linestyle": "--", "linewidth": 2})

plt.title('PM2.5 vs Respiratory Admission Rate', loc='left', pad=15)
plt.xlabel('PM2.5 (μg/m³)')
plt.ylabel('Respiratory Admission Rate (per 100k)')
sns.despine(left=True, bottom=True)
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', frameon=False, title='Region')
plt.tight_layout()
plt.show()
```


    
![png](blog_files/blog_7_0.png)
    


## 5. Expanded Regression Analysis

We started with a simple relationship. Now, we'll build a series of OLS regression models to better isolate the impact of PM2.5:
1. **Baseline Model:** Only PM2.5.
2. **Pollutant Controls:** Adding NO2 and O3.
3. **Fixed Effects:** Controlling for unobserved differences across `region` and `year`.
4. **Interaction Model:** Exploring if the combined effect of PM2.5 and NO2 is worse than their individual effects.


```python
# 1. Baseline Model
mod1 = smf.ols('admission_rate_per_100k ~ Q("PM2.5")', data=df).fit()

# 2. Pollutant Controls
mod2 = smf.ols('admission_rate_per_100k ~ Q("PM2.5") + NO2 + O3', data=df).fit()

# 3. Fixed Effects (Region and Year)
mod3 = smf.ols('admission_rate_per_100k ~ Q("PM2.5") + NO2 + O3 + C(region) + C(year)', data=df).fit()

# 4. Interaction Term
mod4 = smf.ols('admission_rate_per_100k ~ Q("PM2.5") * NO2 + O3 + C(region) + C(year)', data=df).fit()

from statsmodels.iolib.summary2 import summary_col
print(summary_col([mod1, mod2, mod3, mod4], 
                  model_names=['Baseline', 'Pollutants', 'Fixed Effects', 'Interaction'],
                  stars=True, float_format='%0.3f',
                  info_dict={'R-squared': lambda x: f"{x.rsquared:0.3f}",
                             'No. Observations': lambda x: f"{int(x.nobs)}"}))

# We'll use the fixed effects model (mod3) for our final predictions and validation.
best_model = mod3
```

    
    =====================================================================================
                                           Baseline  Pollutants Fixed Effects Interaction
    -------------------------------------------------------------------------------------
    Intercept                             624.467*** 615.020    949.840***    1262.685** 
                                          (157.826)  (442.891)  (217.374)     (560.568)  
    Q("PM2.5")                            69.208***  61.197     39.992*       7.557      
                                          (16.755)   (38.641)   (20.036)      (57.181)   
    NO2                                              3.019      -3.584        -14.838    
                                                     (11.425)   (4.114)       (19.019)   
    O3                                               0.315      2.019         1.995      
                                                     (6.490)    (2.064)       (2.079)    
    C(region)[T.London]                                         35.002        37.193     
                                                                (45.202)      (45.666)   
    C(region)[T.Midlands]                                       114.881***    119.403*** 
                                                                (28.872)      (30.019)   
    C(region)[T.North East and Yorkshire]                       234.679***    234.304*** 
                                                                (22.780)      (22.951)   
    C(region)[T.North West]                                     244.723***    245.960*** 
                                                                (23.782)      (24.038)   
    C(region)[T.South East]                                     -72.468***    -70.555*** 
                                                                (23.596)      (23.972)   
    C(region)[T.South West]                                     -73.996**     -97.867*   
                                                                (34.379)      (52.432)   
    C(year)[T.2016]                                             -35.100       -33.863    
                                                                (28.206)      (28.480)   
    C(year)[T.2017]                                             -74.930**     -73.518**  
                                                                (27.970)      (28.265)   
    C(year)[T.2018]                                             -77.195**     -76.707**  
                                                                (30.750)      (30.979)   
    C(year)[T.2019]                                             -76.374**     -78.286**  
                                                                (31.553)      (31.933)   
    C(year)[T.2020]                                             -309.973***   -313.496***
                                                                (34.947)      (35.672)   
    C(year)[T.2021]                                             -318.310***   -320.268***
                                                                (34.012)      (34.406)   
    C(year)[T.2022]                                             -130.595***   -131.922***
                                                                (35.077)      (35.394)   
    C(year)[T.2023]                                             -157.918***   -162.898***
                                                                (37.959)      (39.101)   
    Q("PM2.5"):NO2                                                            1.156      
                                                                              (1.908)    
    R-squared                             0.219      0.220      0.950         0.950      
    R-squared Adj.                        0.206      0.180      0.931         0.930      
    No. Observations                      63         63         63            63         
    R-squared                             0.219      0.220      0.950         0.950      
    =====================================================================================
    Standard errors in parentheses.
    * p<.1, ** p<.05, ***p<.01
    

### Visualizing the Pollution Effect
To make the impact easier to digest, let's plot the coefficients with their confidence intervals from the Fixed Effects model.


```python
# Extract coefficients and conf intervals for the pollutants from Model 3
params = mod3.params[['Q("PM2.5")', 'NO2', 'O3']]
conf = mod3.conf_int().loc[['Q("PM2.5")', 'NO2', 'O3']]
conf['error'] = conf[1] - params

plt.figure(figsize=(8, 5), dpi=100)
plt.errorbar(x=params.index, y=params.values, yerr=conf['error'], fmt='o', 
             color='crimson', markersize=10, linewidth=2, capsize=5)

plt.title('Impact of Pollutants on Respiratory Admissions (per 100k)\nControlling for Region and Year', loc='left', pad=15)
plt.ylabel('Coefficient (Impact)')
plt.axhline(0, color='gray', linestyle='--', linewidth=1)
sns.despine()
plt.tight_layout()
plt.show()
```


    
![png](blog_files/blog_11_0.png)
    


## 6. Residuals Plot for Final Model Validation


```python
# Calculate predictions and residuals for the Fixed Effects model
df['predicted'] = best_model.fittedvalues
df['residuals'] = best_model.resid

plt.figure(figsize=(10, 6), dpi=100)
sns.residplot(x=df['predicted'], y=df['residuals'], lowess=True, 
              scatter_kws={'alpha': 0.7, 's': 80, 'edgecolor': 'w', 'linewidths': 0.5, 'color': 'steelblue'},
              line_kws={'color': 'crimson', 'linewidth': 2})

plt.title('Residuals vs Predicted Values (Fixed Effects Model)', loc='left', pad=15)
plt.xlabel('Predicted Admission Rate (per 100k)')
plt.ylabel('Residuals')
plt.axhline(0, color='gray', linestyle='--', linewidth=1)
sns.despine(left=True, bottom=True)
plt.tight_layout()
plt.show()
```


    
![png](blog_files/blog_13_0.png)
    

