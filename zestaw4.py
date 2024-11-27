import numpy as np
import matplotlib.pyplot as plt

def trapez(x):
    if -1 <= x < 0:
        return (1/3) * (x + 1)
    elif 0 <= x < 2:
        return 1/3
    elif 2 <= x <= 3:
        return (1/3) * (3 - x)
    else:
        return 0


def generate_trapezoidal_random_numbers(n):
    samples = []

    while len(samples) < n:
        x = np.random.uniform(-1, 3)
        y = np.random.uniform(0, 1/3)
        if y < trapez(x):
            samples.append(x)

    return np.array(samples)

def plot_histogram_and_fgp(samples, num_bins=50):
    # Rysowanie histogramu eksperymentalnej funkcji gęstości prawdopodobieństwa (FGP)
    plt.hist(samples, bins=num_bins, density=True, alpha=0.6, color='b', label='Eksperymentalna FGP')

    # Generowanie punktów do wykresu teoretycznej FGP
    x = np.linspace(-1, 3, 1000)
    y = np.array([trapez(xi) for xi in x])
    
    # Rysowanie teoretycznej funkcji gęstości prawdopodobieństwa (FGP)
    plt.plot(x, y, 'r-', lw=2, label='Teoretyczna FGP')

    plt.xlabel('x')
    plt.ylabel('Gęstość')
    
    plt.title(f'Porównanie eksperymentalnej i teoretycznej FGP (n = {len(samples)})')
    
    plt.legend()
    plt.show()

sample_sizes = [10**3, 10**5]
for size in sample_sizes:
    samples = generate_trapezoidal_random_numbers(size)
    plot_histogram_and_fgp(samples)
