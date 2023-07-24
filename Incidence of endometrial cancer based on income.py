#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[8]:


# Create a DataFrame with the provided data
data = {
    'Sociodemographic index': ['Low', 'Low-middle', 'Middle', 'Middle-High', 'High'],
    'Central Asia': [0, 16.59, 24.57, 12.19, 46.65],
    'Eastern Asia': [0, 3.96, 0, 0, 0],
    'High-income Asia Pacific': [0, 0, 10.40, 0, 0],
    'South Asia': [0, 0, 0, 2.97, 0],
    'Southeast Asia': [0, 0, 0, 1.27, 0],
    'Central Europe': [0, 0, 0, 8.71, 0],
    'Eastern Europe': [0, 0, 0, 0, 3.56],
    'Western Europe': [0, 0, 0, 0, 7.20],
    'Andean Latin America': [0, 0, 0, 0, 2.16],
    'Central Latin America': [0, 0, 0, 0, 6.98],
    'Southern Latin America': [0, 0, 0, 0, 1.78],
    'Tropical Latin America': [0, 0, 0, 0, 3.30],
    'North America': [0, 0, 0, 0, 6.34],
    'South Sub-Saharan Africa': [0, 0, 0, 0, 5.85],
    'Western Sub-Saharan Africa': [0, 0, 0, 0, 3.98],
    'North Afruca and Middle East': [0, 0, 0, 0, 10.37],
    'Oceania': [0, 0, 0, 0, 3.10],
    'Australasia': [0, 0, 0, 0, 2.64],
    'Caribbean': [0, 0, 0, 0, 7.29]
}

df = pd.DataFrame(data).set_index('Sociodemographic index')

# Create the heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(df, cmap='YlOrRd', annot=True, fmt=".2f", linewidths=0.5, cbar=True)

# Customize the plot
plt.title('Contribution Rate of Increasing and Decreasing Trends', fontsize=16)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Sociodemographic Index', fontsize=12)
plt.xticks(rotation=45)
plt.yticks(rotation=0)

# Show the plot
plt.show()


# In[ ]:





# In[ ]:




