import pennylane as qml
import torch
import torch.nn as nn
from torch.optim import Adam

# ==========================================
# 1. Definição do Circuito Quântico
# ==========================================
n_qubits = 2
dev = qml.device("default.qubit", wires=n_qubits)


@qml.qnode(dev)
def circuito_vqc(inputs, weights):
    # Data Encoding: Mapeia as features para os qubits
    qml.AngleEmbedding(inputs, wires=range(n_qubits), rotation="Y")

    # Ansatz: Aplica as camadas parametrizadas de emaranhamento
    qml.BasicEntanglerLayers(weights, wires=range(n_qubits))

    # Medição: Retorna o valor esperado contínuo no intervalo [-1, 1]
    return qml.expval(qml.PauliZ(0))


# ==========================================
# 2. Encapsulamento em Arquitetura PyTorch
# ==========================================
n_camadas = 2
formato_pesos = {"weights": (n_camadas, n_qubits)}

# TorchLayer gerencia os batches e a compatibilidade de dados automaticamente
modelo = qml.qnn.TorchLayer(circuito_vqc, formato_pesos)


# ==========================================
# 3. Training Loop Clássico
# ==========================================
def treinar_vqc(X_treino, y_treino, epocas=50):
    otimizador = Adam(modelo.parameters(), lr=0.1)

    # Função de perda: MSE
    funcao_custo = nn.MSELoss()

    print("Iniciando o treino do modelo quântico...")
    for epoca in range(epocas):
        otimizador.zero_grad()

        # Forward pass: PyTorch envia o batch de dados para o PennyLane
        predicoes = modelo(X_treino)

        # Cálculo da perda
        perda = funcao_custo(predicoes, y_treino)

        # Backward pass: PennyLane calcula o gradiente nativamente
        perda.backward()

        # Atualização dos pesos do Ansatz
        otimizador.step()

        if (epoca + 1) % 10 == 0:
            print(f"Época {epoca + 1:03d} | Perda (MSE): {perda.item():.4f}")

    return modelo


# Exemplo de execução (com dados artificiais)
if __name__ == "__main__":
    # Geramos 20 amostras aleatórias.
    # Forçamos o dtype para float32 para alinhar com o padrão do PyTorch
    X_dummy = torch.rand((20, n_qubits), dtype=torch.float32)

    # Criamos rótulos artificiais (-1.0 ou 1.0) baseados na soma das features
    y_dummy = torch.where(torch.sum(X_dummy, dim=1) > 1.0, 1.0, -1.0)

    # Garantimos que os rótulos também estejam em float32 para a função de custo
    y_dummy = y_dummy.to(torch.float32)

    modelo_treinado = treinar_vqc(X_dummy, y_dummy)

“””
--- Exemplo de output ---

Iniciando o treino do modelo quântico...
Época 010 | Perda (MSE): 0.8167
Época 020 | Perda (MSE): 0.8120
Época 030 | Perda (MSE): 0.7970
Época 040 | Perda (MSE): 0.7920
Época 050 | Perda (MSE): 0.7920
“””
