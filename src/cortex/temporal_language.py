# src/cortex/temporal_language.py
import numpy as np
from src.core.bio_neuron import ConductanceBasedLIFGroup

class TemporalLanguageSystem:
    """
    Vòng lặp ngôn ngữ Broca - Wernicke của người trưởng thành.
    Không dùng câu thoại cố định, ngôn ngữ tự hình thành dựa trên phân vùng cụm xung thần kinh.
    """
    def __init__(self):
        self.wernicke = ConductanceBasedLIFGroup(200, "Wernicke_Area") # Phân tích ngữ nghĩa
        self.broca = ConductanceBasedLIFGroup(200, "Broca_Area")       # Lắp ráp cấu trúc câu
        
        # Bản đồ ngữ nghĩa phân vùng neuron: Mỗi khái niệm chiếm một cụm 20 tế bào
        self.semantic_lexicon = {
            0: "Tôi", 1: "Bạn", 2: "Súng", 3: "Sợ", 
            4: "Tại_Sao", 5: "Dừng_Lại", 6: "Nguy_Hiểm", 7: "Tình_Bạn"
        }

    def process_incoming_speech(self, text_input):
        """Mã hóa lời nói của người chơi thành dòng điện truyền thẳng vào vùng Wernicke"""
        in_current = np.zeros(self.wernicke.size)
        words = text_input.upper().split()
        
        # Ánh xạ từ vựng vào cụm neuron tương ứng
        word_to_id = {"TÔI": 0, "BẠN": 1, "SÚNG": 2, "SỢ": 3, "TẠI_SAO": 4, "DỪNG_LẠI": 5, "NGUY_HIỂM": 6, "BAN": 7}
        for w in words:
            if w in word_to_id:
                idx = word_to_id[w] * 20
                in_current[idx:idx+20] = 30.0 # Bơm dòng điện kích thích ngữ nghĩa
        return in_current

    def decode_broca_to_speech(self, broca_spikes):
        """Giải mã hoạt động mạng lưới điện của vùng Broca thành chuỗi phát ngôn tự do của NPC"""
        if not np.any(broca_spikes):
            return "..."
            
        active_concepts = []
        for concept_id, word_str in self.semantic_lexicon.items():
            start = concept_id * 20
            # Kiểm tra xem cụm neuron của từ đơn này có mật độ phát xung vượt ngưỡng không
            if np.sum(broca_spikes[start:start+20]) >= 3:
                active_concepts.append(word_str)
                
        if not active_concepts:
            return "..."
            
        # Tự lắp ghép cấu trúc câu dựa trên luồng điện sinh học tự phát sinh
        return " ... ".join(active_concepts) + "!"
