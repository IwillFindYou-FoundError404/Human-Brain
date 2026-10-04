import numpy as np

class NeuromodulationSystem:
    """
    Hệ thống điều hòa hóa học thần kinh.
    Quản lý nồng độ chất hóa học ảo và sự ảnh hưởng của chúng lên hiệu điện thế màng tế bào.
    """
    def __init__(self):
        # Mức nền sinh học bình thường bằng 1.0
        self.neurotransmitters = {
            "dopamine": 1.0,       # Động lực, phần thưởng
            "serotonin": 1.0,      # Ổn định tâm trạng, kiềm chế
            "noradrenaline": 1.0,  # Chiến-hay-biến (Phản xạ sinh tồn)
            "cortisol": 1.0        # Căng thẳng, cảnh giác cao độ
        }
        
    def release_chemical(self, transmitter, amount):
        """Giải phóng chất dẫn truyền thần kinh vào khe synapse ảo"""
        if transmitter in self.neurotransmitters:
            self.neurotransmitters[transmitter] = np.clip(
                self.neurotransmitters[transmitter] + amount, 0.0, 10.0
            )

    def process_homeostasis_decay(self, dt):
        """Cơ chế tự cân bằng: Chất hóa học tự phân hủy theo thời gian để về mức nền 1.0"""
        for chem in self.neurotransmitters:
            current = self.neurotransmitters[chem]
            # Tốc độ phân hủy tự nhiên
            decay_rate = 0.2 if chem != "cortisol" else 0.05 
            self.neurotransmitters[chem] = current - (current - 1.0) * decay_rate * dt

    def get_firing_threshold_modifier(self, region_name):
        """Tính toán sự thay đổi ngưỡng kích hoạt điện thần kinh dựa trên hóa học hiện tại"""
        nor = self.neurotransmitters["noradrenaline"]
        ser = self.neurotransmitters["serotonin"]
        
        # Noradrenaline cao hạ thấp ngưỡng kích hoạt của Amygdala (dễ hoảng loạn)
        if region_name == "Amygdala":
            return -0.15 * (nor - 1.0)
        # Serotonin cao làm tăng ngưỡng kích hoạt của Motor_Cortex (bình tĩnh, bớt xung động hành vi)
        elif region_name == "Prefrontal_Cortex":
            return +0.1 * (ser - 1.0)
        
        return 0.0
