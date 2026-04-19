# Traffic Accident Data Analysis and Visualization

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample accident dataset
data = {
    "Time": ["Morning","Night","Evening","Morning","Night","Evening","Morning","Night","Evening","Morning"],
    "Weather": ["Clear","Rainy","Clear","Foggy","Rainy","Clear","Foggy","Rainy","Clear","Clear"],
    "Road_Condition": ["Dry","Wet","Dry","Wet","Wet","Dry","Wet","Wet","Dry","Dry"],
    "Accident_Count": [12,25,15,20,30,18,22,28,16,14]
}

df = pd.DataFrame(data)

print(df)

# ================== EDA ==================

# 1. Accidents based on time of day
sns.barplot(x="Time", y="Accident_Count", data=df)
plt.title("Accidents Based on Time of Day")
plt.show()

# 2. Accidents based on weather
sns.barplot(x="Weather", y="Accident_Count", data=df)
plt.title("Accidents Based on Weather Conditions")
plt.show()

# 3. Accidents based on road condition
sns.barplot(x="Road_Condition", y="Accident_Count", data=df)
plt.title("Accidents Based on Road Condition")
plt.show()
