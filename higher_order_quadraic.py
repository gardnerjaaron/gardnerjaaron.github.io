import numpy as np
import matplotlib.pyplot as plt

# Higher-Order Quadratic RGB function
def higher_order_rgb(iter_normal, color_mut):
    r = (color_mut[0] * (1 - iter_normal) * iter_normal**3 * 255)%256
    g = (color_mut[1] * (1 - iter_normal) * iter_normal**2 * 255)%256
    b = (color_mut[2] * (1 - iter_normal) * iter_normal * 255)%256
    return r, g, b

# Normalized iteration values and scaling factors
iter_normals = np.linspace(0, 1, 500)
color_mut = [15, 8.5, 4]

# Calculate RGB values
higher_order_r, higher_order_g, higher_order_b = higher_order_rgb(iter_normals, color_mut)

# Plot Higher-Order Quadratic Color Weighting
plt.figure(figsize=(10, 5))
plt.plot(iter_normals, higher_order_r, label="Red", color="red")
plt.plot(iter_normals, higher_order_g, label="Green", color="green")
plt.plot(iter_normals, higher_order_b, label="Blue", color="blue")
plt.title("Higher-Order Quadratic Color Weighting")
plt.xlabel("Normalized Iteration Value")
plt.ylabel("Color Intensity")
plt.legend()
plt.grid()
plt.show()
