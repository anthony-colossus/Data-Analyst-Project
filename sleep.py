import pandas as pd
import matplotlib.pyplot as plt

# Load the updated sleep data
data = pd.read_csv('/content/sleep_data(extra).csv', parse_dates=['Sleep_Start', 'Sleep_End'])

# Calculate sleep duration
data['Sleep_Duration'] = (data['Sleep_End'] - data['Sleep_Start']).dt.total_seconds() / 3600  # in hours

# Calculate average sleep time
data['Sleep_Start_Hour'] = data['Sleep_Start'].dt.hour + data['Sleep_Start'].dt.minute / 60

# Analyze average sleep duration
avg_sleep_duration = data['Sleep_Duration'].mean()
print(f"Average Sleep Duration: {avg_sleep_duration:.2f} hours")

# Analyze average sleep start time
avg_sleep_start = data['Sleep_Start_Hour'].mean()
print(f"Average Sleep Start Time: {avg_sleep_start:.2f} hours")

# Analyze sleep quality
avg_sleep_quality = data['Sleep_Quality'].mean()
print(f"Average Sleep Quality Rating: {avg_sleep_quality:.2f}")

# Analyze average heart rate during sleep
avg_heart_rate = data['Heart_Rate_Avg'].mean()
print(f"Average Heart Rate During Sleep: {avg_heart_rate:.2f} BPM")

# Plot Sleep Duration
plt.figure(figsize=(10, 5))
plt.bar(data['Date'], data['Sleep_Duration'], color='skyblue')
plt.title('Sleep Duration Over Days')
plt.xlabel('Date')
plt.ylabel('Sleep Duration (hours)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Plot Movement Count
plt.figure(figsize=(10, 5))
plt.bar(data['Date'], data['Movement_Count'], color='salmon')
plt.title('Movement Count During Sleep')
plt.xlabel('Date')
plt.ylabel('Movement Count')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Plot Sleep Quality
plt.figure(figsize=(10, 5))
plt.bar(data['Date'], data['Sleep_Quality'], color='lightgreen')
plt.title('Sleep Quality Over Days')
plt.xlabel('Date')
plt.ylabel('Sleep Quality Rating')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Plot Average Heart Rate
plt.figure(figsize=(10, 5))
plt.bar(data['Date'], data['Heart_Rate_Avg'], color='lightcoral')
plt.title('Average Heart Rate During Sleep Over Days')
plt.xlabel('Date')
plt.ylabel('Heart Rate (BPM)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Plot Caffeine and Alcohol Intake
plt.figure(figsize=(10, 5))
plt.bar(data['Date'], data['Caffeine_Intake'], label='Caffeine Intake (mg)', alpha=0.7)
plt.bar(data['Date'], data['Alcohol_Intake'] * 100, label='Alcohol Intake (Standard Drinks)', alpha=0.5)  # Scale for visibility
plt.title('Caffeine and Alcohol Intake Over Days')
plt.xlabel('Date')
plt.ylabel('Intake')
plt.xticks(rotation=45)
plt.legend()
plt.grid(axis='y')
plt.show()
