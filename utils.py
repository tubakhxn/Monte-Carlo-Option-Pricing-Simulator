import numpy as np
from scipy.stats import norm

# Geometric Brownian Motion simulation
def simulate_gbm_paths(S0, r, sigma, T, steps, n_paths):
    dt = T / steps
    t = np.linspace(0, T, steps + 1)
    paths = np.zeros((n_paths, steps + 1))
    paths[:, 0] = S0
    for i in range(n_paths):
        W = np.random.standard_normal(steps)
        W = np.cumsum(W) * np.sqrt(dt)
        X = (r - 0.5 * sigma ** 2) * t[1:] + sigma * W
        paths[i, 1:] = S0 * np.exp(X)
    return t, paths

# Monte Carlo European Option Pricing
def monte_carlo_option_price(paths, K, r, T, option_type='call'):
    S_T = paths[:, -1]
    if option_type == 'call':
        payoff = np.maximum(S_T - K, 0)
    else:
        payoff = np.maximum(K - S_T, 0)
    price = np.exp(-r * T) * np.mean(payoff)
    return price

# Black-Scholes Analytical Price
def black_scholes_price(S0, K, r, sigma, T, option_type='call'):
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == 'call':
        price = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
    return price
