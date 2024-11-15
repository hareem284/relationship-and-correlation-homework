#importing matplotlib
import matplotlib.pyplot as plt
#importing pandas
import pandas as pd
#importing seaborn
import seaborn as sns
#reading dataframe
rdf=pd.read_csv("FuelConsumption(4).csv")
print(rdf.info())
print(rdf.head())
#creating a scatter plot
sns.set_style('whitegrid')
sns.set_theme('paper')
sns.set_context('talk')
sns.scatterplot(rdf,x='CO2EMISSIONS',y='FUELCONSUMPTION_COMB_MPG',hue='FUELTYPE',palette='viridis')
plt.show()
