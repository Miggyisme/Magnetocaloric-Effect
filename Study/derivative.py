import numpy as np
import matplotlib.pyplot as plt

nome_arquivo = "ferro_M_B15_L515439.0.dat"

x = []
y = []

with open(nome_arquivo, 'r') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) >= 2:
            x.append(float(parts[0]))
            y.append(float(parts[1]))

x = np.array(x)
y = np.array(y)

# Derivada do numpy
dy_dx = np.gradient(y, x)

# Plot
plt.scatter(x, dy_dx, label='dy/dx')
plt.xlabel('x')
plt.ylabel('dy/dx')
plt.title('Derivada Numérica')
plt.legend()
plt.grid(True)
plt.show()
