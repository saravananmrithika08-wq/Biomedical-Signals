# ECG Signal Plotter and Analyser
# Mrithika — Biomedical Engineering Student
# Simulates and analyses a basic ECG waveform using Python

import numpy as np
import matplotlib.pyplot as plt

# --- Generate Simulated ECG Signal ---
def generate_ecg(duration=5, fs=500):
    """
    Simulates a basic ECG waveform
    duration: length in seconds
    fs: sampling frequency in Hz
    """
    t = np.linspace(0, duration, duration * fs)
    
    # Simulate ECG using sine waves (simplified model)
    ecg = np.zeros(len(t))
    
    # Heart rate: 75 bpm = 1.25 Hz
    hr = 1.25
    
    for i, time in enumerate(t):
        # P wave
        ecg[i] += 0.25 * np.exp(-((time % (1/hr) - 0.1) ** 2) / 0.001)
        # QRS complex
        ecg[i] += 1.50 * np.exp(-((time % (1/hr) - 0.3) ** 2) / 0.0002)
        # T wave
        ecg[i] += 0.35 * np.exp(-((time % (1/hr) - 0.5) ** 2) / 0.004)
    
    return t, ecg

# --- Add Noise ---
def add_noise(ecg, noise_level=0.05):
    noise = noise_level * np.random.randn(len(ecg))
    return ecg + noise

# --- Plot ECG ---
def plot_ecg(t, ecg_clean, ecg_noisy):
    fig, axes = plt.subplots(2, 1, figsize=(12, 6))
    
    # Clean ECG
    axes[0].plot(t, ecg_clean, color='green', linewidth=1.5)
    axes[0].set_title('Simulated ECG — Clean Signal')
    axes[0].set_xlabel('Time (seconds)')
    axes[0].set_ylabel('Amplitude (mV)')
    axes[0].grid(True, alpha=0.3)
    axes[0].set_xlim(0, 5)
    
    # Noisy ECG
    axes[1].plot(t, ecg_noisy, color='red', linewidth=1, alpha=0.8)
    axes[1].set_title('Simulated ECG — With Noise')
    axes[1].set_xlabel('Time (seconds)')
    axes[1].set_ylabel('Amplitude (mV)')
    axes[1].grid(True, alpha=0.3)
    axes[1].set_xlim(0, 5)
    
    plt.suptitle('ECG Signal Analysis — Mrithika S, BME Student', 
                 fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig('ecg_output.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("ECG plot saved as ecg_output.png")

# --- Main ---
print("=== ECG Signal Analyser ===")
print("Generating simulated ECG...")

t, ecg_clean = generate_ecg(duration=5, fs=500)
ecg_noisy = add_noise(ecg_clean, noise_level=0.05)

print(f"Signal duration: 5 seconds")
print(f"Sampling frequency: 500 Hz")
print(f"Simulated heart rate: 75 bpm")

plot_ecg(t, ecg_clean, ecg_noisy)
