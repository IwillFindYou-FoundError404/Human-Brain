# src/subcortex/hippocampus_memory.py
import numpy as np
from src.core.bio_neuron import LeakyIntegrateAndFireGroup

class HippocampusMemory:
    """
    Vùng Hải mã. Lưu giữ ký ức bằng cách thay đổi cấu trúc vật lý mạng lưới (Plasticity).
    Sử dụng thuật toán học tập sinh học STDP (Long-Term Potentiation - LTP).
    """
    def __init__(self):
        self.population = LeakyIntegrateAndFireGroup(150, "Hippocampus")
        # Lưu trữ ma trận trọng số liên kết ký ức với thực tế
        self.synaptic_weights = np.random.uniform(0.3, 0.5, size=(150, 150))

    def consolidate_memory(self, source_spikes, target_spikes, dopamine_level):
        """
        Cơ chế STDP biến đổi cấu trúc não: 
        Nếu neuron nguồn phát xung ngay trước neuron đích, liên kết synapse sẽ dày lên vĩnh viễn.
        Càng có nhiều Dopamine (cảm xúc mạnh), ký ức khắc sâu càng nhanh.
        """
        if np.any(source_spikes) and np.any(target_spikes):
            # Tính toán ma trận gia tăng trọng số vật lý
            update = np.outer(source_spikes, target_spikes) * 0.02 * dopamine_level
            self.synaptic_weights = np.clip(self.synaptic_weights + update, 0.0, 2.5)
