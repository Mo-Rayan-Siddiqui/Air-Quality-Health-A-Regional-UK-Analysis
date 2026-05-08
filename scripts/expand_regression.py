import nbformat

with open('blog.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Markdown for section 5
md5 = """## 5. Expanded Regression Analysis

We started with a simple relationship. Now, we'll build a series of OLS regression models to better isolate the impact of PM2.5:
1. **Baseline Model:** Only PM2.5.
2. **Pollutant Controls:** Adding NO2 and O3.
3. **Fixed Effects:** Controlling for unobserved differences across `region` and `year`.
4. **Interaction Model:** Exploring if the combined effect of PM2.5 and NO2 is worse than their individual effects."""

code_reg = """# 1. Baseline Model
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
best_model = mod3"""

md_coef = """### Visualizing the Pollution Effect
To make the impact easier to digest, let's plot the coefficients with their confidence intervals from the Fixed Effects model."""

code_coef = """# Extract coefficients and conf intervals for the pollutants from Model 3
params = mod3.params[['Q("PM2.5")', 'NO2', 'O3']]
conf = mod3.conf_int().loc[['Q("PM2.5")', 'NO2', 'O3']]
conf['error'] = conf[1] - params

plt.figure(figsize=(8, 5), dpi=100)
plt.errorbar(x=params.index, y=params.values, yerr=conf['error'], fmt='o', 
             color='crimson', markersize=10, linewidth=2, capsize=5)

plt.title('Impact of Pollutants on Respiratory Admissions (per 100k)\\nControlling for Region and Year', loc='left', pad=15)
plt.ylabel('Coefficient (Impact)')
plt.axhline(0, color='gray', linestyle='--', linewidth=1)
sns.despine()
plt.tight_layout()
plt.show()"""

md_resid = """## 6. Residuals Plot for Final Model Validation"""

code_resid = """# Calculate predictions and residuals for the Fixed Effects model
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
plt.show()"""

# Replace in cells
nb.cells[8].source = md5
nb.cells[9].source = code_reg

# Insert new cells for coefficient plot
new_md_cell = nbformat.v4.new_markdown_cell(source=md_coef)
new_code_cell = nbformat.v4.new_code_cell(source=code_coef)

nb.cells.insert(10, new_md_cell)
nb.cells.insert(11, new_code_cell)

# Update residual plot cells which are now at indices 12 and 13
nb.cells[12].source = md_resid
nb.cells[13].source = code_resid

with open('blog.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print("Regression analysis expanded successfully.")
