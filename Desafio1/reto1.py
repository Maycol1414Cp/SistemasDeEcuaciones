import numpy as np

# Coeficientes de las ecuaciones (matriz de coeficientes)
A = np.array([
    [0.52, 0.3, 0.18],
    [0.2, 0.5, 0.3 ],
    [0.25, 0.2, 0.55]
])
#trasnpuesta de la matriz
At=np.transpose(A)
# Términos independientes (cantidad requerida de arena, grano fino, grano grueso)
b = np.array([4800, 5810, 5690])

# Resolver el sistema de ecuaciones
solucion = np.linalg.solve(At, b)
totD=sum(b)
totS=sum(solucion)
print(f"Total demanda: {totD:.2f} m³")

# Mostrar resultados
print(f"Metros cúbicos a transportar desde cada cantera:")
for i in range(3):
    print(f"Cantera {i+1}: {solucion[i]:.2f} m³")
print(f"Total suministro: {totS:.2f} m³")