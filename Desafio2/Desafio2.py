import numpy as np

def jacobi(A, b, x0, tol, max_iter):
  """
  Resuelve un sistema de ecuaciones lineales usando el método de Jacobi.

  Args:
    A: Matriz de coeficientes.
    b: Vector de términos independientes.
    x0: Vector de valores iniciales.
    tol: Tolerancia para la convergencia.
    max_iter: Número máximo de iteraciones.

  Returns:
    Vector solución o None si no converge.
  """

  n = len(A)
  x = x0.copy()
  for k in range(max_iter):
    for i in range(n):
      s = 0
      for j in range(n):
        if i != j:
          s += A[i,j] * x[j]
      x[i] = (b[i] - s) / A[i,i]

    # Criterio de convergencia
    if np.linalg.norm(x - x0) < tol:
        return x
    x0 = x.copy()
  return None

# Ejemplo de uso:
A = np.array([[3, -1, 1],
              [1, 3, 1],
              [1, -1, 3]])
b = np.array([1, 3, 3])
x0 = np.zeros(3)
tol = 1e-6
max_iter = 100

x = jacobi(A, b, x0, tol, max_iter)
if x is not None:
  print("La solución es:", x)
else:
  print("El método no convergió.")