import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(42)
years = np.arange(2000, 2031)
n_years = len(years)
global_power_consumption_rate = np.random.normal(2.4, 0.5, n_years)
ai_advancement_rate = np.random.normal(1.2, 0.3, n_years)
data_center_power_consumption = np.linspace(150, 1160, n_years)
ai_power_consumption = data_center_power_consumption * (ai_advancement_rate / 10)

df = pd.DataFrame({
    'Year': years,
    'GlobalPowerConsumptionRate': global_power_consumption_rate,
    'AIAdvancementRate': ai_advancement_rate,
    'DataCenterPowerConsumption': data_center_power_consumption,
    'AIPowerConsumption': ai_power_consumption
})

X = df[['GlobalPowerConsumptionRate', 'AIAdvancementRate', 'DataCenterPowerConsumption']].values
y = df['AIPowerConsumption'].values

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

def gradient_descent(X, y, learning_rate=0.01, iterations=100):
    m, n = X.shape
    theta = np.zeros(n)
    history = []

    for i in range(iterations):
        gradients = -2/m * X.T.dot(y - X.dot(theta))
        theta = theta - learning_rate * gradients
        cost = (1/m) * np.sum((y - X.dot(theta))**2)
        history.append((theta.copy(), cost))

    return theta, history

theta_final, history = gradient_descent(X_scaled, y, learning_rate=0.1, iterations=50)

theta_history, cost_history = zip(*history)

theta_0, theta_1, theta_2 = zip(*theta_history)
cost = np.array(cost_history)

fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

sc = ax.scatter(theta_0, theta_1, theta_2, c=cost, cmap='viridis', marker='o', s=50)
ax.plot(theta_0, theta_1, theta_2, color='red', linestyle='--', linewidth=2, marker='x', markersize=5)

cbar = fig.colorbar(sc)
cbar.set_label('Cost')

ax.set_xlabel('Theta 0')
ax.set_ylabel('Theta 1')
ax.set_zlabel('Theta 2')
ax.set_title('Gradient Descent Optimization Path')

plt.show()
