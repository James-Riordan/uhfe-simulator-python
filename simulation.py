from uhfe_simulator.fields import PsiField
from uhfe_simulator.core import update_field
from uhfe_simulator import parameters as p

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
        self.psi_field.initialize_random(amplitude=0.05)

    def step(self):
        """
        Advance the ψ field by one timestep.
        """
        update_field(self.psi_field)
        self.time += p.time_step
        self.step_count += 1

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
