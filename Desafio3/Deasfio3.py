import numpy as np

def gauss_seidel(A, b, x0, tol, max_iter):
  """
  Resuelve un sistema de ecuaciones lineales usando el método de Gauss-Seidel.

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
        if j < i:
          s += A[i,j] * x[j]
        elif j > i:
          s += A[i,j] * x0[j]
      x[i] = (b[i] - s) / A[i,i]

    # Criterio de convergencia
    if np.linalg.norm(x - x0) < tol:
        return x
    x0 = x.copy()
  return None

# Datos del problema
A = np.array([[52, 20, 25],
              [30, 50, 20],
              [18, 30, 55]])
b = np.array([4800, 5810, 5690])
x0 = np.zeros(3)  # Vector inicial
tol = 1e-6
max_iter = 100

# Aplicando Gauss-Seidel
x = gauss_seidel(A, b, x0, tol, max_iter)

if x is not None:
  print("La solución es:", x)
else:
  print("El método no convergió.")