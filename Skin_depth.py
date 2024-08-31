import numpy as np
from scipy.constants import mu_0, pi
import math
import time
import matplotlib.pyplot as plt

# Coil parameters
outer_diameter = 6/ 1000  # 6 mm in meters
width = 0.102 / 1000  # 0.102 mm in meters
spacing = 0.102/ 1000  # 0.102 mm in meters
rotation = 1
num_turns = 5
num_coils = 1
shift = 0.102 / 1000  # distance between coil planes
resolution = 1

def skin_depth(frequency, copper_thickness):
    resistivity_copper = 1.68e-8
    permeability = 4 * math.pi * 10 ** -7
    omega = 2 * math.pi * frequency
    delta = math.sqrt(2 * resistivity_copper / (omega * permeability))
    skin_depths = copper_thickness / delta
    return delta, skin_depths


frequency = 0.75e6  # 1 MHz
copper_thickness = 35e-6
skin_depth_value, skin_depths = skin_depth(frequency, copper_thickness)
print(f"Skin depth at {frequency*1e-6:.4} MHz for copper is {skin_depth_value * 1e6:.2f} micrometers")
print(f'Number of skin depths is: {skin_depths:.2} - Advised copper thickness less than: {0.5*skin_depth_value*1e6:.4} micrometers')
