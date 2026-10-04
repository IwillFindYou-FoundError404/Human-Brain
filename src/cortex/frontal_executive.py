# src/cortex/frontal_executive.py
import numpy as np
from src.core.bio_neuron import LeakyIntegrateAndFireGroup

class PrefrontalFrontalCortex:
    """Vỏ não trước trán: Trung tâm xử lý ý chí, đấu tranh tư duy logic và điều khiển vận động sơ cấp"""
    def __init__(self):
        self.pfc_logic = LeakyIntegrateAndFireGroup(300, "Prefrontal_Cortex")
        self.motor_output = LeakyIntegrateAndFireGroup(150, "Motor_Cortex")

    def process_decision(self, logic_input, amygdala_panic_spikes, noradrenaline):
        """Cuộc đấu tranh dòng điện giữa lý trí (PFC) và bản năng sợ hãi (Amygdala)"""
        motor_input = np.zeros(self.motor_output.size)
        
        # Nếu Amygdala hoảng loạn quá mạnh và Noradrenaline cao, bản năng sẽ đè bẹp lý trí
        if np.sum(amygdala_panic_spikes) > 15 and noradrenaline > 4.0:
            # Ép dòng điện chạy thẳng vào cụm neuron điều khiển hành vi "Bỏ chạy"
            motor_input[0:50] = 2.8 
        else:
            # Nếu không, xung điện từ tư duy logic sẽ hướng dẫn cơ thể đứng yên quan sát
            motor_input[50:100] = 1.5
            
        return motor_input
