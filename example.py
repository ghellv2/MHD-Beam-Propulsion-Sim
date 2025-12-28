#!/usr/bin/env python3
"""
Example usage of the LaserDepositionModel for MHD beam propulsion simulation.
"""

from laser_model import LaserDepositionModel


def main():
    """Demonstrate basic usage of the laser deposition model."""
    # Initialize model with a 10.6 µm CO2 laser at 1 MW power
    model = LaserDepositionModel(
        laser_wavelength=10.6e-6,  # meters
        power=1e6                  # watts
    )
    print(f"Model: {model}")
    
    # Plasma parameters (typical for laser‑sustained plasma)
    plasma_density = 1e22          # electron number density [m^-3]
    temperature = 1e4              # electron temperature [K]
    
    # Compute absorption coefficient
    alpha = model.absorption_coefficient(plasma_density, temperature)
    print(f"Absorption coefficient: {alpha:.2e} m^-1")
    
    # Estimate deposited power over 1 meter
    distance = 1.0                 # meters
    deposited = model.deposited_power(distance, plasma_density, temperature)
    print(f"Deposited power after {distance} m: {deposited:.2f} W")
    
    # Show fraction of power absorbed
    fraction = (model.power - deposited) / model.power
    print(f"Fraction absorbed: {fraction:.2%}")


if __name__ == "__main__":
    main()
