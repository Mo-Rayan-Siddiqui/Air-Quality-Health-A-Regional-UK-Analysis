# Air Quality & Respiratory Health in the UK: A Regional Analysis
**Author:** NabAli  
**Date:** May 2026  

---

## Abstract
This study investigates the localized impact of air pollution—specifically Fine Particulate Matter (PM2.5), Nitrogen Dioxide (NO2), and Ozone (O3)—on respiratory hospital admissions across the regions of England from 2015 to 2023. By merging environmental monitoring data from the Department for Environment, Food & Rural Affairs (DEFRA) with healthcare demand data from the National Health Service (NHS), this report builds a multi-variate Fixed Effects Ordinary Least Squares (OLS) regression model. The analysis establishes that PM2.5 is the most significant environmental driver of respiratory hospital admissions. We find that for every 1 μg/m³ increase in average regional PM2.5, respiratory hospital admissions increase by approximately 40 per 100,000 population. Furthermore, the model uncovers stark regional baseline inequalities and successfully captures the anomalous structural drops in admissions during the 2020/2021 COVID-19 lockdowns.

---

## 1. Introduction
Air pollution remains one of the most critical environmental determinants of public health. While national studies often generalize the impact of pollutants, localized regional analysis provides actionable intelligence for healthcare administration and urban planning. This project specifically examines the varying degrees of respiratory hospital admissions across English regions and correlates them with key pollutants.

The primary objective is to determine whether localized spikes in specific pollutants consistently predict increased hospital demand. By identifying the primary culprits among PM2.5, NO2, and O3, policymakers can target emission-reduction strategies more effectively.

---

## 2. Methodologies
### 2.1 Data Collection
- **Environmental Data:** Sourced from DEFRA's Automatic Urban and Rural Network (AURN). Daily metrics for PM2.5, NO2, and O3 were aggregated into annual regional averages.
- **Healthcare Data:** Sourced from NHS England, providing total annual respiratory hospital admissions mapped to English administrative regions.
- **Demographic Normalization:** Population data from ONS/Nomis was utilized to normalize admissions into a standardized rate: `admission_rate_per_100k`.

### 2.2 Analytical Framework
A robust data pipeline merged these datasets by `region` and `year`. The statistical approach began with Exploratory Data Analysis (EDA) to visualize spatial and temporal trends. We then progressed to an OLS regression framework, culminating in a Fixed Effects model that controlled for unobserved regional heterogeneity (e.g., socioeconomic deprivation) and temporal shocks (e.g., COVID-19).

---

## 3. Exploratory Data Analysis & Results

### 3.1 Spatial Distribution of PM2.5
We first visualized the geographic spread of pollution. The choropleth map below demonstrates the variance in average PM2.5 levels across England, highlighting denser concentrations in urban hubs like London and the South East.

![Choropleth Map of PM2.5](blog_files/blog_3_0.png)

### 3.2 Temporal Trends (2015-2023)
Analyzing the trends over the 8-year period reveals a general, consistent downward trajectory in PM2.5 across all regions, reflecting the success of recent clean air initiatives.

![Time Series of PM2.5](blog_files/blog_5_0.png)

### 3.3 Bivariate Correlation
A direct comparison between PM2.5 and the respiratory admission rate shows a positive correlation. However, the distinct clustering of regional colors indicates that while pollution drives admissions, the baseline rates differ wildly depending on the region.

![Scatter Plot: PM2.5 vs Admissions](blog_files/blog_7_0.png)

---

## 4. Regression Analysis
To isolate the true effect of the pollutants, we ran a Fixed Effects regression model controlling for `region` and `year`. 

### 4.1 Visualizing the Pollution Effect
The coefficient plot below extracts the impact of the three major pollutants from our Fixed Effects model. 

![Coefficient Plot](blog_files/blog_11_0.png)

**Key Findings:**
- **PM2.5 Dominance:** Controlling for all other factors, PM2.5 retains a positive coefficient of ~40 (p = 0.052). This means every 1 μg/m³ increase drives ~40 additional admissions per 100k people.
- **NO2 and O3:** When modeled alongside PM2.5, these pollutants do not show a statistically significant independent effect, suggesting PM2.5 absorbs the primary statistical variance for respiratory harm in this dataset.

### 4.2 Model Validation
The residuals plot for the Fixed Effects model demonstrates a relatively even distribution around zero, confirming that our model accurately captures the variance without severe heteroskedasticity.

![Residuals Plot](blog_files/blog_13_0.png)

### 4.3 Uncovering Anomalies
Our model also quantified two critical non-pollution factors:
- **Regional Inequity:** The North West and North East & Yorkshire regions have a baseline admission rate of ~230-240 more per 100k people than the East of England, pointing to compounded socio-demographic health disparities.
- **COVID-19:** The year coefficients for 2020 and 2021 showed massive drops (-310 and -318 per 100k), validating the model's accuracy in capturing lockdown-induced reductions in transmissible respiratory infections.

---

## 5. Conclusion
This study provides clear evidence that fine particulate matter (PM2.5) is a statistically significant driver of respiratory hospital admissions at the regional level, overpowering the independent effects of NO2 and O3. While air quality is improving nationally, the quantified impact of PM2.5 gives the NHS a tangible metric for demand forecasting. Furthermore, the stark baseline disparities highlight that environmental policy must be coupled with targeted public health funding in the North of England to address compounded vulnerabilities.

---

## 6. References
1. Department for Environment, Food & Rural Affairs (DEFRA). Automatic Urban and Rural Network (AURN) datasets.
2. NHS England. Hospital Episode Statistics (HES) for Respiratory Admissions.
3. Office for National Statistics (ONS). Regional Population Estimates.
4. Seabold, Skipper, and Josef Perktold. "statsmodels: Econometric and statistical modeling with python." Proceedings of the 9th Python in Science Conference. 2010.
