# src/subcortex/amygdala_emotion.py
import numpy as np
from src.core.bio_neuron import LeakyIntegrateAndFireGroup

class AmygdalaEmotion:
    """Hạch hạnh nhân: Tính toán mức độ đe dọa và gửi tín hiệu ép tim mạch/hóa học sinh tồn"""
    def __init__(self):
        self.population = LeakyIntegrateAndFireGroup(100, "Amygdala")

    def evaluate_threat(self, visual_features):
        """Nhận diện tín hiệu hình ảnh nguy hiểm để kích phát dòng điện sinh tồn"""
        current_input = np.zeros(self.population.size)
        # Giả định 20 neuron đầu tiên nhạy cảm với các vật thể dạng súng/vũ khí
        if visual_features.get("weapon_detected", False):
            current_input[0:30] = 3.0  # Bơm dòng điện cực mạnh kích hoạt báo động khẩn
        return current_input
