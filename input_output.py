import numpy as np
import os

def save_field(psi_field, filename="psi_field.npy", directory="data"):
    """
    Save the current ψ field to a .npy file.
    """
    os.makedirs(directory, exist_ok=True)
    full_path = os.path.join(directory, filename)
    np.save(full_path, psi_field)
    print(f"ψ field saved to {full_path}")

def load_field(filename="psi_field.npy", directory="data"):
    """
    Load a ψ field from a .npy file.
    """
    full_path = os.path.join(directory, filename)
    if os.path.exists(full_path):
        psi = np.load(full_path)
        print(f"ψ field loaded from {full_path}")
        return psi
    else:
        raise FileNotFoundError(f"No saved field at: {full_path}")
