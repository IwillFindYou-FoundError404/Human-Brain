# src/chemical/neuromodulation.py
import numpy as np

class NeuromodulationSystem:
    """Ma trận hóa học thần kinh điều phối trạng thái tâm lý toàn diện của hệ thống"""
    def __init__(self):
        self.transmitters = {
            "dopamine": 1.0,       # Động lực, học tập, phần thưởng
            "serotonin": 1.0,      # Bình tĩnh, kiềm chế hành vi bộc phát
            "noradrenaline": 1.0,  # Khẩn cấp, hoảng loạn, tăng tốc xử lý
            "cortisol": 1.0        # Căng thẳng, lưu vết tổn thương tâm lý
        }

    def flood(self, transmitter, amount):
        self.transmitters[transmitter] = np.clip(self.transmitters[transmitter] + amount, 0.0, 10.0)

    def decay(self, dt=1.0):
        # Xu hướng tự cân bằng sinh học (Homeostasis) về mức ổn định 1.0
        for chem in self.transmitters:
            rate = 0.05 if chem == "cortisol" else 0.1
            self.transmitters[chem] -= (self.transmitters[chem] - 1.0) * rate * dt
