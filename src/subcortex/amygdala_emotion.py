# src/subcortex/amygdala_emotion.py
import numpy as np
from src.core.bio_neuron import ConductanceBasedLIFGroup

class AmygdalaEmotionCore:
    """Hạch hạnh nhân: Máy quét và phản xạ vô điều kiện trước nguy cơ đe dọa sinh tồn"""
    def __init__(self):
        self.population = ConductanceBasedLIFGroup(150, "Amygdala_Core")

    def process_interregional_flows(self, visual_spikes, visual_weights):
        """Tính toán dòng điện synapse truyền từ Thùy chẩm sang Hạch hạnh nhân"""
        # Dòng điện truyền qua = Lưới điện thùy chẩm x Ma trận liên vùng
        in_current = np.dot(visual_spikes.astype(float), visual_weights) * 12.0
        return in_current
