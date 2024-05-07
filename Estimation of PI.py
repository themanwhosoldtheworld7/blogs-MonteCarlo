#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Monte Carlo Estimation of Pi.
This script demonstrates estimating the value of Pi using the Monte Carlo method
by simulating random points within a square and counting those within a circumscribed circle.

Created on Sat Apr 20, 2024
@author: ainishlodaya
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_random_points(num_trials):
    """Generate random points within the square from -1 to 1 for both coordinates."""
    x = np.random.uniform(-1, 1, num_trials)
    y = np.random.uniform(-1, 1, num_trials)
    return x, y

def calculate_distances(x, y):
    """Calculate distances of points from the origin."""
    return np.sqrt(x**2 + y**2)

def estimate_pi(num_trials):
    """Estimate the value of Pi using the Monte Carlo method."""
    x, y = generate_random_points(num_trials)
    distances = calculate_distances(x, y)
    inside_circle = distances <= 1
    return 4 * np.sum(inside_circle) / num_trials

def plot_results(x, y, inside_circle, pi_estimate, num_trials):
    """Create a scatter plot showing the estimation process and results."""
    plt.figure(figsize=(6, 6))
    plt.scatter(x[inside_circle], y[inside_circle], color='red', s=1)
    plt.scatter(x[~inside_circle], y[~inside_circle], color='blue', s=1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Monte Carlo Estimation of Pi with {num_trials} Trials\nEstimated Pi = {pi_estimate:.4f}")
    plt.xlabel('X coordinate')
    plt.ylabel('Y coordinate')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.grid(True)
    plt.show()

def main():
    trials = [10, 100, 1000, 10000, 1000000]
    for num_trials in trials:
        pi_estimate = estimate_pi(num_trials)
        x, y = generate_random_points(num_trials)
        distances = calculate_distances(x, y)
        inside_circle = distances <= 1
        plot_results(x, y, inside_circle, pi_estimate, num_trials)

if __name__ == "__main__":
    main()
