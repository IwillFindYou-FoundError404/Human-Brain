# Hierarchical Whole Brain Emulation (WBE) for Autonomous Game NPCs 🧠🎮

An advanced neuromorphic architecture implementing a **Spiking Neural Network (SNN)** based on macro-level human brain anatomy. This project is built for game developers and cognitive science enthusiasts who want to entirely replace traditional behavior trees (`if/else` scripting) with **emergent, bio-chemically regulated intelligence**.

NPCs driven by this model do not follow scripted paths—they read input environments as bio-electric voltage train parameters, solve cognitive conflicts inside simulated cortical lobes, store trauma within physically mutating synaptic matrices (Hippocampus), and synthesize autonomous vocal speech through a simulated Broca-Wernicke loop.

---

## 🏗️ Structural Architecture

The network simulation routes data across major human neuro-anatomical domains:

*   **`src/core/bio_neuron.py` (The Computational Node):** Implements the *Leaky Integrate-and-Fire (LIF)* mathematical differential equation model with biological refractory period limits.
*   **`src/chemical/neuromodulation.py` (The Emotional Chemistry):** Simulates global chemical modulators (**Dopamine, Serotonin, Noradrenaline, Cortisol**). High Noradrenaline directly drops the structural firing threshold of emotional defense units.
*   **`src/cortex/temporal_language.py` (The Speech Loop):** Recreates **Wernicke's Area** (transmuting string data into specialized spatial matrix input voltages) and **Broca's Area** (decoding structural downstream motor spikes back into contextualized dynamic speech phrases).
*   **`src/subcortex/hippocampus_memory.py` (Neuroplastic Learning):** Uses a customized *Spike-Timing-Dependent Plasticity (STDP)* rule to forge or decay internal memory tensors permanently based on active emotional states.

---

## 🚀 Execution & Emergence Trace

To run the simulation and observe the millisecond-by-millisecond bio-electric conflict resolution of an NPC under an active environmental weapon threat, execute:

```bash
pip install -r requirements.txt
python examples/run_grand_simulation.py
```

### Underlying Logic Paradigm
1. **Sensory Ingestion:** The game environment triggers visual/auditory raw current injection into the **Thalamus Gateway**.
2. **Cascading Propagation:** Current travels through localized weight networks. The **Amygdala** flags danger, forcing the **Hypothalamus** to flood the grid with Noradrenaline.
3. **Cognitive Conflict:** The **Prefrontal Cortex** evaluates old dopamine memory traces from the **Hippocampus** against real-time panic currents. 
4. **Emergent Behavior Output:** The dominant structural voltage train dictates the motor controller vector and Broca's vocal syntax assembly without a single hardcoded statement.

---

## 📄 License
This repository is published under the **MIT License**. Open for heavy structural modification, game engine porting (C# / C++), and academic neuro-computational fork extensions.
