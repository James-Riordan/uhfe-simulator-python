import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

from simulation import UHFESimulation
import parameters as p

class UHFESimulatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("UHFE Simulator")

        # Setup simulation
        self.sim = UHFESimulation()
        self.sim.initialize()

        # Setup Matplotlib figure
        self.fig, self.ax = plt.subplots(figsize=(5, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=0, column=0, columnspan=3)

        # Control buttons
        self.step_button = ttk.Button(master, text="Step", command=self.step)
        self.step_button.grid(row=1, column=0)

        self.run_button = ttk.Button(master, text="Run 50 Steps", command=lambda: self.run(50))
        self.run_button.grid(row=1, column=1)

        self.quit_button = ttk.Button(master, text="Quit", command=self.master.quit)
        self.quit_button.grid(row=1, column=2)

        # Initial visualization
        self.update_plot()

    def step(self):
        self.sim.step()
        self.update_plot()

    def run(self, steps):
        self.sim.run(steps)
        self.update_plot()

    def update_plot(self):
        self.ax.clear()
        field = self.sim.get_field_snapshot()

        if p.dimensions == 2:
            im = self.ax.imshow(np.abs(field).T, origin='lower', cmap='plasma')
            self.fig.colorbar(im, ax=self.ax)
        else:
            self.ax.text(0.5, 0.5, "3D View not yet supported in GUI", ha='center')

        self.canvas.draw()
