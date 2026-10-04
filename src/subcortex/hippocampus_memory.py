# src/subcortex/hippocampus_memory.py
import numpy as np
from src.core.bio_neuron import ConductanceBasedLIFGroup

class HippocampusMemoryBank:
    """
    Vùng Hải mã của não người trưởng thành.
    Lưu giữ kinh nghiệm bằng thuật toán học tập sinh học STDP (Spike-Timing-Dependent Plasticity).
    """
    def __init__(self):
        self.population = ConductanceBasedLIFGroup(150, "Hippocampus_Core")
        # Khởi tạo ma trận liên kết ký ức nền tảng vật lý ban đầu giữa các thùy
        self.associative_weights = np.random.uniform(0.2, 0.4, size=(150, 150))

    def evaluate_plasticity_stdp(self, pre_spikes, post_spikes, dopamine_level, cortisol_level):
        """
        Cơ chế STDP biến đổi vật lý: Trọng số tăng (LTP) nếu Pre-spike kích hoạt trước Post-spike.
        Dopamine cao thúc đẩy khắc sâu ký ức, Cortisol cao (Căng thẳng mãn tính) gây nhiễu loạn bộ nhớ.
        """
        if np.any(pre_spikes) and np.any(post_spikes):
            # Tính toán ma trận biến thiên cấu trúc não bộ thời gian thực
            learning_rate = 0.05 * (dopamine_level / (cortisol_level + 0.1))
            delta_w = np.outer(pre_spikes, post_spikes) * learning_rate
            self.associative_weights = np.clip(self.associative_weights + delta_w, 0.0, 3.0)
