# uhfe_simulator/visualization.py

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import parameters as p

def plot_field(psi, title="ψ Field", save_path=None):
    """
    Render the magnitude of the ψ field in 2D or 3D.
    """
    abs_psi = np.abs(psi)

    if p.dimensions == 2:
        plt.figure(figsize=(6, 6))
        plt.imshow(abs_psi.T, origin='lower', cmap='plasma')
        plt.colorbar(label='|ψ|')
        plt.title(title)
        plt.xlabel("x")
        plt.ylabel("y")
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()
            plt.savefig("2d-test-output.png")

    elif p.dimensions == 3:
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        x, y, z = np.indices(psi.shape)
        magnitude = np.abs(psi)

        # Mask to highlight only significant wave peaks
        mask = magnitude > magnitude.mean()
        x, y, z, c = x[mask], y[mask], z[mask], magnitude[mask]

        ax.scatter(x, y, z, c=c, cmap='viridis', alpha=0.6, s=2)
        ax.set_title(title)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()
            plt.savefig("3d-test-output.png")
    else:
        raise NotImplementedError("Only 2D and 3D visualization supported.")
