import numpy as np
from scipy.stats import hmean, gmean

# Datos
data = [4, 2, 3, 4, 3, 1, 4, 3, 3, 4, 1, 3]

# Media Aritmética
mean_arithmetic = np.mean(data)

# Media Armónica
mean_harmonic = hmean(data)

# Media Cuadrática
mean_quadratic = np.sqrt(np.mean(np.square(data)))

# Media Geométrica
mean_geometric = gmean(data)

print(mean_arithmetic, mean_harmonic, mean_quadratic, mean_geometric)