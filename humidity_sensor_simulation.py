# Author: Mithila Gubba
# Project: Simulation of Capacitive Humidity Sensor Using MEMS and Polymer Materials

import numpy as np
import matplotlib.pyplot as plt

initial_capacitance = 1e-12  # 1 pF base capacitance
relative_permittivities = {
    "Polyimide": 3.4,
    "PMMA": 2.6,
    "PVA": 7.0,
    "Nafion": 6.5
}

humidity_levels = np.linspace(0, 100, 50)  # 0% to 100% RH

def simulate_capacitance_change(epsilon_r, humidity):
    # Linear model: C = C0 * (1 + alpha * RH), alpha depends on material
    alpha = 0.01 * epsilon_r  # Simplified coefficient for change with RH
    return initial_capacitance * (1 + alpha * humidity / 100)


plt.figure(figsize=(10, 6))
for material, epsilon_r in relative_permittivities.items():
    capacitance_values = simulate_capacitance_change(epsilon_r, humidity_levels)
    plt.plot(humidity_levels, capacitance_values * 1e12, label=material)  

plt.title('Capacitance Response of MEMS Humidity Sensor with Different Polymers')
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Capacitance (pF)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
