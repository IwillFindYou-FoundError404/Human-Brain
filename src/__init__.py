# src/__init__.py

from .connectome import HumanConnectome
from .neuromodulation import NeuromodulationSystem
from .simulator import SpikingNeuralSimulator

# Định nghĩa các Class được phép xuất bản khi dùng lệnh "from src import *"
__all__ = [
    "HumanConnectome",
    "NeuromodulationSystem",
    "SpikingNeuralSimulator"
]

__version__ = "1.0.0"
__author__ = "Your Name"
