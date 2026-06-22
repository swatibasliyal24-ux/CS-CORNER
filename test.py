import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
data = pd.read_csv('laptop_data.csv')
print(data.head())
print(data.shape)
print(data.info())
print(data.isnull().sum())
print(data.columns)
print(data.duplicated().sum())



sorted_df = data.sort_values(by='Price', ascending=False)

print(sorted_df.head(10))
print("SWATI TEST")