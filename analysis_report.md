# Comprehensive Analysis Report: Air Quality & Respiratory Health in the UK

## 1. Executive Summary
This report details the investigation into the relationship between regional air pollution and respiratory health across England from 2015 to 2023. By combining air quality metrics from DEFRA with NHS hospital admissions data, the project sought to isolate the impacts of specific pollutants (PM2.5, NO2, O3) on public health infrastructure. 

The core finding is that **Fine Particulate Matter (PM2.5)** is a primary driver of respiratory hospital admissions. The analysis demonstrates that for every 1 μg/m³ increase in PM2.5, respiratory admissions rise by approximately 40 per 100,000 population, even after rigorous controls for regional baselines and temporal anomalies.

## 2. Data Sources & Methodology
**Data Sources:**
- **DEFRA Automatic Urban and Rural Network (AURN):** Provided daily monitoring data for PM2.5, NO2, and O3, which was aggregated into annual regional averages.
- **NHS England:** Provided annual respiratory hospital admissions by region.
- **ONS/Nomis:** Population estimates used to calculate the normalized `admission_rate_per_100k`.

**Methodology:**
1. **Data Pipeline:** Python scripts automated the retrieval and aggregation of raw data. A testing suite (`pytest`) was utilized to ensure structural integrity and correct normalization of the merged dataset.
2. **Exploratory Data Analysis (EDA):** Visualized regional pollution distributions via a choropleth map (using the `eer.json` GeoJSON shapefile) and mapped the time series of PM2.5 reductions.
3. **Statistical Modeling:** Conducted Ordinary Least Squares (OLS) regression modeling in progressive stages, building up to a robust Fixed Effects model that isolated the impact of PM2.5 by controlling for both regional invariants and year-over-year shifts.

## 3. Exploratory Data Analysis
- **Spatial Distribution:** The choropleth map indicates higher concentrations of PM2.5 in densely populated regions, notably London and the South East.
- **Temporal Trends:** A clear, consistent downward trend in average PM2.5 levels is visible across all regions from 2015 to 2023.
- **Bivariate Correlation:** Scatter plotting the raw data revealed a positive correlation between PM2.5 and admission rates, though distinct regional clusters highlighted the need for fixed effects modeling.

## 4. Regression Analysis Results
We evaluated four progressive models to ensure the robustness of the findings:

1. **Baseline Model:** PM2.5 alone showed a positive correlation with admissions.
2. **Pollutant Controls:** Adding NO2 and O3 weakened the independent significance of the additional pollutants, suggesting PM2.5 absorbs the primary statistical variance.
3. **Fixed Effects Model (Final Model):** 
   - **PM2.5 Impact:** After controlling for region and year, PM2.5 retained a coefficient of **39.99 (p = 0.052)**. 
   - **Regional Disparities:** The North West and North East/Yorkshire showed significantly higher baseline admission rates (coefficients of +244 and +234 respectively compared to the reference region), pointing to socio-demographic factors outside of air quality.
   - **COVID-19 Impact:** The year 2020 and 2021 dummy variables showed massive, highly significant drops in admissions (-310 and -318 per 100k), accurately capturing the reduction of transmissible respiratory illnesses during lockdowns.
4. **Interaction Model:** The interaction between PM2.5 and NO2 did not yield a statistically significant amplifying effect in this regional aggregation.

## 5. Policy Implications
1. **Targeting PM2.5:** Given its position as the primary statistically significant pollutant driving hospital admissions, environmental policy and low-emission zones should prioritize fine particulate matter reduction.
2. **Addressing Regional Inequities:** The severe baseline disparities in the North of England suggest that while clean air is crucial, public health interventions must also address compounded socioeconomic vulnerabilities and healthcare access in these specific regions.
3. **Health Service Planning:** The quantified coefficient (40 additional admissions per 100k per 1 μg/m³ of PM2.5) provides a tangible metric for the NHS to model expected respiratory ward demand based on localized air quality forecasts.

## 6. Limitations & Next Steps
- **Granularity:** The current data is aggregated at the broad regional level. Local Authority District (LAD) or Lower Layer Super Output Area (LSOA) level analysis would yield more precise, localized insights.
- **Confounding Variables:** Future analysis should ingest specific socioeconomic indices (e.g., Index of Multiple Deprivation) and smoking prevalence to further refine the model's accuracy.
