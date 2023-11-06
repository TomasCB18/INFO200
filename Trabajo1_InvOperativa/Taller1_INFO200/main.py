import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
# Definir la función objetivo y las restricciones
c = [-1, -1]  # Coeficientes de la función objetivo (maximizar)
A = [
    [5000, 8000],   # Restricción 1: 5000x1 + 8000x2 <= 150000
    [155, 5700],    # Restricción 2: 155x1 + 5700x2 <= 50000
    [58, 450],      # Restricción 3: 58x1 + 450x2 <= 5000
    [0, -1]         # Restricción 4: -x2 >= -5 (mínimo de 5 pelotas de fútbol)
]
b = [150000, 50000, 5000, -5]  # Lado derecho de las restricciones

# Resolver el problema de programación lineal
result = linprog(c, A_ub=A, b_ub=b)

# Extraer los resultados
x1_optimal = result.x[0]
x2_optimal = result.x[1]
z_optimal = -result.fun  # Se multiplica por -1 porque linprog resuelve problemas de minimización

# Imprimir la solución optima en consola
print("El punto que Optimiza al max la funcion objetivo es:(",x1_optimal,",",x2_optimal,")")
print("Optimo de la función objetivo (maximizar):", z_optimal)
print("Cantidad de pelotas de tenis a comprar:", x1_optimal)
print("Cantidad de pelotas de futbol a comprar:", x2_optimal)

# Graficar solo la región factible
x1_values = np.linspace(0, 30, 100)
x2_values_1 = (150000 - 5000 * x1_values) / 8000
x2_values_2 = (50000 - 155 * x1_values) / 5700
x2_values_3 = (5000 - 58 * x1_values) / 450

plt.fill_between(x1_values, 0, np.minimum(np.minimum(x2_values_1, x2_values_2), x2_values_3), alpha=0.3, color='gray', label='Región Factible')

plt.scatter(x1_optimal, x2_optimal, color='red', marker='*', label='Solución optima')

plt.title('Región Factible')
plt.xlabel('Pelotas de Tenis (x1)')
plt.ylabel('Pelotas de Futbol (x2)')
plt.legend()
plt.grid(True)
plt.savefig('region_factible.png')
plt.show()

# Graficar solo las restricciones con simbologia
plt.plot(x1_values, x2_values_1, label='5000x1 + 8000x2 <= 150000')
plt.plot(x1_values, x2_values_2, label='155x1 + 5700x2 <= 50000')
plt.plot(x1_values, x2_values_3, label='58x1 + 450x2 <= 5000')

# Agregar linea adicional para la restricción minima de pelotas de futbol
plt.plot(x1_values, 5 * np.ones_like(x1_values), label='x2 >= 5', linestyle='--')

plt.scatter(x1_optimal, x2_optimal, color='red', marker='*', label='Solución Óptima')

plt.title('Restricciones con Simbología')
plt.xlabel('Pelotas de Tenis (x1)')
plt.ylabel('Pelotas de Futbol (x2)')
plt.legend()
plt.grid(True)
plt.savefig('restricciones.png')
plt.show()
