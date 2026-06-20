import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

def plotar_lei_potencia(G_tratado):
    # Pega apenas os graus de entrada (citações recebidas)
    graus_entrada = [grau for _, grau in G_tratado.in_degree() if grau > 0]
    
    # Conta a frequência de cada grau
    contagem_graus = Counter(graus_entrada)
    k_valores = np.array(list(contagem_graus.keys()))
    p_k_valores = np.array(list(contagem_graus.values())) / len(graus_entrada) # P(k)
    
    # Plota em escala Log-Log
    plt.figure(figsize=(8, 6))
    plt.scatter(k_valores, p_k_valores, color='blue', alpha=0.5, marker='.')
    plt.xscale('log')
    plt.yscale('log')
    
    plt.title("Distribuição de Graus de Entrada (Escala Log-Log)")
    plt.xlabel("Grau de Entrada (k)")
    plt.ylabel("Probabilidade P(k)")
    plt.grid(True, which="both", ls="--", alpha=0.2)
    plt.savefig("lei_potencia.png")
    print("Gráfico 'lei_potencia.png' gerado! A reta descendente prova a Lei de Potência.")

# plotar_lei_potencia(G_tratado)