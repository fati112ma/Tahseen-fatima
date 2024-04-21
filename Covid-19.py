import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Define start and end dates
start_date = datetime(2020, 1, 1)
end_date = datetime(2024, 4, 21)

# Generate date range
date_range = pd.date_range(start=start_date, end=end_date)

# Generate synthetic data
num_days = len(date_range)
new_cases = np.random.randint(100, 1000, size=num_days)
deaths = np.random.randint(1, 50, size=num_days)
recoveries = np.random.randint(50, 800, size=num_days)

# Create DataFrame
data = {
    'Date': date_range,
    'New Cases': new_cases,
    'Deaths': deaths,
    'Recoveries': recoveries
}
df = pd.DataFrame(data)

# Save DataFrame to a CSV file
df.to_csv('covid_data.csv', index=False)

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(df['Date'], df['New Cases'], label = 'New Cases', color='blue', alpha = 0.7)
plt.bar(df['Date'], df['Deaths'], label = 'Deaths', color = 'red', alpha = 0.7)
plt.bar(df['Date'], df['Recoveries'], label='Recoveries', color='green', alpha = 0.7)
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.title("COVID-19 Statistics", loc = "Center")
plt.legend()
plt.grid(True)
plt.show()
