"""
The package provides a Space Imaging Simulator for Proximity Operations (SISPO)

The package creates images of a 3D object using blender. The images are render
in a flyby scenario. UCAC4 star catalogue to create the background. Afterwards
hese images are used with openMVG and openMVS to reconstruct the 3D model and
reconstruct the trajectory.
"""

from pathlib import Path

import simulation.simulation as sim
import reconstruction.reconstruction as rc
import compression.compression as comp
import utils

import matplotlib.pyplot as plt

if __name__ == "__main__":
    env = sim.Environment("Didymos", 20)
    env.simulate()
    env.render()
