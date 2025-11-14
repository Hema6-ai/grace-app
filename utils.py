import numpy as np

def generate_population(num_points):
    Jso = 0.03 + 0.03 * np.random.rand(num_points)
    Jto = 0.44 + 0.05 * np.random.rand(num_points)
    return Jso, Jto

def generate_pareto_curve(id):
    np.random.seed(id)
    deg = np.arange(1, 61)
    error = (1e-3 + id*3e-4) * np.exp(deg/80) + 1e-4*np.random.randn(60)
    return deg, np.abs(error)

def generate_degree_variance(constellation_id):
    np.random.seed(constellation_id)
    deg = np.arange(1, 61)
    error = (1e-3 + constellation_id*2e-4) * np.exp(deg/100) + 1e-4*np.random.randn(60)
    return deg, np.abs(error)
