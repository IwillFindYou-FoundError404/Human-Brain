# src/core/neuron_models.py
import numpy as np

class ConductanceBasedLIFGroup:
    """
    Giả lập một quần thể tế bào thần kinh vỏ não của người trưởng thành.
    Sử dụng phương trình vi phân phụ thuộc độ dẫn (Conductance-based LIF) 
    để mô phỏng các kênh ion hóa học (AMPA và GABA) truyền qua màng tế bào.
    """
    def __init__(self, size, name="CorticalPopulation"):
        self.size = size
        self.name = name
        
        # Các thông số màng tế bào sinh học (mV)
        self.v = np.full(size, -65.0)          # Hiệu điện thế màng hiện tại (Resting state)
        self.v_rest = -65.0                    # Điện thế nghỉ tế bào
        self.v_th = -50.0                      # Ngưỡng kích hoạt phát xung (Threshold)
        self.v_reset = -70.0                   # Điện thế sau khi xả xung điện
        self.tau_m = 20.0                      # Hằng số thời gian màng tế bào (ms)
        self.g_leak = 10.0                     # Độ dẫn điện rò rỉ (nS)
        
        # Điện thế đảo cực của các kênh ion (Reversal Potentials)
        self.e_rev_exc = 0.0                   # Kênh kích thích (AMPA - mV)
        self.e_rev_inh = -70.0                 # Kênh ức chế (GABA - mV)
        
        # Độ dẫn động của synapse theo thời gian thực (Dynamic Conductances)
        self.g_ampa = np.zeros(size)
        self.g_gaba = np.zeros(size)
        
        # Hằng số thời gian phân rã hóa học (Decay constants - ms)
        self.tau_ampa = 2.0                    
        self.tau_gaba = 5.0                    
        
        # Thời gian trơ sinh học (Refractory period) không thể nhận điện tích liên tục
        self.refractory_period = 3             
        self.refractory_timers = np.zeros(size)

    def integrate_ms(self, i_ext, g_exc_input, g_inh_input, dt=1.0):
        """
        Giải phương trình vi phân màng tế bào bằng phương pháp Euler:
        C_m * dV/dt = -g_leak*(V - V_rest) - g_ampa*(V - E_exc) - g_gaba*(V - E_inh) + I_ext
        """
        self.refractory_timers = np.maximum(0, self.refractory_timers - 1)
        active_cells = self.refractory_timers == 0
        
        # Tích tụ độ dẫn từ các chất hóa học synapse truyền đến
        self.g_ampa += g_exc_input
        self.g_gaba += g_inh_input
        
        # Tính toán các dòng điện ion nội tại
        i_leak = self.g_leak * (self.v - self.v_rest)
        i_syn_exc = self.g_ampa * (self.v - self.e_rev_exc)
        i_syn_inh = self.g_gaba * (self.v - self.e_rev_inh)
        
        # Cập nhật điện thế màng cho các tế bào không ở trạng thái trơ
        dv = (-i_leak[active_cells] - i_syn_exc[active_cells] - i_syn_inh[active_cells] + i_ext[active_cells]) / self.tau_m * dt
        self.v[active_cells] += dv
        
        # Phân rã tự nhiên nồng độ chất hóa học tại khe synapse theo cấp số mũ
        self.g_ampa -= (self.g_ampa / self.tau_ampa) * dt
        self.g_gaba -= (self.g_gaba / self.tau_gaba) * dt
        
        # Xác định tế bào vượt ngưỡng kích hoạt phát xung (Spike)
        spikes = (self.v >= self.v_th) & active_cells
        
        # Đưa các tế bào phát xung về trạng thái nghỉ và kích hoạt thời gian trơ
        self.v[spikes] = self.v_reset
        self.refractory_timers[spikes] = self.refractory_period
        
        return spikes
