import time
from simulator import QuantumSimulator

def run_bell_state_circuit():
    print("=== Running Quantum Circuit: Bell State Generation ===")
    
    start_time = time.perf_counter()
    
    # Initialize 2 Qubits Simulator
    sim = QuantumSimulator(num_qubits=2)
    mem_size = sim.state_vector.nbytes
    
    # Bell State Workflow
    sim.apply_H(target=0)           # Superposition on Qubit 0
    sim.apply_CNOT(control=0, target=1) # Entangle Qubit 0 and 1
    
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000

    probabilities = sim.get_probabilities()
    
    print("\nCircuit Execution Results:")
    for state, prob in probabilities.items():
        print(f"State {state} Probability: {prob * 100}%")
        
    print("\n=== Minimum Required KPI Report ===")
    print(f"• Execution Time      : {execution_time:.4f} ms")
    print(f"• State Vector Size   : {sim.state_size} elements ({mem_size} Bytes)")
    print(f"• Supported Qubits    : {sim.num_qubits}")
    print(f"• Probabilities Sum   : {sum(probabilities.values())}")

if __name__ == "__main__":
    run_bell_state_circuit()
