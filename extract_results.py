import pandas as pd
import statsmodels.formula.api as smf
import json

df = pd.read_csv('data/clean/merged_regional_data.csv')

mod1 = smf.ols('admission_rate_per_100k ~ Q("PM2.5")', data=df).fit()
mod2 = smf.ols('admission_rate_per_100k ~ Q("PM2.5") + NO2 + O3', data=df).fit()
mod3 = smf.ols('admission_rate_per_100k ~ Q("PM2.5") + NO2 + O3 + C(region) + C(year)', data=df).fit()

results = {
    'baseline': {
        'rsquared': round(mod1.rsquared, 4),
        'pm25_coef': round(mod1.params['Q("PM2.5")'], 2),
        'pm25_pval': round(mod1.pvalues['Q("PM2.5")'], 4),
    },
    'pollutants': {
        'rsquared': round(mod2.rsquared, 4),
        'pm25_coef': round(mod2.params['Q("PM2.5")'], 2),
        'no2_coef': round(mod2.params['NO2'], 2),
        'o3_coef': round(mod2.params['O3'], 2),
    },
    'fixed_effects': {
        'rsquared': round(mod3.rsquared, 4),
        'pm25_coef': round(mod3.params['Q("PM2.5")'], 2),
        'pm25_pval': round(mod3.pvalues['Q("PM2.5")'], 4),
        'no2_coef': round(mod3.params['NO2'], 2),
        'no2_pval': round(mod3.pvalues['NO2'], 4),
        'o3_coef': round(mod3.params['O3'], 2),
        'o3_pval': round(mod3.pvalues['O3'], 4),
        'pm25_ci_low': round(mod3.conf_int().loc['Q("PM2.5")'][0], 2),
        'pm25_ci_high': round(mod3.conf_int().loc['Q("PM2.5")'][1], 2),
        'no2_ci_low': round(mod3.conf_int().loc['NO2'][0], 2),
        'no2_ci_high': round(mod3.conf_int().loc['NO2'][1], 2),
        'o3_ci_low': round(mod3.conf_int().loc['O3'][0], 2),
        'o3_ci_high': round(mod3.conf_int().loc['O3'][1], 2),
    }
}

for key in mod3.params.index:
    if 'C(region)' in key:
        region_name = key.replace('C(region)[T.', '').replace(']', '')
        results['fixed_effects']['region_' + region_name] = round(mod3.params[key], 2)
    if 'C(year)' in key:
        year_val = key.replace('C(year)[T.', '').replace(']', '')
        results['fixed_effects']['year_' + year_val] = round(mod3.params[key], 2)

print(json.dumps(results, indent=2))
