# UHFE field constants
kappa = 1.0 # 1.0       # Nonlinear self-focusing term (|ψ|²ψ)
lambda_ = 0.5 # 0.5     # Coherence-locking operator strength (C[ψ])
beta = 0.2 # 0.3        # Topological memory persistence (T[ψ])
gamma = 0.3  # 0.1       # Laplacian smoothing term (∇²ψ)

# Dirac-Harmonic operator placeholder (optional scaling)
dirac_scale = 0.5

# Simulation control
time_step = 0.0005
grid_size = 100
spatial_resolution = 1.0
dimensions = 2  # Options: 1, 2, or 3

# Domain shape: 'cube', 'sphere', 'torus', 'flower_of_life'
domain_shape = 'torus'

# Grid geometry: 'cartesian', 'rhombic'
grid_geometry = 'cartesian'

# Fidelity and performance controls
max_recursion_depth = 3       # Used for T[ψ] and future topology
max_neighbor_radius = 1.01    # For harmonic adjacency graphs
precision_mode = 'float32'    # Use 'float64' for high precision

# Fidelity presets (manual override, optional CLI later)
fidelity_level = 'medium'     # Options: 'low', 'medium', 'high', 'max'
