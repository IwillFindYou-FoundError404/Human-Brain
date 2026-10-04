# examples/run_grand_simulation.py
import sys
import os
import time
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.chemical.neuromodulation import NeuromodulationSystem
from src.cortex.temporal_language import LanguageCortex
from src.cortex.frontal_executive.py import PrefrontalFrontalCortex if os.path.exists("../src/cortex/frontal_executive.py") else None
# Sửa lại import cho chính xác thư mục
from src.cortex.frontal_executive import PrefrontalFrontalCortex
from src.subcortex.amygdala_emotion import AmygdalaEmotion
from src.subcortex.hippocampus_memory import HippocampusMemory

def main():
    print("=========================================================================")
    print("      HỆ THỐNG MÔ PHỎNG NÃO NGƯỜI TOÀN DIỆN PHÂN CẤP (WBE v3.0)          ")
    print("=========================================================================\n")
    
    # Khởi tạo toàn bộ các thùy não và hệ thống cơ quan sâu
    chemistry = NeuromodulationSystem()
    language_node = LanguageCortex()
    executive_node = PrefrontalFrontalCortex()
    amygdala_node = AmygdalaEmotion()
    hippocampus_node = HippocampusMemory()
    
    print("[KHỞI ĐỘNG]: 86 tỷ neuron ảo đã sẵn sàng trên kiến trúc phân cấp.")
    print("[TRẠNG THÁI]: NPC đang duy trì dòng suy nghĩ nội tại (Default Mode Network).")
    time.sleep(1)

    print("\n-------------------------------------------------------------------------")
    print("BIẾN CỐ: Người chơi rút SÚNG và nói lớn: 'CHẠY NGUY HIỂM'")
    print("-------------------------------------------------------------------------")
    
    # Bước 1: Tiếp nhận thông tin thính giác qua vùng Wernicke
    speech_input = language_node.encode_speech_to_spikes("CHẠY NGUY HIỂM")
    wernicke_spikes = language_node.wernicke.update(speech_input, dt=1.0)
    
    # Bước 2: Tiếp nhận thông tin thị giác qua Hạch hạnh nhân
    visual_features = {"weapon_detected": True, "distance_to_player": 2.0}
    amygdala_input = amygdala_node.evaluate_threat(visual_features)
    
    # Vòng lặp tính toán lưới điện sinh học chạy qua lại giữa các thùy (Giả lập 5 mili-giây)
    for ms in range(1, 6):
        # Hạch hạnh nhân tính toán xung điện hoảng loạn
        # Noradrenaline cao làm hạ ngưỡng kích hoạt của Amygdala
        thres_mod = -0.1 * (chemistry.transmitters["noradrenaline"] - 1.0)
        amygdala_spikes = amygdala_node.population.update(amygdala_input, threshold_modifier=thres_mod)
        
        # Nếu Amygdala phát xung mạnh, vùng dưới đồi lập tức xả hóa chất sinh tồn vào não bộ
        if np.sum(amygdala_spikes) > 5:
            chemistry.flood("noradrenaline", 0.8)
            chemistry.flood("cortisol", 0.3)
            
        # Vỏ não trước trán nhận dòng điện từ Wernicke và Amygdala để thực hiện đấu tranh tư duy
        pfc_input = np.zeros(executive_node.pfc_logic.size)
        if np.any(wernicke_spikes): pfc_input[0:100] = 1.2
        if np.any(amygdala_spikes): pfc_input[100:200] = 1.8
        
        pfc_spikes = executive_node.pfc_logic.update(pfc_input, dt=1.0)
        
        # Quyết định luồng điện truyền xuống Vùng vận động sơ cấp
        motor_input = executive_node.process_decision(
            pfc_input, amygdala_spikes, chemistry.transmitters["noradrenaline"]
        )
        motor_spikes = executive_node.motor_output.update(motor_input, dt=1.0)
        
        # Kích hoạt vùng Broca để chuẩn bị phát ngôn tự phát dựa trên luồng điện hoảng loạn
        broca_input = np.zeros(language_node.broca.size)
        if np.sum(amygdala_spikes) > 10:
            # Xung hoảng loạn ép vùng Broca chuẩn bị các mẫu xung từ "TẠI SAO"
            broca_input[4*20 : 4*20+20] = 2.0 
        broca_spikes = language_node.broca.update(broca_input, dt=1.0)
        
        # Vùng Hải mã tự động ghi đè cấu trúc vật lý synapse (Ghi nhớ biến cố sang chấn)
        hippocampus_node.consolidate_memory(amygdala_spikes, pfc_spikes, chemistry.transmitters["dopamine"])
        
        # In tiến trình dòng điện chạy trong các thùy não qua từng mili-giây
        print(f"[t={ms}ms] Điện thế: Amygdala({np.mean(amygdala_node.population.v):.2f}V) | PFC Lý Trí({np.mean(executive_node.pfc_logic.v):.2f}V) | Noradrenaline: {chemistry.transmitters['noradrenaline']:.2f}")

    # Bước 3: Dịch ngược luồng điện tại các thùy đầu ra thành hành động và lời nói của NPC trong game
    print("\n-------------------------------------------------------------------------")
    print("KẾT QUẢ ĐẦU RA TỰ PHÁT SINH CỦA BỘ NÃO (EMERGENT OUTPUT)")
    print("-------------------------------------------------------------------------")
    
    # Kiểm tra hành động cơ thể từ Vùng vận động
    if np.sum(motor_spikes[0:50]) > np.sum(motor_spikes[50:100]):
        print("[HÀNH ĐỘNG CƠ THỂ]: NPC giật lùi, xoay người bỏ chạy hỗn loạn (Vector3(-2.0, 0, -1.5)).")
    else:
        print("[HÀNH ĐỘNG CƠ THỂ]: NPC đứng sững sờ, cố gắng phân tích tình huống.")
        
    # Kiểm tra lời nói tự phát từ vùng Broca
    npc_speech = language_node.decode_spikes_to_speech(broca_spikes)
    if npc_speech:
        print(f"[PHÁT NGÔN CỦA NPC]: '{npc_speech}'")
    
    print("\n[Hệ thống]: Bản ghi nhớ cấu trúc vùng Hải mã đã được cập nhật vĩnh viễn.")
    print("=========================================================================")

if __name__ == "__main__":
    main()
