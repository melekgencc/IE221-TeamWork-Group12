
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Parameters
mu = 0.5
sigma = np.sqrt(1 / 12)
m = 1000
n_values = [2, 5, 10, 30, 50]

# Histograms
plt.figure(figsize=(12, 8))

for i, n in enumerate(n_values):
    sums = np.sum(np.random.uniform(0, 1, (m, n)), axis=1)
    z = (sums - n * mu) / (sigma * np.sqrt(n))

    plt.subplot(3, 2, i + 1)
    plt.hist(z, bins=30, density=True, alpha=0.7)
    x = np.linspace(-4, 4, 200)
    plt.plot(x, stats.norm.pdf(x), 'r')
    plt.title(f"n = {n}")

plt.tight_layout()
plt.savefig("results/figures/clt_histograms.png")
plt.show()

# Q-Q plots
plt.figure(figsize=(10, 6))
for n in n_values:
    sums = np.sum(np.random.uniform(0, 1, (m, n)), axis=1)
    z = (sums - n * mu) / (sigma * np.sqrt(n))
    stats.probplot(z, dist="norm", plot=plt)

plt.title("CLT Normal Q-Q Plots")
plt.savefig("results/figures/clt_qqplots.png")
plt.show()
