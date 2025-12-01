import pandas as pd
import matplotlib.pyplot as plt

#df = pd.read_csv('C:\Users\gangu\Downloads\archive (1)\Energy_consumption.csv')
df = pd.read_csv(r"C:\Users\gangu\Downloads\archive (1)\Energy_consumption.csv")


results = {}

# 1 Null values
results['null_values'] = df.isnull().sum()

# 2 Duplicates
results['duplicate_count'] = df.duplicated().sum()

# 3 Data types
df.info()
# 4 Outlier detection using IQR
Q1 = df.select_dtypes(include='number').quantile(0.25)
Q3 = df.select_dtypes(include='number').quantile(0.75)
IQR = Q3 - Q1
outliers = df[((df.select_dtypes(include='number') < (Q1 - 1.5 * IQR)) | 
               (df.select_dtypes(include='number') > (Q3 + 1.5 * IQR))).any(axis=1)]
results['outlier_rows'] = len(outliers)

# 5 Summary statistics
results['summary_stats'] = df.describe()

# Figures
plt.figure()
df['EnergyConsumption'].hist()
plt.title("Energy Consumption Distribution")
plt.xlabel("EnergyConsumption")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

plt.figure()
df['Temperature'].plot(kind='box')
plt.title("Temperature Outlier Boxplot")
plt.tight_layout()
plt.show()

plt.figure()
df['RenewableEnergy'].plot(kind='box')
plt.title("Renewable Energy Outlier Boxplot")
plt.tight_layout()
plt.show()

results
