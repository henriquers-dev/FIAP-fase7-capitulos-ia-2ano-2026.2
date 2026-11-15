# Importando as bibliotecas necessárias
import pennylane as qml
import numpy as np

# Vetor clássico com 4 features (requer log2(4) = 2 qubits)
x = np.array([1.5, 0.0, -2.1, 3.2])
n = int(np.log2(len(x)))

dev = qml.device("default.qubit", wires=n)

@qml.qnode(dev)
def amplitude_embedding(features):
    # Normalização é gerida pelo parâmetro normalize=True
    qml.AmplitudeEmbedding(features=features, wires=range(n), normalize=True)
    return qml.state()

print(amplitude_embedding(x))
"""
[ 0.36487819+0.j  0.        +0.j -0.51082947+0.j  0.77840681+0.j]
"""