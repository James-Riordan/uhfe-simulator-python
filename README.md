# UHFE Simulator

A modular simulation of the **Unified Harmonic Field Equation (UHFE)** — modeling the universe as a recursive, nonlinear, phase-coherent harmonic field. Inspired by the work of Milo Wolff, Ray Tomes, Gabriel LaFrenière, Nikola Tesla, and others.

---

## 🧠 What is UHFE?

UHFE models the universe as a self-organizing ψ field evolving through:

\[
\not{D}_M \psi + \lambda C[\psi] + \kappa |\psi|^2 \psi + \beta T[\psi] + \gamma \nabla^2 \psi = 0
\]

- Dirac-Harmonic structure & spin
- Nonlinear soliton emergence
- Coherent phase-locking
- Topological memory persistence
- Recursive scalar field evolution

---

## 💻 Features

- Modular design: fields, core, simulation, GUI, audio
- 1D, 2D, 3D field evolution with toroidal/spherical domains
- Real-time GUI and audio sonification
- Ready for rhombic dodecahedral lattice simulation
- Docker + Pipenv support

---

## 🚀 Quick Start

### 🔧 Local Run

```bash
pip install pipenv
pipenv install
pipenv run python main.py
```

Or Launch GUI:

```bash
pipenv run python -m uhfe_simulator.gui
```

### Docker

```bash
docker build -t uhfe-sim .
docker run -it --rm uhfe-sim
```

---

## 📁 Structure

```bash
uhfe_simulator/
├── core.py            # UHFE evolution logic
├── fields.py          # ψ field & Laplacian (torus/sphere)
├── simulation.py      # Time control
├── visualization.py   # 2D/3D ψ field rendering
├── gui.py             # Interactive simulation
├── input_output.py    # Save/load states
├── audio.py           # Sonification
├── parameters.py      # Config + fidelity controls
├── geometry.py        # Rhombic dodecahedron lattice
├── utils.py           # φ tools, phase wrapping
```

## 🧠 Credits

Made by James Riordan — Harmonizing reality through waveform.