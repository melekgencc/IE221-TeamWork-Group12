import numpy as np
import matplotlib.pyplot as plt

# Number of samples
n = 10000

# Generate Uniform(0,1) samples
X = np.random.uniform(0, 1, n)

# Cumulative mean
cumulative_mean = np.cumsum(X) / np.arange(1, n + 1)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(cumulative_mean, label="Cumulative Mean")
plt.axhline(0.5, color="red", linestyle="--", label="μ = 0.5")
plt.xlabel("Number of Observations (n)")
plt.ylabel("Sample Mean")
plt.title("SLLN Simulation (Uniform[0,1])")
plt.legend()
plt.grid()

# Save figure
plt.savefig("results/figures/slln_convergence.png")
plt.show()
