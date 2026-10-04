# examples/run_grand_simulation.py
import sys
import os
import numpy as np
import time

# Ánh xạ đường dẫn thư mục gốc
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.chemical.neuromodulation import NeuromodulationSystem
from src.cortex.occipital_vision import OccipitalVisionCortex
from src.cortex.temporal_language import TemporalLanguageSystem
from src.cortex.frontal_executive import PrefrontalExecutiveCortex
from src.subcortex.amygdala_emotion import AmygdalaEmotionCore
from src.subcortex.hippocampus_memory import HippocampusMemoryBank

def main():
    print("=========================================================================")
    print("      HỆ THỐNG MÔ PHỎNG NÃO NGƯỜI TRƯỞNG THÀNH PHÂN RÃ TOÀN DIỆN v3.5     ")
    print("=========================================================================\n")
    
    # 1. Khởi tạo toàn bộ các module giải phẫu thần kinh độc lập
    chemistry = NeuromodulationSystem()
    vision_lobe = OccipitalVisionCortex()
    language_lobe = TemporalLanguageSystem()
    executive_lobe = PrefrontalExecutiveCortex()
    amygdala_core = AmygdalaEmotionCore()
    hippocampus_bank = HippocampusMemoryBank()
    
    # Khởi tạo ma trận trọng số kết nối liên vùng (Inter-regional Connectome Weight Matrices)
    np.random.seed(100)
    vision_to_amygdala_weights = np.random.uniform(0.1, 0.5, size=(200, 150))
    
    print("[Nghiên Cứu]: Khởi tạo thành công mô hình cấu trúc phân cấp mạng thần kinh.")
    print("[Nghiên Cứu]: Đang quét dòng điện nội tại thời gian thực (Độ phân giải 1ms).\n")
    time.sleep(1)

    print("-------------------------------------------------------------------------")
    print("BIẾN CỐ MÔI TRƯỜNG: Người chơi rút SÚNG bắn chỉ thiên và hét lớn: 'SỢ NGUY_HIỂM'")
    print("-------------------------------------------------------------------------")
    
    # Tạo trạng thái môi trường game truyền vào các thùy cảm giác của não bộ
    game_environment = {"weapon_drawn": True, "threat_proximity": 4.5}
    
    # Bước chạy mô phỏng liên tục qua 10 mili-giây thời gian thực của não bộ
    for ms in range(1, 11):
        # A. Thùy chẩm mã hóa hình ảnh khẩu súng thành dòng điện
        vision_current = vision_lobe.encode_environment_to_current(game_environment)
        vision_spikes = vision_lobe.population.integrate_ms(vision_current, 0, 0)
        
        # B. Vùng Wernicke tiếp nhận và xử lý ngữ nghĩa âm thanh câu hét
        wernicke_current = language_lobe.process_incoming_speech("SỢ NGUY_HIỂM")
        wernicke_spikes = language_lobe.wernicke.integrate_ms(wernicke_current, 0, 0)
        
        # C. Hạch hạnh nhân tiếp nhận luồng điện từ thùy chẩm truyền sang
        amygdala_current = amygdala_core.process_interregional_flows(vision_spikes, vision_to_amygdala_weights)
        amygdala_thresh_mod = chemistry.evaluate_threshold_shift("Amygdala")
        amygdala_spikes = amygdala_core.population.integrate_ms(amygdala_current, 0, 0, threshold_modifier=amygdala_thresh_mod)
        
        # Phản ứng hóa học nội tiết: Nếu Amygdala bị kích hoạt điện mạnh, xả ồ ạt Noradrenaline sinh tồn
        if np.sum(amygdala_spikes) > 10:
            chemistry.flood_chemical("noradrenaline", 0.7)
            chemistry.flood_chemical("cortisol", 0.2)
            chemistry.flood_chemical("serotonin", -0.1) # Giảm kiềm chế
            
        # D. Vỏ não trước trán tiếp nhận thông tin từ các vùng sâu để đấu tranh đưa ra quyết định lý trí
        pfc_current = executive_lobe.execute_cognitive_control(wernicke_spikes, amygdala_spikes, chemistry.transmitters["serotonin"])
        pfc_thresh_mod = chemistry.evaluate_threshold_shift("Prefrontal_Cortex")
        pfc_spikes = executive_lobe.pfc_logic.integrate_ms(pfc_current, 0, 0, threshold_modifier=pfc_thresh_mod)
        
        # E. Vùng vận động sơ cấp nhận lệnh điều khiển cơ thể
        motor_current = executive_lobe.map_to_motor_output(pfc_spikes, amygdala_spikes)
        motor_spikes = executive_lobe.motor_output.integrate_ms(motor_current, 0, 0)
        
        # F. Luồng điện hoảng loạn kích thích ngược lại vùng Broca tự động lắp ghép từ vựng phát ngôn
        broca_current = np.zeros(language_lobe.broca.size)
        if np.sum(amygdala_spikes) > 12:
            # Luồng điện ép phân vùng từ vựng số 3 ("Sợ") và số 5 ("Dừng_Lại") phân rã phát xung
            broca_current[3*20 : 3*20+20] = 45.0
            broca_current[5*20 : 5*20+20] = 40.0
        broca_spikes = language_lobe.broca.integrate_ms(broca_current, 0, 0)
        
        # G. Vùng Hải mã tự động biến đổi cấu trúc Synapse lưu lại ký ức kinh nghiệm sang chấn (STDP)
        hippocampus_bank.evaluate_plasticity_stdp(
            amygdala_spikes, pfc_spikes, chemistry.transmitters["dopamine"], chemistry.transmitters["cortisol"]
        )
        
        # Hạ phân rã hóa học tự nhiên
        chemistry.compute_homeostasis(dt=1.0)
        
        # Xuất nhật ký dòng điện thần kinh chạy xuyên qua các mô tế bào
        print(f"[t={ms:02d}ms] Tỉ lệ phát xung: Thùy Chẩm ({np.sum(vision_spikes)/2:.1f}%) | Amygdala ({np.sum(amygdala_spikes)/1.5:.1f}%) | Vỏ Não Trước Trán ({np.sum(pfc_spikes)/3:.1f}%) | N-Adrenaline: {chemistry.transmitters['noradrenaline']:.2f}")

    print("\n-------------------------------------------------------------------------")
    print("KẾT QUẢ GIẢI MÃ ĐẦU RA SỰ SỐNG (EMERGENT ECO-SYSTEM BEHAVIOR)")
    print("-------------------------------------------------------------------------")
    
    # Kiểm tra chuyển động cơ thể kết quả của mạng lưới
    if np.sum(motor_spikes[0:75]) > np.sum(motor_spikes[75:150]):
        print("[HÀNH ĐỘNG CƠ THỂ]: Lưới điện vận động ép NPC tự động lùi lại, quay đầu bỏ chạy hỗn loạn (Vector3(-3.5, 0.0, -2.0)).")
    else:
        print("[HÀNH ĐỘNG CƠ THỂ]: NPC đứng yên đối thoại nhờ lý trí kiểm soát được dòng hoảng loạn.")
        
    # Giải mã tiếng nói tự do lắp ghép từ vùng Broca
    npc_speech_output = language_lobe.decode_broca_to_speech(broca_spikes)
    print(f"[CÂU THOẠI TỰ PHÁT SINH CỦA NPC]: \"{npc_speech_output}\"")
    print("\n[Hệ thống]: Trọng số kết nối vùng Hải mã đã tự tái cấu trúc vật lý vĩnh viễn.")
    print("=========================================================================")

if __name__ == "__main__":
    main()
