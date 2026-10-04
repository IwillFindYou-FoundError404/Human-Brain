# Human Connectome Simulation for Game NPCs 🧠🤖

A conceptual blueprint and architectural framework for simulating a 100% biological human brain structure (Whole Brain Emulation) tailored for open-world game NPCs. This repository replaces pre-programmed script pathways with **emergent behavioral generation** driven by bio-electric spike propagation across simulated human brain lobes, fully regulated by a real-time neuromodulation system.

---

## 🏗️ Architectural Framework

The system maps environment states directly into structural neuro-anatomy via a 4-tier processing pipeline:

1. **Human Connectome Layer (The Biological Hardware):** Maps simulated network parameters and synaptic pathways across the 4 major cerebral lobes (**Frontal, Parietal, Temporal, Occipital**) and deep subcortical nodes (**Thalamus, Amygdala, Hypothalamus**).
2. **Neuromodulation Matrix (The Chemistry):** Continuous state tracking of 4 primary virtual neurotransmitters (**Dopamine, Serotonin, Noradrenaline, Cortisol**) that dynamically modulate neuron firing thresholds across the network.
3. **Bio-Electric Simulation Engine:** A simplified Spiking Neural Network (SNN) tracking membrane voltage shifts at millisecond intervals to propagate data.
4. **Game I/O Bridge:** Translates environmental inputs (sensory triggers) into digital nerve impulses, and motor cortex output patterns back into structural movement vectors (`Vector3`).

---

## 📂 Repository Components

- `src/connectome.py`: Structural definitions of human cortical lobes, deep structures, and synaptic links.
- `src/neuromodulation.py`: Manages neurotransmitter synthesis, decay rates, and homeostatic baseline calculations.
- `src/simulator.py`: Core logic loop governing electric impulse routing through the node graph.
- `examples/run_npc_brain.py`: Executable scenario modeling an NPC's internal cognitive conflict under sudden environmental threat.

---

## 🚀 Installation & Sample Execution

Run the simulation runner script to observe how behaviors spontaneously emerge through synaptic weighting and chemical spikes:

```bash
pip install -r requirements.txt
python examples/run_npc_brain.py
```

### Expected Output Trace:
```text
--- Initializing Simulated NPC Human Brain Connectome v1.0 ---

[0.00s] Environment Signal: Threat detected! (Player draws weapon).
[0.02s] Thalamus routes visual spike trains to Occipital Lobe and Amygdala.
[0.05s] Amygdala registers danger -> Hypothalamus pumps Noradrenaline.
        -> Current Noradrenaline Level: 8.40
[0.25s] Prefrontal Cortex (Logic/Memory) vs Amygdala (Fear) conflict resolving...
[0.40s] Motor neurons fired! Amygdala bypasses prefrontal logic via high-voltage spikes.
        -> Action Output: Vector3(-1.0, 0.0, -0.5) [NPC retreats in panic]
```

## 🛠️ Requirements & Tech Stack
- **Language:** Python 3.9+
- **Core Dependencies:** NetworkX (Graph node modeling), NumPy (Matrix calculations).

## 📄 License
Distributed under the MIT License. Free for open-source modification and integration into custom game engines.
