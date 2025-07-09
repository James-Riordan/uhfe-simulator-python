import numpy as np

# Golden Ratio (φ)
phi = (1 + np.sqrt(5)) / 2

def golden_ratio_approx(n):
    """
    Return the ratio of Fibonacci(n+1) / Fibonacci(n).
    Approaches φ as n increases.
    """
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return b / a

def normalize_field(psi):
    """
    Normalize ψ field magnitude to range [-1, 1].
    """
    mag = np.abs(psi)
    max_val = np.max(mag) + 1e-12
    return psi / max_val

def wrap_phase(psi):
    """
    Return wrapped phase angle of ψ in range [-π, π].
    """
    return np.angle(psi)
