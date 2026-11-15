# pip install pennylane
import pennylane as qml

# Simulador nativo
dev_nativo = qml.device("default.qubit", wires=2)

# pip install pennylane-qiskit
# Simulador do Qiskit
dev_qiskit = qml.device("qiskit.aer", wires=2)
