import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

years = np.arange(2000, 2031)
consumption = np.array([3000, 3050, 3100, 3200, 3300, 3400, 3550, 3700, 3850, 4000, 4200, 4400, 4600, 4800, 5050, 5300, 5550, 5800, 6100, 6400, 6750, 7100, 7500, 7900, 8350, 8800, 9250, 9700, 10150, 10600, 11100])  # hypothetical values

data = pd.DataFrame({'Year': years, 'Consumption': consumption})

model = LinearRegression()
model.fit(data[['Year']], data['Consumption'])

future_years = np.arange(2000, 2031).reshape(-1, 1)
data['Predicted_Consumption'] = model.predict(future_years)

plt.figure(figsize=(12, 6))
plt.scatter(data['Year'], data['Consumption'], label='Actual Consumption', color='blue', marker='x')
plt.plot(data['Year'], data['Predicted_Consumption'], label='Predicted Consumption up to 2023', color='red', linestyle='-')

future_years_extended = np.arange(2023, 2031).reshape(-1, 1)
predicted_future_consumption = model.predict(future_years_extended)
plt.plot(future_years_extended, predicted_future_consumption, label='Predicted Consumption beyond 2023', color='green', linestyle='--')

plt.xlabel('Year')
plt.ylabel('Electricity Consumption (MWh)')
plt.title('Electricity Consumption Prediction up to 2030 using Linear Regression')
plt.legend()
plt.grid(True)
plt.show()
