
import numpy as np
import matplotlib.pyplot as plt

# Number of points
n = 20000

inside = 0
pi_estimates = []

for i in range(1, n + 1):
    x, y = np.random.uniform(0, 1, 2)
    if x**2 + y**2 <= 1:
        inside += 1
    pi_estimates.append(4 * inside / i)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(pi_estimates, label="Estimated π")
plt.axhline(np.pi, color="red", linestyle="--", label="True π")
plt.xlabel("Number of Points")
plt.ylabel("π Value")
plt.title("Monte Carlo Estimation of π")
plt.legend()
plt.grid()

# Save figure
plt.savefig("results/figures/pi_estimation.png")
plt.show()
