import numpy as np

class QuantumSimulator:
    def __init__(self, num_qubits):
        if num_qubits < 1 or num_qubits > 3:
            raise ValueError("Simulator optimized for 1-3 qubits.")
        self.num_qubits = num_qubits
        self.state_size = 2**num_qubits
        self.state_vector = np.zeros(self.state_size, dtype=complex)
        self.state_vector[0] = 1.0  # Initialize to state |0...0>

        # Base Gate Matrices
        self.I = np.eye(2, dtype=complex)
        self.X_gate = np.array([[0, 1], [1, 0]], dtype=complex)
        self.H_gate = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
        self.Z_gate = np.array([[1, 0], [0, -1]], dtype=complex)

    def _get_single_qubit_operator(self, gate, target_qubit):
        operator = 1
        for i in range(self.num_qubits):
            if i == target_qubit:
                operator = np.kron(operator, gate)
            else:
                operator = np.kron(operator, self.I)
        return operator

    def apply_X(self, target):
        op = self._get_single_qubit_operator(self.X_gate, target)
        self.state_vector = np.dot(op, self.state_vector)

    def apply_H(self, target):
        op = self._get_single_qubit_operator(self.H_gate, target)
        self.state_vector = np.dot(op, self.state_vector)

    def apply_Z(self, target):
        op = self._get_single_qubit_operator(self.Z_gate, target)
        self.state_vector = np.dot(op, self.state_vector)

    def apply_CNOT(self, control, target):
        cnot_matrix = np.eye(self.state_size, dtype=complex)
        for i in range(self.state_size):
            if (i >> (self.num_qubits - 1 - control)) & 1:
                target_mask = 1 << (self.num_qubits - 1 - target)
                flipped_index = i ^ target_mask
                cnot_matrix[i, i] = 0
                cnot_matrix[i, flipped_index] = 1
        self.state_vector = np.dot(cnot_matrix, self.state_vector)

    def get_probabilities(self):
        probabilities = np.abs(self.state_vector) ** 2
        result = {}
        for i in range(self.state_size):
            binary_state = format(i, f'0{self.num_qubits}b')
            result[f"|{binary_state}>"] = round(probabilities[i], 4)
        return result
