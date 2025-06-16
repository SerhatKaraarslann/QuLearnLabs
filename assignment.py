from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.quantum_info import Statevector


ent_circ = QuantumCircuit(3)  # Create a quantum circuit with 3 qubits 

ent_circ.h(0)  # Apply Hadamard gate to qubit 0, creating superposition, 1/sqrt(2) (|0> +  |1>)

ent_circ.cx(0, 1) # CNOT gate to entangle qubit 0 with qubit 1, creating entanglement between them
ent_circ.cx(0, 2)  # CNOT gate to entangle qubit 0 with qubit 2, creating entanglement between them


#This will give us the state of the qubits after applying the gates
state = Statevector.from_instruction(ent_circ)
print(state)


#Add measurements to all qubits
ent_circ.measure_all()

#Use the StatevectorSampler for Simulation
sampler = StatevectorSampler()


# Number of shots (although it's a statevector simulation, this is a common parameter)
shots = 1000
job = sampler.run([ent_circ],shots = shots)


#get the result of the job
result = job.result()[0]


#print the measurement bitstrings
print(result.data.meas.get_bitstrings())

#Print the counts of the each measurements outcome
counts = result.data.meas.get_counts()
print("\nCounts of measurement outcomes:")
print(counts)


#calculate and print the probabilities of each outcome
prob_dict = {state : c / shots for state, c in counts.items()}
print("\nProbabilities of measurement outcomes:")
print(prob_dict)


#draw the circuit
ent_circ.draw("mpl")
