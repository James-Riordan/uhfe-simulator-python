from simulation import UHFESimulation
from visualization import plot_field
# import parameters as p


def main():
    sim = UHFESimulation()
    sim.initialize()

    print(f"Running UHFE simulation for {100} steps...")
    sim.run(steps=1000)

    field_snapshot = sim.get_field_snapshot()
    plot_field(field_snapshot, title="UHFE Simulation Result")

if __name__ == "__main__":
    main()
