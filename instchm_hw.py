import numpy as np
from scipy.optimize import curve_fit

# Define the Van Deemter equation
def vandeemter(u, A, B, C):
    return A + B/u + C*u

# Your data
flow_rate = np.array([1.53, 3.15, 5.22, 7.91, 10.52, 13.51, 15.67, 17.91, 20.11])
retention_time = np.array([66.40, 32.25, 19.46, 12.84, 9.65, 7.52, 6.48, 5.67, 5.05])
peak_width = np.array([5.11, 1.90, 0.99, 0.63, 0.49, 0.41, 0.38, 0.35, 0.33])

# Calculate linear velocity (u) and plate height (H)
L = 15.0  # column length in cm
u = L / retention_time  # linear velocity in cm/min
sigma = peak_width / (4*np.sqrt(2*np.log(2)))  # standard deviation of the peak
H = sigma**2 / L  # plate height

# Fit the data to the Van Deemter equation
popt, pcov = curve_fit(vandeemter, u, H)

# Print the optimal parameters
print(f"A = {popt[0]}, B = {popt[1]}, C = {popt[2]}")
