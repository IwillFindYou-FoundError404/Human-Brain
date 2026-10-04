# src/cortex/occipital_vision.py
import numpy as np
from src.core.bio_neuron import ConductanceBasedLIFGroup

class OccipitalVisionCortex:
    """Thùy chẩm: Chuyển đổi các thực thể hình ảnh/sự kiện môi trường thành xung mã hóa điện học"""
    def __init__(self):
        self.population = ConductanceBasedLIFGroup(200, "Occipital_Visual")

    def encode_environment_to_current(self, environment_state):
        """Biến đổi các thuộc tính hình ảnh môi trường thành dòng điện đầu vào (pA)"""
        current_input = np.random.normal(5.0, 1.0, self.population.size)
        
        # Nếu camera game quét thấy vũ khí, bơm dòng điện kích thích mạnh lên cụm neuron thị giác nhận diện
        if environment_state.get("weapon_drawn", False):
            current_input[0:80] += 25.0
        # Thêm dòng điện kích thích dựa trên khoảng cách gần của mối đe dọa
        proximity = environment_state.get("threat_proximity", 0.0)
        current_input[80:150] += proximity * 5.0
        
        return current_input
