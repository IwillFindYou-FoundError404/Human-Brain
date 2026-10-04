# src/cortex/temporal_language.py
import numpy as np
from src.core.bio_neuron import LeakyIntegrateAndFireGroup

class AdvancedLanguageCortex:
    """
    Vùng Ngôn ngữ Nâng cao: Không dùng câu thoại cố định.
    NPC tự lắp ghép câu từ luồng xung điện động lực của các thùy não.
    """
    def __init__(self):
        # Vùng Broca gồm 300 neuron, chia thành các phân vùng từ vựng độc lập
        self.broca = LeakyIntegrateAndFireGroup(300, "Broca_Dynamic_Speech")
        
        # Kho từ vựng của NPC (Mỗi từ được đại diện bởi một cụm 30 neuron)
        self.lexicon = {
            0: "Tôi", 1: "Bạn", 2: "Súng", 3: "Sợ", 
            4: "Tại sao", 5: "Không", 6: "Dừng lại", 7: "Nguy hiểm",
            8: "Cứu", 9: "Đau"
        }
        
    def decode_spikes_to_speech(self, broca_spikes):
        """
        Dịch luồng điện động thành câu nói tự do.
        Thuật toán quét qua toàn bộ lưới điện của vùng Broca, tìm các phân vùng từ 
        có tỉ lệ phát xung vượt ngưỡng và sắp xếp chúng theo cường độ dòng điện.
        """
        if not np.any(broca_spikes):
            return "..."

        activated_words = []
        
        # Quét qua 10 từ trong kho từ vựng (mỗi từ chiếm 30 neuron)
        for word_id, word_str in self.lexicon.items():
            start_idx = word_id * 30
            end_idx = start_idx + 30
            
            # Tính toán cường độ dòng điện (số lượng xung) của từ này
            spike_count = np.sum(broca_spikes[start_idx:end_idx])
            
            # Nếu từ này nhận được đủ điện tích từ Thùy trán và Amygdala truyền sang
            if spike_count > 4:  # Ngưỡng kích hoạt từ đơn
                activated_words.append((word_str, spike_count))
        
        # Sắp xếp các từ theo cường độ luồng điện (từ nào điện mạnh hơn sẽ nói trước)
        activated_words.sort(key=lambda x: x[1], reverse=True)
        
        if not activated_words:
            return "..."
            
        # Lắp ghép các từ đơn lẻ lại thành một cấu trúc câu tự phát sinh
        raw_words = [item[0] for item in activated_words]
        
        # Tạo ra câu nói dựa trên các từ bị kích hoạt điện (Ví dụ: ["Tại sao", "Súng", "Tôi", "Sợ"])
        sentence = " ... ".join(raw_words) + "!"
        return sentence
