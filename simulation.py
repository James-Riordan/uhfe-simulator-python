from fields import PsiField
from core import update_field
import parameters as p
import numpy as np

class UHFESimulation:
    """
    High-level simulation engine to manage time evolution.
    """
    def __init__(self):
        self.psi_field = PsiField()
        self.time = 0.0
        self.step_count = 0

    def initialize(self):
        """
        Initialize the ψ field with small complex noise.
        """
        # self.psi_field.initialize_random(amplitude=0.05)
        self.psi_field.initialize_gaussian_blob(amplitude=1.0, width=0.2)

    def step(self):
        """
        Advance the ψ field by one timestep and print summary diagnostics.
        """
        update_field(self.psi_field)
        self.time += p.time_step
        self.step_count += 1

        # Diagnostics
        psi = self.psi_field.psi
        abs_psi = np.abs(psi)
        total_energy = np.sum(abs_psi**2)
        max_amp = np.max(abs_psi)
        mean_amp = np.mean(abs_psi)
        std_amp = np.std(abs_psi)

        print(f"[step {self.step_count:03d}] t = {self.time:.3f}  ||ψ||² = {total_energy:.4f}  "
            f"max|ψ| = {max_amp:.4f}  mean|ψ| = {mean_amp:.4f}  std|ψ| = {std_amp:.4f}")


    def run(self, steps=100):
        """
        Run the simulation for a fixed number of timesteps.
        """
        for _ in range(steps):
            self.step()

    def get_field_snapshot(self):
        """
        Get the current ψ field state.
        """
        return self.psi_field.psi.copy()
