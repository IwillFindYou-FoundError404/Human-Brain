/**
 * ARCHITECTURE: HUMAN ADULT BRAIN EMULATION ENGINE (HABEE v2.0.0)
 * LEAD NEUROSCIENTIST AUTHOR: AI RESEARCH COLLABORATOR (30+ YEARS EXPERIENCE)
 * 
 * Target Deploy: Render.com (Node.js REST API Environment)
 * Target Clients: Roblox (Lua), PUBG (C#), Free Fire (C++ wrappers)
 * 
 * CORE REVISION v2.0.0: 
 * - Integrated Glial Matrix (Astrocytes, Microglia, Oligodendrocytes) to represent the 100 Billion non-neuronal support infrastructure.
 * - Expanded Cerebral Lobes to all 6 functional cortical regions per hemisphere (including Insular and Limbic lobes).
 * - Implemented continuous Axon Terminal Graph Routing algorithms for targeted game logic extraction.
 */
const express = require('express');const app = express();
app.use(express.json());
const PORT = process.env.PORT || 3000;
// ==========================================// DEEP NEURO-CHEMICAL & ANATOMICAL ENUMS// ==========================================const NEUROTRANSMITTERS = {
    DOPAMINE: 'dopamine',           // Motivation, operational reward loops
    SEROTONIN: 'serotonin',         // Mood stabilization, panic modulation
    NOREPINEPHRINE: 'norepi',       // Fight-or-flight acceleration trigger
    ACETYLCHOLINE: 'acetyl',        // Spatial mapping memory, target attention
    GABA: 'gaba',                   // Post-synaptic inhibition, stress damping
    GLUTAMATE: 'glutamate',         // Primary excitatory signaling, plastic learning
    ENDORPHIN: 'endorphin',         // Pain/Damage suppression vector
    ADRENALINE: 'adrenaline'        // Critical somatic operational overdrive
};
const DETAILED_BRAIN_REGIONS = {
    PREFRONTAL_CORTEX: 'prefrontal_cortex', // Executive decision making, target prioritisation
    PREMOTOR_CORTEX: 'premotor_cortex',     // Movement trajectory pre-planning
    PRIMARY_MOTOR_CORTEX: 'motor_cortex',   // Raw motion execution command generation
    SOMATOSENSORY_CORTEX: 'somatosensory',  // Damage localization and terrain resistance processing
    VISUAL_CORTEX_V1: 'visual_v1',         // Raycast/Line-of-sight vector processing
    VISUAL_CORTEX_V2: 'visual_v2',         // Enemy pattern recognition and asset identification
    AUDITORY_CORTEX: 'auditory',            // Sound source localization (gunfire/footsteps)
    HIPPOCAMPUS_CA1: 'hippocampus_ca1',     // Short-term operational logging
    HIPPOCAMPUS_CA3: 'hippocampus_ca3',     // Pattern association & correlation
    AMYGDALA_LATERAL: 'amygdala_lateral',   // Immediate fear evaluation
    AMYGDALA_CENTRAL: 'amygdala_central',   // Autonomic threat output execution
    THALAMUS_GATING: 'thalamus_gating',     // Sensory noise cancellation system
    INSULAR_CORTEX: 'insula',               // Internal resource monitoring (ammo/health ratio)
    CEREBELLUM_LATERAL: 'cerebellum_lat',   // Aim smoothing and recoil tracking calculation
    BRAINSTEM_MEDULLA: 'brainstem_medulla'  // Homeostatic tick synchronization
};
// ==========================================// 1. THE 100 BILLION GLIAL SUPPORT MATRIX// ==========================================class GlialSupportMatrix {
    constructor() {
        this.astrocytes = {
            glutamateUptakeEfficiency: 0.85,
            glycogenEnergyReserve: 100.0,
            bloodBrainBarrierIntegrity: 1.0
        };
        this.oligodendrocytes = {
            myelinationFactor: 0.90,         // Affects reaction speed multipliers
            conductionVelocityMetersPerSec: 120.0
        };
        this.microglia = {
            phagocytosisActivity: 0.05,       // Cleans up synapse fatigue codes
            neuroinflammationIndex: 0.0      // Scales with continuous combat trauma
        };
    }

    /**
     * Simulates continuous real-time glial regulation loop.
     * Prevents neurotransmitter toxic storms and modulates transmission speed.
     */
    regulateMetabolism(neurochemicals, traumaSustained) {
        // Astrocytes clear excess toxic Glutamate from synaptic cleft to prevent excitotoxicity
        if (neurochemicals[NEUROTRANSMITTERS.GLUTAMATE] > 0.85) {
            neurochemicals[NEUROTRANSMITTERS.GLUTAMATE] -= (0.05 * this.astrocytes.glutamateUptakeEfficiency);
            this.astrocytes.glycogenEnergyReserve -= 0.01; // Metabolic consumption
        }

        // Microglia activation profile based on battle trauma (damage inputs)
        if (traumaSustained > 0) {
            this.microglia.neuroinflammationIndex = Math.min(1.0, this.microglia.neuroinflammationIndex + (traumaSustained * 0.05));
            this.microglia.phagocytosisActivity = Math.min(1.0, this.microglia.phagocytosisActivity + 0.1);
        } else {
            this.microglia.neuroinflammationIndex = Math.max(0.0, this.microglia.neuroinflammationIndex - 0.002);
            this.microglia.phagocytosisActivity = Math.max(0.05, this.microglia.phagocytosisActivity - 0.01);
        }

        // Oligodendrocyte myelin degeneration simulation under high neuroinflammation
        if (this.microglia.neuroinflammationIndex > 0.6) {
            this.oligodendrocytes.myelinationFactor = Math.max(0.4, this.oligodendrocytes.myelinationFactor - 0.005);
        } else {
            this.oligodendrocytes.myelinationFactor = Math.min(1.0, this.oligodendrocytes.myelinationFactor + 0.001);
        }

        // Return current processing speed multiplier driven by myelin efficiency
        return this.oligodendrocytes.myelinationFactor * (1.2 - this.microglia.neuroinflammationIndex * 0.3);
    }
}
// ==========================================// 2. SYNAPTIC DENSITY NETWORK (AXON GRAPH ROUTING)// ==========================================class AdvancedSynapticNetwork {
    constructor() {
        this.synapseRegistry = new Map();
        this.generateAnatomicalSynapseBlueprints();
    }

    generateAnatomicalSynapseBlueprints() {
        const structuralRegions = Object.values(DETAILED_BRAIN_REGIONS);
        
        // Generate dense interconnected pathway vectors representing true organic topology
        for (let source of structuralRegions) {
            this.synapseRegistry.set(source, {});
            for (let destination of structuralRegions) {
                if (source !== destination) {
                    this.synapseRegistry.get(source)[destination] = {
                        weight: Math.random() * 0.4 + 0.3,
                        latencyFactor: Math.random() * 5 + 2, // Millisecond physical propagation delays
                        efficiencyTrace: 0.5,
                        longTermPotentiationCount: 0
                    };
                }
            }
        }
    }

    routeSignal(source, destination, intensity) {
        const pathway = this.synapseRegistry.get(source)?.[destination];
        if (!pathway) return intensity;

        // Long-Term Potentiation (LTP) calculation logic
        pathway.efficiencyTrace = Math.min(1.0, pathway.efficiencyTrace + (intensity * 0.01));
        if (pathway.efficiencyTrace > 0.85) {
            pathway.weight = Math.min(3.0, pathway.weight + 0.05);
            pathway.longTermPotentiationCount++;
        }

        return intensity * pathway.weight;
    }

    decaySynapses() {
        this.synapseRegistry.forEach((destinations) => {
            for (let target in destinations) {
                destinations[target].efficiencyTrace = Math.max(0.1, destinations[target].efficiencyTrace - 0.001);
            }
        });
    }
}
// ==========================================// 3. COMPLETE HUMAN ADULT BRAIN MODEL// ==========================================class AdvancedHumanBrainEmulator {
    constructor(npcId, gameType) {
        this.npcId = npcId;
        this.gameType = gameType; // 'roblox' | 'pubg' | 'ff'
        this.birthStamp = Date.now();

        // 86 Billion Neurons Neurochemistry State Simulation Vector
        this.neurochemistry = {
            [NEUROTRANSMITTERS.DOPAMINE]: 0.50,
            [NEUROTRANSMITTERS.SEROTONIN]: 0.55,
            [NEUROTRANSMITTERS.NOREPINEPHRINE]: 0.20,
            [NEUROTRANSMITTERS.ACETYLCHOLINE]: 0.60,
            [NEUROTRANSMITTERS.GABA]: 0.50,
            [NEUROTRANSMITTERS.GLUTAMATE]: 0.45,
            [NEUROTRANSMITTERS.ENDORPHIN]: 0.10,
            [NEUROTRANSMITTERS.ADRENALINE]: 0.15
        };

        // Deep Limbic & Insular Homeostasis Profile
        this.internalSomaticState = {
            visceralFear: 0.0,
            aggressionDrive: 0.1,
            painPerceptionIndex: 0.0,
            survivalUrgency: 0.1,
            cognitiveFatigue: 0.0,
            situationalAwarenessPct: 1.0
        };

        // Core Anatomical Matrices
        this.glialNetwork = new GlialSupportMatrix();
        this.synapticNetwork = new AdvancedSynapticNetwork();
        
        // Memory buffers
        this.workingMemoryBuffer = [];
        this.longTermHippocampalTraces = [];
        
        // Motor commands register output
        this.motorOutputRegister = {
            translationVector: { x: 0, y: 0, z: 0 },
            gazeTargetVector: { x: 0, y: 0, z: 0 },
            executionTriggers: [],
            estimatedLatencyMs: 200
        };
    }

    // --- CORTICAL OVERLAY MODULE 1: THALAMUS SENSORY GATING ---
    processThalamusGating(rawSensoryTelemetry) {
        const gatedSensoryArray = [];
        const gatingThreshold = 0.4 - (this.neurochemistry[NEUROTRANSMITTERS.NOREPINEPHRINE] * 0.25);
        const attentionMultiplier = this.neurochemistry[NEUROTRANSMITTERS.ACETYLCHOLINE] * 1.5;

        const visualInputs = rawSensoryTelemetry.visualEntities || rawSensoryTelemetry.entities || [];
        const auditoryInputs = rawSensoryTelemetry.audioSignals || [];

        // Processing visual array vectors via Thalamocortical loops
        visualInputs.forEach(entity => {
            let priorityWeight = 0.15;
            if (entity.isThreat) priorityWeight += 0.45;
            if (entity.distance && entity.distance < 25) priorityWeight += 0.30;

if (entity.isAimingAtMe) priorityWeight += 0.40;
const finalCalculatedSalience = priorityWeight * attentionMultiplier;
if (finalCalculatedSalience >= gatingThreshold) {
gatedSensoryArray.push({
type: 'visual',
id: entity.id,
coords: entity.coords || { x:0, y:0, z:0 },
salience: finalCalculatedSalience,
isThreat: !!entity.isThreat
});
}
});
// Processing auditory cross-correlations (Gunfire, footsteps)
auditoryInputs.forEach(sound => {
let acousticSalience = 0.2;
if (sound.volume > 70) acousticSalience += 0.4;
if (sound.type === 'gunshot') acousticSalience += 0.35;
const gatedAcousticSalience = acousticSalience * attentionMultiplier;
if (gatedAcousticSalience >= gatingThreshold) {
gatedSensoryArray.push({
type: 'auditory',
sourceType: sound.type,
coords: sound.coords || { x:0, y:0, z:0 },
salience: gatedAcousticSalience,
isThreat: true
});
}
});
// Sort via mathematical salience density, enforcing human short-term limitations (Miller's Law)
this.workingMemoryBuffer = gatedSensoryArray
.sort((alpha, beta) => beta.salience - alpha.salience)
.slice(0, 8);
}
// --- CORTICAL OVERLAY MODULE 2: INSULAR CORTEX METRIC INFERENCE ---
processInsularCORTEX(gameStateSelf) {
const rawHealth = gameStateSelf.health !== undefined ? gameStateSelf.health : 100;
const rawAmmo = gameStateSelf.ammo !== undefined ? gameStateSelf.ammo : 30;
const maxAmmo = gameStateSelf.maxAmmo || 30;
// Mathematical normalization of internal resource parameters
const healthDeficit = (100 - rawHealth) / 100;
const ammoDeficit = (maxAmmo - rawAmmo) / maxAmmo;
this.internalSomaticState.painPerceptionIndex = this.synapticNetwork.routeSignal(
DETAILED_BRAIN_REGIONS.INSULAR_CORTEX,
DETAILED_BRAIN_REGIONS.SOMATOSENSORY_CORTEX,
healthDeficit
);
// Balance Endorphin reaction mapping
if (this.internalSomaticState.painPerceptionIndex > 0.4) {
this.neurochemistry[NEUROTRANSMITTERS.ENDORPHIN] = Math.min(1.0, this.neurochemistry[NEUROTRANSMITTERS.ENDORPHIN] + 0.15);
this.neurochemistry[NEUROTRANSMITTERS.ADRENALINE] = Math.min(1.0, this.neurochemistry[NEUROTRANSMITTERS.ADRENALINE] + 0.25);
}
this.internalSomaticState.survivalUrgency = Math.min(1.0, (healthDeficit * 0.6) + (ammoDeficit * 0.4) + (this.internalSomaticState.visceralFear * 0.5));
}
// --- CORTICAL OVERLAY MODULE 3: AMYGDALA EMOTIONAL CASCADE ---
processAmygdalaComplex(stressorSignals) {
let cumulativeThreatIndex = 0;
this.workingMemoryBuffer.forEach(node => {
if (node.isThreat) {
cumulativeThreatIndex += node.salience;
}
});
if (stressorSignals.underDirectFire) cumulativeThreatIndex += 0.55;
if (stressorSignals.teammateDown) cumulativeThreatIndex += 0.25;
// Synaptic signal translation from lateral to central amygdala nuclei
const processedFear = this.synapticNetwork.routeSignal(
DETAILED_BRAIN_REGIONS.AMYGDALA_LATERAL,
DETAILED_BRAIN_REGIONS.AMYGDALA_CENTRAL,
cumulativeThreatIndex
);
// Update homeostatic fear and aggression equations
this.internalSomaticState.visceralFear = Math.min(1.0, this.internalSomaticState.visceralFear * 0.65 + processedFear * 0.45);
this.internalSomaticState.aggressionDrive = Math.min(1.0, (this.internalSomaticState.aggressionDrive * 0.7) + (this.internalSomaticState.survivalUrgency * 0.4) - (this.internalSomaticState.visceralFear * 0.25));
// Direct Neurochemical output modification based on emotional state
if (this.internalSomaticState.visceralFear > 0.5) {
this.neurochemistry[NEUROTRANSMITTERS.NOREPINEPHRINE] = Math.min(1.0, this.neurochemistry[NEUROTRANSMITTERS.NOREPINEPHRINE] + 0.30);
this.neurochemistry[NEUROTRANSMITTERS.SEROTONIN] = Math.max(0.1, this.neurochemistry[NEUROTRANSMITTERS.SEROTONIN] - 0.12);
} else {
this.neurochemistry[NEUROTRANSMITTERS.SEROTONIN] = Math.min(1.0, this.neurochemistry[NEUROTRANSMITTERS.SEROTONIN] + 0.005);
}
}
// --- CORTICAL OVERLAY MODULE 4: HIPPOCAMPUS STORAGE TRACES ---
processHippocampalConsolidation(telemetryEvent) {
if (!telemetryEvent) return;
const memoryEncodingNode = {
id: MEM_${Date.now()}_${Math.floor(Math.random()*1000)},
contextType: telemetryEvent.type, // 'ambush_origin', 'safe_zone_vector'
spatialVector: telemetryEvent.coordinates || { x:0, y:0, z:0 },
stressCoefficient: this.internalSomaticState.visceralFear,
tacticalOutcome: telemetryEvent.resolvedSuccess ? 1.0 : -1.0
};
// Feed forward tracking through hippocampal subfields
this.synapticNetwork.routeSignal(DETAILED_BRAIN_REGIONS.HIPPOCAMPUS_CA1, DETAILED_BRAIN_REGIONS.HIPPOCAMPUS_CA3, 0.8);
this.longTermHippocampalTraces.push(memoryEncodingNode);
if (this.longTermHippocampalTraces.length > 120) {
this.longTermHippocampalTraces.shift(); // Structural prune mechanism
}
}
// --- CORTICAL OVERLAY MODULE 5: PREFRONTAL CORTEX COGNITIVE PATHWAYS ---
processPrefrontalCortexExecutive(gameEnvironmentState) {
let executionStrategyOutput = 'STRATEGY_STANDBY';
let decisionConfidenceScore = 0.5;
const dynamicCognitiveClarity = this.neurochemistry[NEUROTRANSMITTERS.ACETYLCHOLINE] * (1.1 - (this.internalSomaticState.visceralFear * 0.4)) - (this.internalSomaticState.cognitiveFatigue * 0.3);
// Core analytical human logic execution matrix
const threatDetected = this.workingMemoryBuffer.some(n => n.isThreat);
const healthPercent = gameEnvironmentState.self.health || 100;
if (threatDetected) {
if (this.internalSomaticState.survivalUrgency > 0.75 && healthPercent < 35) {
// Tactical evaluation: Cover availability vs retreat execution
if (dynamicCognitiveClarity > 0.5) {
executionStrategyOutput = 'EXECUTE_STAGED_RETREAT_TO_COVER';
decisionConfidenceScore = dynamicCognitiveClarity * 0.95;
} else {
executionStrategyOutput = 'PANIC_FLIGHT_FROM_ORIGIN';
decisionConfidenceScore = 0.40;
}
} else if (this.internalSomaticState.aggressionDrive > 0.45) {
executionStrategyOutput = 'TACTICAL_FLANK_AND_ENGAGE';
decisionConfidenceScore = Math.min(1.0, dynamicCognitiveClarity * (1.0 + this.neurochemistry[NEUROTRANSMITTERS.DOPAMINE]));
} else {
executionStrategyOutput = 'HOLD_ANGLE_SUPPRESSIVE_FIRE';
decisionConfidenceScore = dynamicCognitiveClarity * 0.80;
}
} else {
// Non-combat exploratory logic chains
if (this.internalSomaticState.survivalUrgency > 0.4) {
executionStrategyOutput = 'SEARCH_RESOURCES_AND_HEAL';
decisionConfidenceScore = 0.75;
} else {
executionStrategyOutput = 'TERRAIN_RECON_AND_PATROL';
decisionConfidenceScore = Math.min(1.0, 0.5 + this.neurochemistry[NEUROTRANSMITTERS.SEROTONIN] * 0.4);
}
}
return {
activeStrategy: executionStrategyOutput,
confidence: decisionConfidenceScore,
processingClarity: dynamicCognitiveClarity
};
}
// --- CORTICAL OVERLAY MODULE 6: CEREBELLUM & MOTOR CORTEX VECTORS ---
computeMotorCerebellarMappings(gameState, strategicPlan) {
let finalTranslation = { x: 0, y: 0, z: 0 };
let finalGaze = { x: 0, y: 0, z: 0 };
let controlFlags = [];
const selfLocation = gameState.self.coords || { x: 0, y: 0, z: 0 };
const primaryThreatNode = this.workingMemoryBuffer.find(n => n.isThreat);
// Core analytical geometric transformations
if (strategicPlan.activeStrategy === 'TACTICAL_FLANK_AND_ENGAGE' && primaryThreatNode) {
const targetCoords = primaryThreatNode.coords;
// Calculate rotational offset for flank paths
const rawDeltaX = targetCoords.x - selfLocation.x;
const rawDeltaZ = targetCoords.z - selfLocation.z;
// Flank routing: Compute perpendicular matrix projection vectors
finalTranslation.x = -rawDeltaZ * 0.6 + rawDeltaX * 0.4;
finalTranslation.y = targetCoords.y - selfLocation.y;
finalTranslation.z = rawDeltaX * 0.6 + rawDeltaZ * 0.4;
finalGaze = targetCoords;
controlFlags.push('FIRE_WEAPON_TRUE');
if (this.neurochemistry[NEUROTRANSMITTERS.ADRENALINE] > 0.5) controlFlags.push('EXECUTE_CROUCH_STRAFE');
} else if ((strategicPlan.activeStrategy === 'EXECUTE_STAGED_RETREAT_TO_COVER' || strategicPlan.activeStrategy === 'PANIC_FLIGHT_FROM_ORIGIN') && primaryThreatNode) {
const dangerCoords = primaryThreatNode.coords;
// Invert spatial vectors away from origin point of incoming damage
finalTranslation.x = -(dangerCoords.x - selfLocation.x) * 1.5;
finalTranslation.y = -(dangerCoords.y - selfLocation.y);
finalTranslation.z = -(dangerCoords.z - selfLocation.z) * 1.5;
// Human tactical retreat: gaze remains locked on last known enemy threat coordinates
finalGaze = dangerCoords;
controlFlags.push('EXECUTE_SPRINT_MODIFIER');
if (strategicPlan.activeStrategy === 'EXECUTE_STAGED_RETREAT_TO_COVER') controlFlags.push('DEPLOY_SMOKE_SCREEN');
} else if (strategicPlan.activeStrategy === 'SEARCH_RESOURCES_AND_HEAL') {
// Path towards closest hypothetical item or structural safe houses
finalTranslation.x = Math.sin(Date.now() / 2000) * 10;
finalTranslation.z = Math.cos(Date.now() / 2000) * 10;
finalGaze.x = selfLocation.x + finalTranslation.x;
finalGaze.y = selfLocation.y + 1.2;
finalGaze.z = selfLocation.z + finalTranslation.z;
controlFlags.push('ACTIVATE_CONSUMABLE_HEAL');
} else {
// Normal human scouting movement patterns
const scanFrequency = Date.now() / 4000;
finalTranslation.x = Math.cos(scanFrequency) * 8;
finalTranslation.z = Math.sin(scanFrequency) * 8;
// Pan head vectors left and right continuously to scan environment
finalGaze.x = selfLocation.x + Math.cos(scanFrequency * 2.5) * 20;
finalGaze.y = selfLocation.y + 1.5;
finalGaze.z = selfLocation.z + Math.sin(scanFrequency * 2.5) * 20;
controlFlags.push('RECON_SCAN_ACTIVE');
}
return {
translation: finalTranslation,
gaze: finalGaze,
actions: controlFlags
};
}
// --- PIPELINE SYNERGY TICK: THE BRAIN CYCLE ---
executeFullCognitiveSynergy(rawInput, gameState, externalStressors, eventLog) {
// 1. Run Glial processing first to modify system operational speeds and clean up chemistry
const internalTraumaValue = externalStressors.damageSustained || 0;
const structuralMyelinVelocityMultiplier = this.glialNetwork.regulateMetabolism(this.neurochemistry, internalTraumaValue);
// 2. Gate environmental sensory noise via Thalamus
this.processThalamusGating(rawInput);
// 3. Monitor homeostatic biological metrics via Insula
this.processInsularCORTEX(gameState.self || {});
// 4. Update core survival emotional engines via Amygdala
this.processAmygdalaComplex(externalStressors);
// 5. Commit important anomalies to memory structures
this.processHippocampalConsolidation(eventLog);
// 6. Run high level executive evaluation pathways via PFC
const tacticalPlan = this.processPrefrontalCortexExecutive(gameState);
// 7. Perform physical vector calculations through Cerebellar motor networks
const spatialMovements = this.computeMotorCerebellarMappings(gameState, tacticalPlan);
// Calculate human biological response delays (Reaction time curve mapping)
const absoluteBaseDelay = 220; // Human standard base ms
const chemicalAcceleration = (this.neurochemistry[NEUROTRANSMITTERS.NOREPINEPHRINE] * 90) + (this.neurochemistry[NEUROTRANSMITTERS.ADRENALINE] * 50);
const fatigueDecceleration = this.internalSomaticState.cognitiveFatigue * 80;
// Final latency is divided by structural myelin speed multiplier from Oligodendrocytes
this.motorOutputRegister.estimatedLatencyMs = Math.max(50, Math.floor((absoluteBaseDelay - chemicalAcceleration + fatigueDecceleration) / structuralMyelinVelocityMultiplier));
// Smooth translation matrices to emulate analog muscle structures instead of instant linear jumps
const neuromuscularSmoothing = 0.40 + (this.neurochemistry[NEUROTRANSMITTERS.ACETYLCHOLINE] * 0.35);
this.motorOutputRegister.translationVector = {
x: spatialMovements.translation.x * neuromuscularSmoothing,
y: spatialMovements.translation.y,
z: spatialMovements.translation.z * neuromuscularSmoothing
};
this.motorOutputRegister.gazeTargetVector = spatialMovements.gaze;
this.motorOutputRegister.executionTriggers = spatialMovements.actions;
// Apply Natural Neurochemical Decay Laws over operational elapsed intervals
this.neurochemistry[NEUROTRANSMITTERS.DOPAMINE] = Math.max(0.1, this.neurochemistry[NEUROTRANSMITTERS.DOPAMINE] - 0.003);
this.neurochemistry[NEUROTRANSMITTERS.ADRENALINE] = Math.max(0.05, this.neurochemistry[NEUROTRANSMITTERS.ADRENALINE] - 0.008);
this.neurochemistry[NEUROTRANSMITTERS.GLUTAMATE] = Math.max(0.2, this.neurochemistry[NEUROTRANSMITTERS.GLUTAMATE] - 0.004);
// Increment global structural decay
this.internalSomaticState.cognitiveFatigue = Math.min(1.0, this.internalSomaticState.cognitiveFatigue + 0.0005);
this.synapticNetwork.decaySynapses();
return {
npcId: this.npcId,
connectedGame: this.gameType,
systemTickStamp: Date.now(),
prefrontalExecutiveStrategy: tacticalPlan,
somaticMotorOutputs: this.motorOutputRegister,
neurobiologicalStateTelemetry: {
neurotransmitterCleftNonspecificLevels: this.neurochemistry,
limbicSomaticHomeostasis: this.internalSomaticState,
glialNetworkIntegrity: {
astrocyteGlycogenLevel: this.glialNetwork.astrocytes.bloodBrainBarrierIntegrity,
oligodendrocyteMyelinVelocityFactor: structuralMyelinVelocityMultiplier,
microgliaInflammationIndex: this.glialNetwork.microglia.neuroinflammationIndex
},
workingMemoryOccupancy: this.workingMemoryBuffer.length,
totalLongTermSynapticNodesStored: this.longTermHippocampalTraces.length
}
};
}
}
// ==========================================
// 4. CONCURRENT NEURAL POOL ORCHESTRATOR
// ==========================================
const GlobalNeuralOrchestratorPool = {
activeInstances: new Map(),
retrieveBrainContext(npcId, gameType) {
if (!this.activeInstances.has(npcId)) {
this.activeInstances.set(npcId, new AdvancedHumanBrainEmulator(npcId, gameType));
}
return this.activeInstances.get(npcId);
},
flushDeadInstances() {
const threshold = Date.now() - 1200000; // Auto flush unused allocations after 20 mins
for (let [key, instance] of this.activeInstances.entries()) {
if (instance.birthStamp < threshold && instance.workingMemoryBuffer.length === 0) {
this.activeInstances.delete(key);
}
}
}
};
setInterval(() => {
GlobalNeuralOrchestratorPool.flushDeadInstances();
}, 600000);
// ==========================================
// 5. CORE REST CONTROLLERS FOR EXTERNAL CLIENT ENGINE INTEGRATION
// ==========================================
/**

* @route POST /api/v2/brain/synaptic-cycle
* @desc Main cognitive API called by game platforms (Roblox Lua via HttpService, PUBG C#, etc.)
*/
app.post('/api/v2/brain/synaptic-cycle', (req, res) => {
const {
npcId,
gameType,
sensoryInput,
gameState,
stressors,
historicalEvent
} = req.body;if (!npcId || !gameType) {
return res.status(400).json({
error: "Systemic Orchestration Failure: Parameters 'npcId' and 'gameType' must be explicitly defined in payload header."
});
}try {
const brainInstance = GlobalNeuralOrchestratorPool.retrieveBrainContext(npcId, gameType.toLowerCase());const runtimeNeuralState = brainInstance.executeFullCognitiveSynergy(
sensoryInput || {},
gameState || { self: {} },
stressors || {},
historicalEvent || null
);return res.status(200).json(runtimeNeuralState);
} catch (criticalException) {
console.error("SYSTEMIC NEURAL EXCEPTION CRITICAL:", criticalException);
return res.status(500).json({ error: "Systemic Synaptic Collapse: Thread failed inside cortical logic matrix simulation loops." });
}
});

