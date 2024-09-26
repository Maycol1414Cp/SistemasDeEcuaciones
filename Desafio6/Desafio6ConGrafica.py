import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Crear una cuadrícula de puntos en el plano xy
x = np.linspace(-1, 2, 100)
y = np.linspace(-1, 2, 100)
X, Y = np.meshgrid(x, y)

# Definir las ecuaciones en función de z
Z1 = (1 - 0.999 * X - 0.001 * Y) / 0.001
Z2 = (1 - 0.001 * X - 0.999 * Y) / 0.001
Z3 = (1 - 0.001 * X - 0.001 * Y) / 0.999

# Graficar las superficies
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z1, alpha=0.5, rstride=100, cstride=100, color='red', label='Ecuación 1')
ax.plot_surface(X, Y, Z2, alpha=0.5, rstride=100, cstride=100, color='blue', label='Ecuación 2')
ax.plot_surface(X, Y, Z3, alpha=0.5, rstride=100, cstride=100, color='green', label='Ecuación 3')

# Configurar el gráfico
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Sistema de Ecuaciones 3x3')
ax.view_init(30, 30)  # Vista en 3D

# Mostrar el gráfico
plt.savefig('Desafio6Python.png')
