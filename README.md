# Air Quality & Health: A Regional UK Analysis

**🌐 Live Interactive Website:** [https://mo-rayan-siddiqui.github.io/Air-Quality-Health-A-Regional-UK-Analysis/](https://mo-rayan-siddiqui.github.io/Air-Quality-Health-A-Regional-UK-Analysis/)
**📄 Full Research Report:** [Full_Research_Report.md](./Full_Research_Report.md)

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

## 🛠️ Replication Guide

To replicate this analysis from scratch on your local machine, follow these exact steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mo-Rayan-Siddiqui/Air-Quality-Health-A-Regional-UK-Analysis.git
   cd Air-Quality-Health-A-Regional-UK-Analysis
   ```

2. **Install dependencies:**
   Ensure you have Python 3.9+ installed, then run:
   ```bash
   pip install -r requirements.txt
   ```
   *(Core dependencies include: `pandas`, `geopandas`, `statsmodels`, `matplotlib`, `seaborn`, `pytest`, `jupyter`)*

3. **Run the Data Pipeline:**
   Execute the data cleaning and merging script. This processes the raw data in `data/raw/` and generates the final dataset `merged_regional_data.csv` in the `data/clean/` folder.
   ```bash
   python scripts/clean_data.py
   ```

4. **Verify Data Integrity:**
   Run the test suite to ensure the data was merged correctly without data loss or schema errors:
   ```bash
   python -m pytest tests/ -v
   ```

5. **Generate the Analysis and Visualizations:**
   Run the Jupyter notebook to execute the Fixed Effects OLS regression and generate all spatial and temporal plots:
   ```bash
   jupyter nbconvert --to html --execute blog.ipynb
   ```

6. **Extract Results for the Website:**
   Run the extraction script to dump the regression coefficients to a JSON structure used by the interactive website:
   ```bash
   python extract_results.py
   ```

7. **View the Interactive Website locally:**
   Start a local HTTP server in the `website/` directory to view the interactive Plotly charts:
   ```bash
   python -m http.server 8080 --directory website
   ```
   *Then navigate to `http://localhost:8080` in your web browser.*
