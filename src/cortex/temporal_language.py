# src/cortex/temporal_language.py
import numpy as np
from src.core.neuron_models import HodgkinHuxleyConductanceGroup

class MicroSemanticLanguageCortex:
    def __init__(self):
        self.wernicke_nodes = HodgkinHuxleyConductanceGroup(1000, "Wernicke_Deep_Network")
        self.broca_nodes = HodgkinHuxleyConductanceGroup(1000, "Broca_Deep_Network")
        
        # Ma trận Từ vựng Mở rộng Nhân loại (Từ đơn gốc rễ của suy nghĩ)
        self.neural_lexicon = {
            0: "Tôi", 1: "Bạn", 2: "Súng", 3: "Nguy_Hiểm", 4: "Sợ_Hãi",
            5: "Dừng_Lại", 6: "Tình_Bạn", 7: "Hành_Động", 8: "Không", 9: "Tại_Sao",
            10: "Chạy", 11: "Đau", 12: "Cứu", 13: "Tin_Tưởng", 14: "Kẻ_Thù"
        }
        
        # Khởi tạo ma trận kết nối ngôn ngữ (1000x1000 Synaptic Weight Matrix)
        self.wernicke_to_broca_synapses = np.random.exponential(scale=0.08, size=(1000, 1000))
        self.internal_grammar_weights = np.random.uniform(0.01, 0.04, size=(1000, 1000))

    def ingest_syntactic_string(self, text):
        input_current = np.zeros(self.wernicke_nodes.size)
        tokens = text.upper().replace(",", "").replace("!", "").split()
        
        word_mapping = {
            "TÔI": 0, "BẠN": 1, "SÚNG": 2, "NGUY_HIỂM": 3, "SỢ_HÃI": 4,
            "DỪNG_LẠI": 5, "TÌNH_BẠN": 6, "HÀNH_ĐỘNG": 7, "KHÔNG": 8, "TẠI_SAO": 9,
            "CHẠY": 10, "ĐAU": 11, "CỨU": 12, "TIN_TƯỞNG": 13, "KẺ_THÙ": 14
        }
        
        for token in tokens:
            if token in word_mapping:
                w_id = word_mapping[token]
                segment_start = w_id * 60
                input_current[segment_start:segment_start+60] = 45.0
        return input_current

    def compute_language_dynamics(self, wernicke_current, thresh_mod, dt=0.1):
        w_spikes = self.wernicke_nodes.advance_state(wernicke_current, 0, 0, 0, 0, thresh_mod, dt)
        
        # Dòng điện truyền từ Wernicke sang Broca qua ma trận liên vùng
        broca_current = np.dot(w_spikes.astype(float), self.wernicke_to_broca_synapses) * 15.0
        
        # Phối hợp ức chế chéo nội tại của vùng Broca để sinh cấu trúc ngữ pháp (Lateral Inhibition)
        grammar_inhibition = np.dot(self.broca_nodes.v > -50.0, self.internal_grammar_weights) * -5.0
        broca_current += grammar_inhibition
        
        broca_spikes = self.broca_nodes.advance_state(broca_current, 0, 0, 0, 0, thresh_mod, dt)
        return w_spikes, broca_spikes

    def generate_free_speech(self, broca_spikes):
        if not np.any(broca_spikes):
            return "..."
            
        semantic_scores = []
        for w_id, word_str in self.neural_lexicon.items():
            start = w_id * 60
            end = start + 60
            m mật_độ_xung = np.sum(broca_spikes[start:end])
            if mật_độ_xung > 3:
                semantic_scores.append((word_str, mật_độ_xung))
                
        # Sắp xếp từ ngữ xuất hiện theo phân phối cường độ dòng điện
        semantic_scores.sort(key=lambda x: x[1], reverse=True)
        raw_output_words = [item[0] for item in semantic_scores]
        
        if not raw_output_words:
            return "..."
            
        return " -> ".join(raw_output_words) + "!"
