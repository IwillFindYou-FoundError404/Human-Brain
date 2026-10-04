# src/chemical/neuromodulation.py
import numpy as np

class NeuromodulationSystem:
    """
    Hệ thống điều hòa hóa học thần kinh toàn cục của người trưởng thành.
    Quản lý các chất dẫn truyền làm thay đổi trực tiếp thuộc tính lý-hóa của mạng lưới.
    """
    def __init__(self):
        self.transmitters = {
            "dopamine": 1.0,       # Động lực, củng cố tính dẻo học tập (Plasticity)
            "serotonin": 1.0,      # Kiểm soát hành vi bộc phát, nâng ngưỡng kiềm chế của vỏ não
            "noradrenaline": 1.0,  # Hệ thống khẩn cấp (Chiến-hay-Biến), hạ ngưỡng kích hoạt sinh tồn
            "cortisol": 1.0        # Hormone căng thẳng dài hạn, làm suy yếu khả năng ghi nhớ lý trí
        }

    def flood_chemical(self, chemical, amount):
        if chemical in self.transmitters:
            self.transmitters[chemical] = np.clip(self.transmitters[chemical] + amount, 0.0, 10.0)

    def compute_homeostasis(self, dt=1.0):
        """Cơ chế tự cân bằng sinh học đưa nồng độ hóa học về mức cân bằng 1.0"""
        for chem in self.transmitters:
            decay_speed = 0.02 if chem == "cortisol" else 0.1
            self.transmitters[chem] -= (self.transmitters[chem] - 1.0) * decay_speed * dt

    def evaluate_threshold_shift(self, region_name):
        """Trả về giá trị thay đổi ngưỡng điện thế (mV) của từng thùy dựa trên hóa học hiện tại"""
        nor = self.transmitters["noradrenaline"]
        ser = self.transmitters["serotonin"]
        
        if region_name == "Amygdala":
            # Noradrenaline cao làm hạ ngưỡng kích hoạt xuống (Khiến NPC nhạy cảm, dễ sợ hãi)
            return -2.5 * (nor - 1.0)
        elif region_name == "Prefrontal_Cortex":
            # Serotonin cao làm tăng ngưỡng kích hoạt (Giúp NPC bình tĩnh, tư duy logic tốt hơn)
            return +1.5 * (ser - 1.0)
        return 0.0
