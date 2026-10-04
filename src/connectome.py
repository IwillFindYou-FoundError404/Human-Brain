import numpy as np

class HumanConnectome:
    """
    Mô phỏng bản đồ kết nối (Connectome) của bộ não người ở cấp độ vĩ mô.
    Khởi tạo quần thể neuron (Neuron Populations) cho từng thùy não và cấu trúc sâu.
    """
    def __init__(self):
        # Định nghĩa các vùng não và số lượng neuron giả lập trong mỗi vùng
        self.regions = {
            "Thalamus": {"size": 100, "type": "sensory_relay"},
            "Occipital_Lobe": {"size": 200, "type": "visual_processing"},
            "Temporal_Lobe": {"size": 200, "type": "auditory_memory"},
            "Hippocampus": {"size": 150, "type": "memory_encoding"},
            "Amygdala": {"size": 100, "type": "threat_assessment"},
            "Hypothalamus": {"size": 80, "type": "homeostasis_chemical"},
            "Prefrontal_Cortex": {"size": 300, "type": "executive_logic"},
            "Motor_Cortex": {"size": 150, "type": "motor_output"}
        }
        
        self.synapses = {}
        self._build_synaptic_pathways()

    def _build_synaptic_pathways(self):
        """Khởi tạo ma trận trọng số synapse ngẫu nhiên dựa trên giải phẫu học não người"""
        np.random.seed(42) # Đảm bảo tính nhất quán khi khởi tạo
        
        # Hàm hỗ trợ tạo liên kết synapse giữa vùng A và vùng B
        def connect(source, target, base_weight):
            src_size = self.regions[source]["size"]
            tgt_size = self.regions[target]["size"]
            # Tạo ma trận trọng số ngẫu nhiên xung quanh mức nền cơ bản
            weight_matrix = np.random.normal(loc=base_weight, scale=0.1, size=(src_size, tgt_size))
            self.synapses[(source, target)] = np.clip(weight_matrix, 0.0, 2.0)

        # Thiết lập các đường dẫn thần kinh chính của não người
        connect("Thalamus", "Occipital_Lobe", base_weight=0.8)   # Luồng thị giác sơ cấp
        connect("Thalamus", "Amygdala", base_weight=0.9)         # Luồng phản xạ nhanh (Sợ hãi)
        connect("Occipital_Lobe", "Prefrontal_Cortex", 0.6)      # Nhận diện vật thể phức tạp
        connect("Occipital_Lobe", "Temporal_Lobe", 0.7)          # Phân tích hình thái & bối cảnh
        connect("Temporal_Lobe", "Hippocampus", 0.8)             # Chuyển đổi dữ liệu vào vùng nhớ
        connect("Hippocampus", "Prefrontal_Cortex", 0.7)         # Truy xuất ký ức để suy luận
        connect("Amygdala", "Hypothalamus", 0.95)                # Kích hoạt phản ứng hóa học sinh tồn
        connect("Prefrontal_Cortex", "Motor_Cortex", 0.75)       # Quyết định hành động có lý trí
        connect("Amygdala", "Motor_Cortex", 0.85)                # Phản xạ vô điều kiện (Bỏ chạy ngay)
