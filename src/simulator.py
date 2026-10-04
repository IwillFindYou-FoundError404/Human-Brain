import numpy as np

class SpikingNeuralSimulator:
    """
    Lõi giả lập mạng thần kinh dạng xung (Spiking Neural Network).
    Tính toán điện thế màng (Membrane Potential) từng mili-giây của mô hình Leaky Integrate-and-Fire (LIF).
    """
    def __init__(self, connectome, neuro_system):
        self.connectome = connectome
        self.chemistry = neuro_system
        
        # Khởi tạo trạng thái điện thế màng cho tất cả neuron trong các vùng
        self.voltages = {}
        self.base_threshold = 1.0  # Ngưỡng điện thế để neuron phát xung (Spike)
        self.resting_potential = 0.0
        self.leak_constant = 0.1   # Tốc độ rò rỉ điện tích theo thời gian
        
        for region, data in self.connectome.regions.items():
            self.voltages[region] = np.full(data["size"], self.resting_potential)

    def inject_sensory_input(self, region, spike_train):
        """Bơm dòng điện cảm giác ngoại cảnh vào một vùng não nhất định"""
        if region in self.voltages:
            size = self.connectome.regions[region]["size"]
            # Đảm bảo luồng dữ liệu khớp với kích thước quần thể neuron của thùy
            clamped_input = np.resize(spike_train, size)
            self.voltages[region] += clamped_input

    def step(self, dt=0.01):
        """
        Một bước chạy mô phỏng thời gian thực (Time Step).
        Tính toán truyền điện từ Thùy trước sang Thùy sau và cập nhật tính dẻo thần kinh (STDP).
        """
        active_spikes = {}
        
        # Bước 1: Xác định các neuron phát xung trong từng vùng não
        for region, v_array in self.voltages.items():
            # Điều chỉnh ngưỡng kích hoạt cục bộ dựa trên chất hóa học trong não
            local_threshold = self.base_threshold + self.chemistry.get_firing_threshold_modifier(region)
            
            spikes = v_array >= local_threshold
            active_spikes[region] = spikes
            
            # Reset các neuron vừa phát xung về trạng thái nghỉ điện thế âm
            self.voltages[region][spikes] = self.resting_potential
            # Các neuron không phát xung sẽ bị rò rỉ điện tích (Leaky)
            self.voltages[region][~spikes] -= (self.voltages[region][~spikes] - self.resting_potential) * self.leak_constant

        # Bước 2: Lan truyền luồng xung điện qua các ma trận synapse liên vùng
        for (src, tgt), weight_matrix in self.connectome.synapses.items():
            src_spikes = active_spikes[src]
            
            if np.any(src_spikes):
                # Tính tổng lượng điện tích truyền qua synapse sang vùng đích
                # Tương đương phép nhân ma trận: Lực dòng điện = Số neuron phát xung x Trọng số synapse
                input_current = np.dot(src_spikes.astype(float), weight_matrix) * 0.2
                self.voltages[tgt] += input_current
                
                # Cơ chế Học tập Sinh học (Tính dẻo thần kinh - Neuroplasticity / STDP tối giản)
                # Tăng nhẹ trọng số synapse nếu con đường này được kích hoạt liên tục
                self.connectome.synapses[(src, tgt)][src_spikes, :] += 0.001
                self.connectome.synapses[(src, tgt)] = np.clip(self.connectome.synapses[(src, tgt)], 0.0, 2.0)

        # Bước 3: Cập nhật sự suy giảm hóa học tự nhiên
        self.chemistry.process_homeostasis_decay(dt)
        
        return active_spikes
