# Air Quality & Health: A Regional UK Analysis

This project investigates the relationship between regional air pollution and respiratory health in the UK. By merging DEFRA's UK air quality monitoring data (PM2.5, NO2, O3) with NHS respiratory hospital admissions data (by region), we aim to identify whether localized pollution levels can predictably explain hospital demand.

## 📊 Policy-Relevant Findings

Our core analysis (`blog.ipynb`) utilizes a robust Fixed Effects OLS regression model controlling for regional differences and year-over-year temporal trends. 

**Key Insights:**
1. **PM2.5 is a Primary Driver of Admissions:** 
   Controlling for other factors, **every 1 μg/m³ increase in average regional PM2.5 is associated with ~40 additional respiratory hospital admissions per 100,000 people.** This borderline statistically significant effect (p = 0.052) highlights fine particulate matter as a critical public health target.
   
2. **NO2 and O3 Effects are Overshadowed by PM2.5:** 
   When modeled together, PM2.5 absorbs most of the statistical variance. Neither NO2 nor O3 proved to be statistically significant independent predictors of respiratory admissions at the regional level once PM2.5 was accounted for.

3. **Regional Health Disparities:** 
   Even after controlling for air quality, the **North West** and **North East and Yorkshire** regions face significantly higher baseline respiratory admissions (~230-240 more per 100k people) compared to southern or eastern regions. This indicates the presence of compounded socioeconomic or healthcare inequalities.

4. **The COVID-19 Anomaly:** 
   The data clearly captures the massive structural drop in respiratory admissions during 2020 (-310 per 100k) and 2021 (-318 per 100k), primarily driven by pandemic lockdowns and social distancing which drastically reduced the transmission of non-COVID respiratory infections.

## 📁 Repository Structure

- `data/raw/` - Raw data downloads from DEFRA (air quality) and the NHS (admissions).
- `data/clean/` - Processed, cleaned, and merged dataset ready for analysis.
- `scripts/` - Python data pipelines for downloading (`download_defra_data.py`, `download_nhs_data.py`) and merging data (`clean_data.py`).
- `tests/` - `pytest` automated test suite to validate the integrity of the data pipeline and merged output.
- `blog.ipynb` - The primary Jupyter notebook containing the full analysis, statistical modeling, and generated spatial/temporal visualizations.
- `blog.html` - An executed, view-ready HTML export of the notebook.

## 🧪 Automated Testing

We use `pytest` to validate our data processing pipelines. Ensure all dependencies are installed (including `pytest`), then run the test suite from the project root:

```bash
python -m pytest tests/ -v
```

The test suite automatically verifies that the output datasets contain no missing values, hold the expected schemas, calculate accurate per-capita rates, and successfully type-cast all variables.
