import pyaurn
import pandas as pd

meta = pyaurn.importMeta()
print(meta.columns)
print(meta[['site', 'code', 'zone']].head())
