import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.interpolate import griddata

# Generate synthetic data
np.random.seed(42)
years = np.arange(2000, 2031)
n_years = len(years)
global_power_consumption_rate = np.random.normal(2.4, 0.5, n_years)
ai_advancement_rate = np.random.normal(1.2, 0.3, n_years)
data_center_power_consumption = np.linspace(150, 1160, n_years)
ai_power_consumption = data_center_power_consumption * (ai_advancement_rate / 10)

# Create DataFrame
df_extended = pd.DataFrame({
    'Year': years,
    'GlobalPowerConsumptionRate': global_power_consumption_rate,
    'AIAdvancementRate': ai_advancement_rate,
    'DataCenterPowerConsumption': data_center_power_consumption,
    'AIPowerConsumption': ai_power_consumption
})

# Define grid for interpolation
grid_x, grid_y = np.mgrid[
    df_extended['GlobalPowerConsumptionRate'].min():df_extended['GlobalPowerConsumptionRate'].max():100j,
    df_extended['AIAdvancementRate'].min():df_extended['AIAdvancementRate'].max():100j
]

# Interpolate the data
grid_z = griddata(
    (df_extended['GlobalPowerConsumptionRate'], df_extended['AIAdvancementRate']),
    df_extended['DataCenterPowerConsumption'],
    (grid_x, grid_y),
    method='cubic'
)

# Normalize data for color mapping
norm = plt.Normalize(df_extended['Year'].min(), df_extended['Year'].max())
colors = plt.cm.viridis(norm(df_extended['Year']))

fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(
    grid_x, grid_y, grid_z, cmap='viridis', edgecolor='none', alpha=0.8)

# Scatter plot for the actual data points
sc = ax.scatter(
    df_extended['GlobalPowerConsumptionRate'], 
    df_extended['AIAdvancementRate'], 
    df_extended['DataCenterPowerConsumption'], 
    c=colors, s=50, label='Data Points')

# Add color bar for year representation
cbar = fig.colorbar(surf)
cbar.set_label('Data Center Power Consumption (TWh)')

ax.set_xlabel('Global Power Consumption Rate (%)')
ax.set_ylabel('AI Advancement Rate (%)')
ax.set_zlabel('Data Center Power Consumption (TWh)')
ax.set_title('AI Power Consumption Data Distribution with Smooth Surface (2000-2030)')

plt.show()
