import numpy as np
import scipy.io.wavfile as wav
import os

def psi_to_audio(psi, sample_rate=44100, duration=2.0, filename="psi_sound.wav"):
    """
    Convert a 1D or 2D ψ field to a mono audio waveform.
    Uses magnitude or averaged slice.
    """
    audio_dir = "audio"
    os.makedirs(audio_dir, exist_ok=True)

    # Use 1D projection: average over rows/columns if 2D
    if psi.ndim == 2:
        signal = np.mean(np.abs(psi), axis=0)
    elif psi.ndim == 1:
        signal = np.abs(psi)
    else:
        raise NotImplementedError("Only 1D or 2D ψ fields can be sonified.")

    # Normalize signal
    signal = signal - np.mean(signal)
    signal = signal / np.max(np.abs(signal))
    signal = np.tile(signal, int(sample_rate * duration / len(signal)))

    # Convert to 16-bit PCM audio
    audio = np.int16(signal * 32767)
    filepath = os.path.join(audio_dir, filename)
    wav.write(filepath, sample_rate, audio)
    print(f"Audio written to: {filepath}")
