# Importando as bibliotecas necessárias
import pennylane as qml
import numpy as np


# Definimos as features e os pesos do Ansatz
features = np.array([0.1, 0.5, -0.2])

num_layers = 2
num_qubits = len(features)

# O formato dos pesos depende do template (num_layers, num_qubits)
# Aqui, criamos 2 camadas para 3 qubits
pesos = np.random.uniform(low=0, high=2 * np.pi, size=(num_layers, num_qubits))

dev = qml.device("default.qubit", wires=num_qubits)

@qml.qnode(dev)
def modelo_hibrido(x, theta):
    # 1. Data Encoding: S(x)
    qml.AngleEmbedding(features=x, wires=range(num_qubits), rotation="Y")

    # 2. Ansatz (Hardware-Efficient): U(theta)
    # Aplica rotações RX parametrizadas seguidas de um anel de portas CNOT
    qml.BasicEntanglerLayers(weights=theta, wires=range(num_qubits), rotation=qml.RX)

    # 3. Medição baseada no Hamiltoniano (Observável Pauli-Z no primeiro qubit)
    return qml.expval(qml.PauliZ(0))

resultado = modelo_hibrido(features, pesos)
print(f"Output do modelo (Valor Esperado): {resultado:.4f}")