from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import math

# Initialise quantum circuit
grover_circ = QuantumCircuit(4)

#All qubits in superposition
grover_circ.h([0, 1, 2, 3])

# Grover's algorithm iterations
for _ in range(int(math.pi)): # formel is π/4*sqrt(N) where N = pow(2,4) 
# Oracle für |0010⟩
    grover_circ.x([3,2,0])  
    grover_circ.h(3)
    grover_circ.mcx([0,1,2], 3)
    grover_circ.h(3)
    grover_circ.x([3,2,0])  
    
    # Diffusion
    grover_circ.h([0,1,2,3])
    grover_circ.x([0,1,2,3])
    grover_circ.h(3)
    grover_circ.mcx([0,1,2], 3)
    grover_circ.h(3)
    grover_circ.x([0,1,2,3])
    grover_circ.h([0,1,2,3])


# check final state before measurement
state = Statevector(grover_circ)
print("Finaler Zustand:", state)

# Measure all qubits
grover_circ.measure_all()

shots = 1000
result = StatevectorSampler().run([grover_circ], shots = shots).result()

counts = result[0].data.meas.get_counts()
print("\nCounts of measurement outcomes:" + str(counts))

for p,c in counts.items():
    print(f"Probability of {p}: {c/shots:.4f}")

pro_dict = {state: c / shots for state, c in counts.items()}

plot_histogram({state: c / shots for state, c in counts.items()},title="Probabilities of Measurement Outcomes")

grover_circ.draw('mpl')
