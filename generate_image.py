import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv('data/clean/merged_regional_data.csv')
fig = plt.figure(figsize=(10, 6), dpi=100)
sm.graphics.plot_partregress('admission_rate_per_100k', 'Q("PM2.5")', ['NO2', 'O3', 'C(region)', 'C(year)'], data=df, obs_labels=False, ax=fig.gca())
plt.title("Partial Regression Plot: PM2.5 vs Admissions\n(Controlling for Region, Year, NO2, O3)", loc='left', pad=15)
plt.xlabel("PM2.5 (Residuals)")
plt.ylabel("Admission Rate per 100k (Residuals)")
sns.despine(left=True, bottom=True)
plt.grid(axis='both', alpha=0.3)
plt.tight_layout()
os.makedirs("website/images", exist_ok=True)
plt.savefig("website/images/partial_regression.png")
print("Saved partial_regression.png")
