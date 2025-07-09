import numpy as np
from uhfe_simulator import parameters as p

class PsiField:
    """
    Core object representing the ψ field grid and evolution interface.
    """
    def __init__(self, grid_shape=(p.grid_size,) * p.dimensions):
        self.grid_shape = grid_shape
        dtype = np.complex64 if p.precision_mode == 'float32' else np.complex128
        self.psi = np.zeros(grid_shape, dtype=dtype)
        self.psi_next = np.zeros_like(self.psi)

    def initialize_random(self, amplitude=1.0):
        """
        Random complex initialization to break symmetry.
        """
        real = (np.random.rand(*self.grid_shape) - 0.5) * 2 * amplitude
        imag = (np.random.rand(*self.grid_shape) - 0.5) * 2 * amplitude
        self.psi = real + 1j * imag

    def clear_next(self):
        self.psi_next = np.zeros_like(self.psi)

    def laplacian(self):
        """
        Toroidal or spherical finite difference Laplacian (1D, 2D, 3D).
        """
        lap = np.zeros_like(self.psi)
        psi = self.psi
        shape = psi.shape

        if p.dimensions == 1:
            lap[1:-1] = psi[:-2] - 2 * psi[1:-1] + psi[2:]

        elif p.dimensions == 2:
            for i in range(shape[0]):
                for j in range(shape[1]):
                    lap[i, j] = (
                        psi[(i - 1) % shape[0], j] +
                        psi[(i + 1) % shape[0], j] +
                        psi[i, (j - 1) % shape[1]] +
                        psi[i, (j + 1) % shape[1]] -
                        4 * psi[i, j]
                    )

        elif p.dimensions == 3:
            for i in range(shape[0]):
                for j in range(shape[1]):
                    for k in range(shape[2]):
                        lap[i, j, k] = (
                            psi[(i - 1) % shape[0], j, k] +
                            psi[(i + 1) % shape[0], j, k] +
                            psi[i, (j - 1) % shape[1], k] +
                            psi[i, (j + 1) % shape[1], k] +
                            psi[i, j, (k - 1) % shape[2]] +
                            psi[i, j, (k + 1) % shape[2]] -
                            6 * psi[i, j, k]
                        )

        if p.domain_shape == "sphere":
            center = tuple(s // 2 for s in shape)
            radius = min(shape) // 2
            for index, _ in np.ndenumerate(psi):
                dist = np.sqrt(sum((ix - cx)**2 for ix, cx in zip(index, center)))
                if dist > radius:
                    lap[index] = 0

        return lap
