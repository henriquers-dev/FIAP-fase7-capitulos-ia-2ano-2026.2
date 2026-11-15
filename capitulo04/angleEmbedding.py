# Importando as bibliotecas necessárias
import pennylane as qml
import numpy as np


# Vetor clássico com 3 features
x = np.array([0.1, 0.5, -0.2])

n = len(x)
dev = qml.device("default.qubit", wires=n)

@qml.qnode(dev)
def angle_embedding(features):
    # Encoding das features utilizando rotações no eixo Y
    qml.AngleEmbedding(features=features, wires=range(n), rotation="Y")
    return qml.state()

print(angle_embedding(x))
"""
[ 0.96286706+0.j -0.09660895+0.j  0.24586032+0.j -0.02466831+0.j
  0.04818351+0.j -0.00483448+0.j  0.01230327+0.j -0.00123444+0.j]
"""
