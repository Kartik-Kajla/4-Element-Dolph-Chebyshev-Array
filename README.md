2.4 GHz 4-Element Dolph–Chebyshev Microstrip Antenna Array
Overview

This repository documents the design and simulation of a 2.45 GHz 4-element Dolph–Chebyshev microstrip antenna array with a target sidelobe level (SLL) of −30 dB.

The project covers the complete engineering workflow, from designing a single microstrip patch antenna to developing a custom unequal Wilkinson feed network and finally integrating both into a complete antenna array.

Project Workflow
Stage 1 — Single Patch Antenna
Design of a 2.4 GHz inset-fed rectangular microstrip patch antenna.
Simulation and impedance matching using ANSYS HFSS.
Validation of S11 and radiation characteristics.

Stage 2 — Feed Network
MATLAB implementation of Dolph–Chebyshev excitation coefficients.
Conversion of excitation coefficients into required power ratios.
Design of equal and unequal Wilkinson power dividers.
EM and circuit co-simulation using Keysight ADS Momentum.

Stage 3 — Antenna Array (In Progress)
Integration of the feed network with six patch antennas.
Array optimization.
Radiation pattern analysis.
Gain, beamwidth, and sidelobe level evaluation.

Software Used
ANSYS HFSS
Keysight ADS Momentum
MATLAB
Design Specifications
Parameter	Value
Frequency	2.4 GHz
Array Type	6-Element Dolph–Chebyshev
Target SLL	−30 dB
Feed Network	Unequal Wilkinson Corporate Feed
Patch Type	Inset-fed Microstrip Patch
Repository Structure
Patch_Antenna/
Feed_Network/
Array/
References/
Current Progress
✅ Single Patch Antenna
✅ Unequal Wilkinson Feed Network
🚧 Complete Array Integration
⏳ Radiation Pattern Validation
References
Constantine A. Balanis — Antenna Theory: Analysis and Design
David M. Pozar — Microwave Engineering
Author

Kartik Kajla

Electronics and Communication Engineering

RF | Microwave Engineering | Antenna Design | Electromagnetics

# 6-Element-Dolph-Chebyshev-Array
Design and simulation of a 6-element Dolph-Chebyshev microstrip patch antenna array with -30 dB side lobe level using HFSS and ADS.