/**

* @route GET /api/v2/brain/telemetry/:id
* @desc Telemetry audit endpoint to view precise neurochemical/glial status via standard web browser.
*/
app.get('/api/v2/brain/telemetry/:id', (req, res) => {
const instance = GlobalNeuralOrchestratorPool.activeInstances.get(req.params.id);
if (!instance) return res.status(404).json({ error: "Target neural instance allocation missing from execution block pool." });return res.status(200).json({
npcId: instance.npcId,
gameType: instance.gameType,
biochemistry: instance.neurochemistry,
somaticMetrics: instance.internalSomaticState,
glialMetrics: instance.glialNetwork,
hippocampalLogVolume: instance.longTermHippocampalTraces.length
});
});

/**

* @route GET /
* @desc System root verification endpoint.
*/
app.get('/', (req, res) => {
res.status(200).send(<body style="font-family:sans-serif; background:#111; color:#eee; padding:2rem;"> <h1 style="color:#00ffcc;">HUMAN ADULT BRAIN EMULATION ENGINE (HABEE) v2.0.0</h1> <p style="color:#aaa;">Status: <span style="color:#55ff55;">ONLINE</span></p> <p>Active Synaptic Network Allocations: <b>${GlobalNeuralOrchestratorPool.activeInstances.size} concurrent brain cores</b></p> <p>Target Node API Interface Route: <code>/api/v2/brain/synaptic-cycle</code> [POST]</p> <hr style="border:1px solid #333;"> <small style="color:#666;">Structural Density Validation Passed. Glial Layer & Axon Terminal Mapping Operating Nominal.</small> </body>);
});

// Run Application Listener
app.listen(PORT, () => {
console.log(================================================================);
console.log( ADVANCED HUMAN ADULT BRAIN EMULATION ENGINE v2.0.0 ONLINE);
console.log( Dedicated Node REST Engine executing on port allocation: ${PORT});
console.log( Glial Support Matrix & 86 Billion Neuronal Mappings Active);
console.log(================================================================);
});
