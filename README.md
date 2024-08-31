# PlanarCoils_SkinDepth

This Python script calculates the skin depth for copper conductors at a given frequency, particularly in the context of coil design. It also advises on the copper thickness relative to the skin depth. The code uses well-known formulas for skin depth and accounts for factors like resistivity and permeability of copper.

## Dependencies

The following Python libraries are required to run this script:

- **numpy**: For numerical computations.
- **scipy.constants**: Provides fundamental constants like permeability (mu_0).
- **math**: Provides mathematical functions like square root, and constants like pi.
- **matplotlib.pyplot**: Imported but not currently utilized for plotting. It can be used to visualize coil parameters or results.
- **time**: For potential time-tracking, though currently unused in the script.

## Parameters and Functions

### Coil Parameters

- **outer_diameter**: The outer diameter of the coil, set to 6 mm (converted to meters).
- **width**: The width of the coil's conductor, set to 0.102 mm (converted to meters).
- **spacing**: The space between turns of the coil, set to 0.102 mm (converted to meters).
- **rotation**: A parameter to define the number of turns per layer, set to 1.
- **num_turns**: The total number of turns in the coil, set to 5.
- **num_coils**: The number of coil layers, set to 1.
- **shift**: The vertical distance between coil planes, set to 0.102 mm (converted to meters).
- **resolution**: Defines the resolution for possible plotting or further calculations, currently set to 1.

### Skin Depth Calculation

- **`skin_depth(frequency, copper_thickness)`**: Calculates the skin depth of a conductor at a specified frequency, based on the electrical resistivity of copper (1.68e-8 ohm-m) and the magnetic permeability of free space (4 * pi * 10^-7 H/m).

#### Input Parameters

- **frequency**: The frequency of operation in Hertz (set to 0.75 MHz in the script).
- **copper_thickness**: The thickness of the copper conductor in meters (set to 35 micrometers or 35e-6 meters).

#### Outputs

- **delta**: The calculated skin depth in meters.
- **skin_depths**: The number of skin depths that fit within the given copper thickness.

### Output

- The script prints the calculated skin depth for copper at a frequency of 0.75 MHz in micrometers.
- It also advises the number of skin depths that fit within the given copper thickness.
- Suggests that the copper thickness should ideally be less than half of the skin depth for effective current conduction.

### Example Output

For a 0.75 MHz frequency and a copper thickness of 35 micrometers:
- **Skin depth** at 0.75 MHz for copper is 75.55 micrometers.
- **Number of skin depths** is: 0.46 - Advised copper thickness less than: 37.77 micrometers.

## Future Improvements

- **Visualization**: Utilize `matplotlib` to plot the relationship between frequency and skin depth.
- **Time Tracking**: Use the `time` module to measure the performance or execution time of the script.
- **Coil Design Extension**: Expand the current coil parameters to compute inductance, resistance, and other properties based on the geometric configuration.

## Usage

This script is useful for RF engineers and electrical designers who need to calculate the appropriate copper thickness for coils or traces operating at high frequencies, ensuring optimal current conduction while minimizing losses due to the skin effect.

## Licence

This project is licensed under the MIT License. See the LICENSE file for details.
