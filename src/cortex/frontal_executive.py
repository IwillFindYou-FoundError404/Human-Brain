# src/cortex/frontal_executive.py
import numpy as np
from src.core.bio_neuron import ConductanceBasedLIFGroup

class PrefrontalExecutiveCortex:
    """Vỏ não trước trán: Cơ quan đầu não tối cao điều khiển ý chí, kiềm chế và hành động có lý trí"""
    def __init__(self):
        self.pfc_logic = ConductanceBasedLIFGroup(300, "Prefrontal_Logic")
        self.motor_cortex = ConductanceBasedLIFGroup(150, "Motor_Primary")

    def execute_cognitive_control(self, wernicke_spikes, amygdala_spikes, serotonin):
        """Giải quyết mâu thuẫn dòng điện giữa vùng logic (Ngôn từ giải thích) và vùng bản năng (Sợ hãi)"""
        pfc_input = np.zeros(self.pfc_logic.size)
        
        # Bơm điện tích từ vùng hiểu ngôn ngữ (Wernicke) vào vùng xử lý logic
        if np.any(wernicke_spikes):
            pfc_input[0:150] += 18.0
            
        # Bơm dòng điện hoảng loạn từ Amygdala vào phân khu phòng vệ sinh tồn
        if np.any(amygdala_spikes):
            # Nếu Serotonin thấp, dòng điện hoảng loạn sẽ dễ dàng tràn ngập vỏ não trước trán
            inhibitory_barrier = 25.0 * serotonin
            pfc_input[150:300] += np.maximum(0, (np.sum(amygdala_spikes) * 2.0) - inhibitory_barrier)
            
        return pfc_input

    def map_to_motor_output(self, pfc_spikes, amygdala_spikes):
        """Dịch lưới điện thùy trán ra Vector hành động trong game"""
        motor_input = np.zeros(self.motor_cortex.size)
        
        # Luồng điện bản năng đè bẹp lý trí -> Kích hoạt cơ chế trốn chạy (Motor 0-75)
        if np.sum(amygdala_spikes) > 25:
            motor_input[0:75] += 35.0
        else:
            # Luồng điện tư duy giữ bình tĩnh -> Kích hoạt cơ chế đứng đàm thoại (Motor 75-150)
            motor_input[75:150] += 15.0
            
        return motor_input
