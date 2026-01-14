import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Fix seed for reproducibility
np.random.seed(42)

# ===================== SLLN =====================
def slln(data, true_mean, title):
    cumulative_mean = np.cumsum(data) / np.arange(1, len(data) + 1)

    plt.figure()
    plt.plot(cumulative_mean, label="Sample Mean")

    if true_mean is not None:
        plt.axhline(true_mean, linestyle="--", label="True Mean")

    plt.title(f"SLLN - {title}")
    plt.xlabel("n")
    plt.ylabel("Cumulative Mean")
    plt.legend()
    plt.show()


# ===================== CLT =====================
def clt(generator, mean, std, title):
    n_values = [2, 5, 10, 30, 50, 100]
    m = 1000

    for n in n_values:
        sums = np.array([np.sum(generator(n)) for _ in range(m)])
        z = (sums - n * mean) / (np.sqrt(n) * std)

        # Histogram
        plt.figure()
        plt.hist(z, bins=30, density=True)
        plt.title(f"CLT Histogram - {title} (n={n})")
        plt.xlabel("Standardized Sum")
        plt.ylabel("Density")
        plt.show()

        # Q-Q plot
        plt.figure()
        stats.probplot(z, dist="norm", plot=plt)
        plt.title(f"Q-Q Plot - {title} (n={n})")
        plt.show()


# ===================== SIMULATIONS =====================
N = 10000

# -------- Uniform(0,1) --------
uniform_data = np.random.uniform(0, 1, N)
slln(uniform_data, 0.5, "Uniform(0,1)")
clt(lambda n: np.random.uniform(0, 1, n), 0.5, np.sqrt(1/12), "Uniform(0,1)")

# -------- Exponential(λ=1) --------
exp_data = np.random.exponential(1, N)
slln(exp_data, 1, "Exponential(λ=1)")
clt(lambda n: np.random.exponential(1, n), 1, 1, "Exponential(λ=1)")

# -------- Pareto α=3 --------
pareto3_data = np.random.pareto(3, N) + 1
slln(pareto3_data, 1.5, "Pareto(α=3)")
clt(lambda n: np.random.pareto(3, n) + 1, 1.5, np.sqrt(0.75), "Pareto(α=3)")

# -------- Pareto α=1.5 (NO CLT) --------
pareto15_data = np.random.pareto(1.5, N) + 1
slln(pareto15_data, 3, "Pareto(α=1.5)")

# -------- Cauchy (NO SLLN & CLT) --------
cauchy_data = np.random.standard_cauchy(N)
slln(cauchy_data, None, "Cauchy Distribution")
