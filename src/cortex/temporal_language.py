# src/cortex/temporal_language.py
import numpy as np
from src.core.bio_neuron import LeakyIntegrateAndFireGroup

class LanguageCortex:
    """
    Mô phỏng vùng Broca và Wernicke.
    Dịch ngôn ngữ thành mẫu xung thần kinh (Encoding) và ngược lại (Decoding).
    """
    def __init__(self):
        self.wernicke = LeakyIntegrateAndFireGroup(200, "Wernicke_Area") # Hiểu ngôn ngữ
        self.broca = LeakyIntegrateAndFireGroup(200, "Broca_Area")       # Phát ngôn
        
        # Từ điển mã hóa khái niệm (Concept Map) kết nối từ ngữ với mẫu xung điện (Pattern IDs)
        self.vocabulary = {
            "SÚNG": 0, "BẠN": 1, "CỨU MẠNG": 2, "NGUY HIỂM": 3, 
            "TẠI SAO": 4, "XIN LỖI": 5, "CHẠY": 6, "ĐAU": 7
        }
        # Ánh xạ ngược từ mẫu xung của vùng Broca ra tiếng người
        self.reverse_vocab = {v: k for k, v in self.vocabulary.items()}

    def encode_speech_to_spikes(self, text):
        """Dịch văn bản môi trường thành luồng điện kích hoạt các neuron vùng Wernicke"""
        input_current = np.zeros(self.wernicke.size)
        words = text.upper().split()
        for word in words:
            if word in self.vocabulary:
                pattern_id = self.vocabulary[word]
                # Kích hoạt một cụm neuron cụ thể đại diện cho từ đó
                start_idx = pattern_id * 20
                input_current[start_idx:start_idx+20] = 2.5
        return input_current

    def decode_spikes_to_speech(self, broca_spikes):
        """Dịch luồng điện từ vùng Broca ngược lại thành lời nói của NPC"""
        if not np.any(broca_spikes):
            return None
            
        # Tìm xem cụm neuron của từ nào đang phát xung mạnh nhất
        best_pattern = -1
        max_spikes = 0
        for pattern_id in range(8):
            start_idx = pattern_id * 20
            spike_count = np.sum(broca_spikes[start_idx:start_idx+20])
            if spike_count > max_spikes:
                max_spikes = spike_count
                best_pattern = pattern_id
                
        if best_pattern in self.reverse_vocab and max_spikes > 2:
            output_map = {
                "TẠI SAO": "Tại sao... anh lại làm thế với tôi?",
                "NGUY HIỂM": "Tránh xa tôi ra! Nguy hiểm!",
                "BẠN": "Cảm ơn... chúng ta vẫn là bạn chứ?",
                "CHẠY": "Không... đừng bắn!"
            }
            return output_map.get(self.reverse_vocab[best_pattern], "...")
        return None
