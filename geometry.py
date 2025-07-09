# uhfe_simulator/geometry.py

import numpy as np
from scipy.spatial import cKDTree

def generate_rhombic_dodecahedron_lattice(n=10, spacing=1.0):
    """
    Generate 3D rhombic dodecahedral lattice using FCC unit cells.
    Returns Nx3 array of 3D points.
    """
    a = spacing
    basis = np.array([
        [0, 0, 0],
        [0.5, 0.5, 0],
        [0.5, 0, 0.5],
        [0, 0.5, 0.5]
    ]) * a

    positions = []
    grid_range = range(-n, n + 1)

    for i in grid_range:
        for j in grid_range:
            for k in grid_range:
                for b in basis:
                    point = np.array([i, j, k]) * a + b
                    positions.append(point)

    return np.array(positions)

def find_neighbors(positions, radius=1.01):
    """
    Return a neighbor adjacency list for each point in the lattice.
    """
    tree = cKDTree(positions)
    adjacency = [tree.query_ball_point(pos, r=radius) for pos in positions]
    return adjacency
