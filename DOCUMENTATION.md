# Technical Report: Hybrid Quantum Circuit Simulator

## 1. Quantum State Representation & Gate Explanation
* [cite_start]**Qubit Storage & Superposison:** Quantum states are stored in a 1D complex-valued NumPy array (state vector) of size $2^n$[cite: 14, 15, 69]. [cite_start]Superposition is represented by the continuous probability amplitudes $\alpha$ and $\beta$ assigned to indices where $|\alpha|^2 + |\beta|^2 = 1$[cite: 18, 23, 24].
* [cite_start]**Probability Computation:** Probabilities are calculated by squaring the absolute magnitude of individual state amplitudes (`np.abs(state_vector) ** 2`)[cite: 19].
* **Gate Modification:** Quantum operations ($H$, $X$, $CNOT$) are calculated by applying matrix multiplications against the state vector[cite: 27, 29, 36]. Multi-qubit global operations are constructed via Kronecker tensor products.

## 2. Key Performance Indicators (KPIs) Discussion
* [cite_start]**State Vector Size:** The state vector size scales exponentially ($2^n$) relative to the qubit count ($n$)[cite: 68, 69]. [cite_start]This memory expansion is why simulating $>50$ qubits on classical computers becomes completely impossible[cite: 70].
* **Execution Time:** Every added qubit doubles matrix operation complexity, meaning gate execution runtime scales drastically over larger architectures[cite: 65, 66].
* [cite_start]**Probability Correctness:** Our Bell State circuit correctly returns exactly $50\%$ probability for $|00\rangle$ and $50\%$ probability for $|11\rangle$, maintaining valid mathematical normalization[cite: 53, 57, 63].

## 3. Hardware and FPGA Discussion
* [cite_start]**Parallelism Opportunities:** The underlying mechanics of this simulator revolve around matrix-vector dot products[cite: 74]. [cite_start]On FPGA hardware, these multiplications can be executed completely in parallel utilizing concurrent DSP-slice-backed MAC units[cite: 75, 78].
* [cite_start]**Fixed-Point vs Floating-Point:** Relying on floating-point arithmetic uses a massive amount of logical cell area on FPGAs[cite: 76, 78]. [cite_start]Moving to custom fixed-point fractional registers scales down resource allocation but introduces subtle mathematical precision errors[cite: 78].
* [cite_start]**Memory Bottleneck:** Because state spaces scale exponentially ($2^n$), standard on-chip BRAM blocks will act as a system bottleneck long before compute hardware bounds are maxed out[cite: 73, 79].
