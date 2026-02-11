# Monte Carlo Option Pricing Simulator

## What is this project about?
This project is a professional simulator for pricing European Call and Put options using Monte Carlo methods. It simulates stock price paths with Geometric Brownian Motion, compares Monte Carlo prices to Black-Scholes analytical prices, and visualizes the results with animated plots. Designed for finance, education, and research.

## Developer / Creator
**tubakhxn**


## Features
- Simulate stock price paths using GBM
- Price European Call and Put options via Monte Carlo
- Calculate Black-Scholes analytical price
- Visualize animated stock price paths and option prices
- Clean, professional dark theme

## Project Structure
- `main.py`: Entry point, handles simulation, visualization, and comparison
- `utils.py`: Contains GBM simulation and pricing functions
- `requirements.txt`: Python dependencies
- `README.md`: Project documentation and formulas

## Formulas

### Geometric Brownian Motion (GBM)
Stock price evolution:
$$
S_t = S_0 \exp\left((r - 0.5\sigma^2)t + \sigma W_t\right)
$$
Where:
- $S_t$: Stock price at time $t$
- $S_0$: Initial stock price
- $r$: Risk-free rate
- $\sigma$: Volatility
- $W_t$: Wiener process (Brownian motion)

### Black-Scholes Formula
European Call:
$$
C = S_0 N(d_1) - K e^{-rt} N(d_2)
$$
European Put:
$$
P = K e^{-rt} N(-d_2) - S_0 N(-d_1)
$$
Where:
$$
d_1 = \frac{\ln(S_0/K) + (r + 0.5\sigma^2)t}{\sigma\sqrt{t}}
$$
$$
d_2 = d_1 - \sigma\sqrt{t}
$$
- $N(\cdot)$: Cumulative distribution function of the standard normal distribution
- $K$: Strike price
- $t$: Time to maturity

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the simulator:
   ```bash
   python main.py
   ```

## Parameters
- Strike price
- Volatility
- Risk-free rate
- Time to maturity

All parameters are labeled and visualized in the plot.

## License
MIT
