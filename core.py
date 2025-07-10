import numpy as np
import parameters as p
from fields import PsiField

def compute_coherence(psi):
    """
    Coherence-locking operator C[ψ].
    Encourages local phase alignment (placeholder).
    """
    return np.conj(psi) * np.abs(psi)

def compute_topological_memory(psi):
    """
    Topological memory operator T[ψ].
    Placeholder — could evolve into recursive field history or knot memory.
    """
    return np.copy(psi)  # Flat memory for now

def update_field(psi_field: PsiField):
    """
    Evolve the ψ field forward by one UHFE time step.

    ∂ψ/∂t = -1j [ λC[ψ] + κ|ψ|²ψ + βT[ψ] + γ∇²ψ ]
    """
    ψ = psi_field.psi
    dt = p.time_step

    # --- UHFE operator terms ---
    lap = psi_field.laplacian()
    coherence_term = compute_coherence(ψ)
    nonlinear_term = np.abs(ψ)**2 * ψ
    memory_term = compute_topological_memory(ψ)

    # --- Optional harmonic potential (helps trap dynamics in center) ---
    if p.domain_shape == "sphere":
        coords = [np.linspace(-1, 1, s) for s in ψ.shape]
        grid = np.meshgrid(*coords, indexing='ij')
        r_squared = sum((g**2 for g in grid))
        potential = r_squared  # harmonic potential V(r) = r²
        potential_term = potential * ψ
    else:
        potential_term = 0

    # --- Combine UHFE equation terms ---
    dψ_dt = -1j * (
        p.lambda_ * coherence_term +
        p.kappa * nonlinear_term +
        p.beta * memory_term +
        p.gamma * lap +
        p.dirac_scale * potential_term  # optional V(x)ψ contribution
    )

    # --- Euler time integration ---
    ψ_next = ψ + dt * dψ_dt

    # --- Optional: soft limit to suppress blowup (REMOVE later) ---
    max_val = np.max(np.abs(ψ_next))
    if max_val > 10.0:
        ψ_next *= (10.0 / max_val)

    # --- Commit update ---
    psi_field.psi_next = ψ_next
    psi_field.psi = np.copy(ψ_next)
    psi_field.clear_next()

