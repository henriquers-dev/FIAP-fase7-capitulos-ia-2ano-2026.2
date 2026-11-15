import numpy as np
import matplotlib.pyplot as plt
import pennylane as qml

dev = qml.device("default.qubit", wires=1)


# Definindo QNode
@qml.qnode(dev)
def circuito_parametrizado(theta):
    qml.RX(theta, wires=0)

    # Podemos retornar múltiplos tipos de medição
    return qml.expval(qml.PauliZ(wires=0)), qml.probs(wires=0)


theta = np.pi / 4
valor_esperado, probabilidades = circuito_parametrizado(theta)

print(f"Expectation Value: {valor_esperado:.4f}")
# Expectation Value: 0.7071

print(f"Probabilidades: {probabilidades}")
# Probabilidades: [0.85355339 0.14644661]

# Figura 1
print(qml.draw(circuito_parametrizado)(theta))

# Figura 2
qml.draw_mpl(circuito_parametrizado)(theta)
plt.show()
