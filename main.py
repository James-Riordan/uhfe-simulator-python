from uhfe_simulator.simulation import UHFESimulation
from uhfe_simulator.visualization import plot_field
from uhfe_simulator import parameters as p

def main():
    sim = UHFESimulation()
    sim.initialize()

    print(f"Running UHFE simulation for {100} steps...")
    sim.run(steps=100)

    field_snapshot = sim.get_field_snapshot()
    plot_field(field_snapshot, title="UHFE Simulation Result")

if __name__ == "__main__":
    main()
