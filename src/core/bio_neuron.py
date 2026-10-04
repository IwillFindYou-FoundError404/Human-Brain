# src/core/bio_neuron.py
import numpy as np

class LeakyIntegrateAndFireGroup:
    """
    Quản lý một quần thể Neuron (Neuron Population) sử dụng mô hình toán học LIF.
    Giả lập hiệu điện thế màng (V), thời gian trơ sinh học (Refractory Period).
    """
    def __init__(self, size, name="Region"):
        self.size = size
        self.name = name
        self.v = np.zeros(size)             # Điện thế màng hiện tại
        self.v_rest = 0.0                   # Điện thế nghỉ
        self.v_th = 1.0                     # Ngưỡng phát xung cơ bản
        self.tau_m = 10.0                   # Hằng số thời gian màng tế bào (ms)
        self.refractory_time = 2            # Thời gian trơ (ms)
        self.refractory_counters = np.zeros(size)

    def update(self, current_input, threshold_modifier=0.0, dt=1.0):
        """Cập nhật trạng thái điện thế màng tế bào sau mỗi mili-giây"""
        # Áp dụng chất hóa học để thay đổi ngưỡng kích hoạt
        current_threshold = self.v_th + threshold_modifier
        
        # Giảm thời gian trơ của các neuron vừa phát xung
        self.refractory_counters = np.maximum(0, self.refractory_counters - 1)
        
        # Những neuron không trong thời gian trơ mới được tích tụ điện tích
        not_refractory = self.refractory_counters == 0
        
        # Công thức toán học LIF: dV/dt = (-V + I) / tau_m
        dv = (-self.v[not_refractory] + current_input[not_refractory]) / self.tau_m * dt
        self.v[not_refractory] += dv
        
        # Xác định những neuron nào vượt ngưỡng để phát xung (Spike)
        spikes = (self.v >= current_threshold) & not_refractory
        
        # Reset các neuron phát xung về điện thế nghỉ và kích hoạt thời gian trơ
        self.v[spikes] = self.v_rest
        self.refractory_counters[spikes] = self.refractory_time
        
        return spikes
