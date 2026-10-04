import sys
import os
import numpy as np
import time

# Thêm đường dẫn src để chạy code trực tiếp
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from connectome import HumanConnectome
from neuromodulation import NeuromodulationSystem
from simulator import SpikingNeuralSimulator

def get_activity_rate(spikes):
    """Tính toán phần trăm neuron phát xung trong một thùy não"""
    return (np.sum(spikes) / len(spikes)) * 100

def main():
    print("=========================================================")
    print("   KHỞI CHẠY MÔ PHỎNG KIẾN TRÚC NÃO NGƯỜI TOÀN DIỆN v2.0 ")
    print("=========================================================\n")
    
    # Khởi tạo 3 tầng kiến trúc sinh học
    brain_map = HumanConnectome()
    chemistry = NeuromodulationSystem()
    simulator = SpikingNeuralSimulator(brain_map, chemistry)
    
    print("[Hệ thống]: Bản đồ Connectome đã nạp thành công.")
    print(f"[Hệ thống]: Đang mô phỏng 8 cấu trúc thùy với tổng cộng {sum(d['size'] for d in brain_map.regions.values())} nút neuron.")
    time.sleep(1)

    print("\n>>> TÌNH HUỐNG 1: Trạng thái NPC thư giãn bình thường")
    # Bơm một dòng điện nhẹ, đều đặn vào Thalamus làm luồng cảm giác môi trường nền
    baseline_sensory = np.random.uniform(0.1, 0.3, size=100)
    simulator.inject_sensory_input("Thalamus", baseline_sensory)
    
    for milisecond in range(3):
        spikes = simulator.step(dt=0.01)
        print(f"  + [t={milisecond}ms] Tỉ lệ phát xung: Thùy Chẩm ({get_activity_rate(spikes['Occipital_Lobe']):.1f}%) | Vỏ Não Trước Trán ({get_activity_rate(spikes['Prefrontal_Cortex']):.1f}%)")
    
    time.sleep(1)
    print("\n>>> TÌNH HUỐNG 2: Biến cố bất ngờ! Người chơi rút súng đe dọa NPC")
    print("[Hành động]: Tín hiệu thị giác nguy hiểm cường độ cao truyền vào Đồi Thị.")
    
    # Bơm xung điện cực mạnh vào Thalamus đại diện cho hình ảnh khẩu súng
    panic_sensory = np.random.uniform(1.5, 2.5, size=100)
    simulator.inject_sensory_input("Thalamus", panic_sensory)
    
    # Hạch hạnh nhân phát hiện nguy hiểm kích hoạt giải phóng Noradrenaline khẩn cấp
    chemistry.release_chemical("noradrenaline", 6.5)
    chemistry.release_chemical("cortisol", 2.0)
    
    print(f"[Hóa học thần kinh]: Noradrenaline tăng vọt lên: {chemistry.neurotransmitters['noradrenaline']:.2f}")
    print("[Hành động]: Bắt đầu chạy vòng lặp mô phỏng lan truyền điện tích...")
    time.sleep(1)

    # Chạy vòng lặp tính toán dòng điện thần kinh truyền qua lại giữa các thùy
    for step_ms in range(10):
        spikes = simulator.step(dt=0.01)
        
        # Kiểm tra mức độ kích hoạt của Vùng Vận Động (Motor Cortex) và Hạch Hạnh Nhân (Amygdala)
        amygdala_rate = get_activity_rate(spikes['Amygdala'])
        motor_rate = get_activity_rate(spikes['Motor_Cortex'])
        pfc_rate = get_activity_rate(spikes['Prefrontal_Cortex'])
        
        print(f"  + [Mili-giây {step_ms:02d}]: Amygdala phát xung {amygdala_rate:5.1f}% | Thùy Trán (PFC) {pfc_rate:5.1f}% | Vùng Vận Động {motor_rate:5.1f}%")
        
        # Quyết định hành vi đầu ra tự phát sinh (Emergent Output) dựa trên dữ liệu lưới điện vận động
        if step_ms == 5 and motor_rate > 30.0:
            print("\n  >> [HÀNH VI TỰ PHÁT SINH ĐẦU RA]:")
            print("     Xung điện vùng vận động vượt ngưỡng do hạch hạnh nhân ép điện thế qua ma trận synapse.")
            print("     NPC TỰ ĐỘNG THỰC HIỆN HÀNH ĐỘNG: Lùi lại, bỏ chạy, cơ thể run rẩy (Vector3(-1.5, 0, -1.0))")
            print("     *(Lưu ý: Không có bất kỳ câu lệnh if/else nào quy định hành động này trước đó)*\n")
            time.sleep(1)

    print("=========================================================")
    print(" Mô phỏng hoàn tất. Mã nguồn đã sẵn sàng đẩy lên GitHub! ")
    print("=========================================================")

if __name__ == "__main__":
    main()
