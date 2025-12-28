# MHD-Beam-Propulsion-Sim

A simulation suite for MHD beam propulsion systems, modeling laser energy absorption for Lightcraft concepts.

## Overview

This repository contains a Python module for simulating laser energy deposition in a plasma, which is a key component of magnetohydrodynamic (MHD) beam propulsion systems. The initial release includes the `LaserDepositionModel` class, which provides a foundation for calculating absorption coefficients and deposited power.

## Installation

```bash
git clone https://github.com/ghellv2/MHD-Beam-Propulsion-Sim.git
cd MHD-Beam-Propulsion-Sim
```

No additional dependencies are required for the basic module.

## Usage

See `example.py` for a simple demonstration.

```python
from laser_model import LaserDepositionModel

# Initialize model with a 10.6 µm CO2 laser at 1 MW power
model = LaserDepositionModel(laser_wavelength=10.6e-6, power=1e6)

# Compute absorption coefficient for a typical plasma
alpha = model.absorption_coefficient(plasma_density=1e22, temperature=1e4)
print(f"Absorption coefficient: {alpha:.2e} m^-1")

# Estimate deposited power over 1 meter
deposited = model.deposited_power(distance=1.0, plasma_density=1e22, temperature=1e4)
print(f"Deposited power: {deposited:.2f} W")
```

## API Reference

### `LaserDepositionModel`

- `__init__(self, laser_wavelength, power)`: Initialize with laser wavelength (meters) and power (watts).
- `absorption_coefficient(self, plasma_density, temperature)`: Returns the absorption coefficient (m⁻¹) based on plasma density (m⁻³) and temperature (K).
- `deposited_power(self, distance, plasma_density, temperature)`: Returns the power deposited after traveling `distance` meters.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
