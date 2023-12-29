import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
   z = 0
   n = 0
   while abs(z) <= 2 and n < max_iter:
       z = z**2 + c
       n += 1
   if n == max_iter:
       return max_iter
   return n + 1 - np.log(np.log2(abs(z)))

def mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter):
   x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
   X, Y = np.meshgrid(x, y)
   Z = X + 1j * Y
   fractal = np.zeros(Z.shape)

   for i in range(width):
       for j in range(height):
           fractal[i, j] = mandelbrot(Z[i, j], max_iter)

   return fractal

def plot_fractal(fractal):
   plt.imshow(fractal, cmap='viridis', extent=(x_min, x_max, y_min, y_max))
   plt.colorbar()
   plt.show()

# Параметры для построения фрактала Мандельброта
width, height = 800, 800
x_min, x_max = -2, 2
y_min, y_max = -2, 2
max_iter = 500

fractal = mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter)
plot_fractal(fractal)
