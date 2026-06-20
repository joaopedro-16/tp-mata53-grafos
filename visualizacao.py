import networkx as nx
import matplotlib.pyplot as plt
import time
import pickle

def main():
    print("==========================================")
    print(" GERADOR DE VISUALIZAÇÃO REDUZIDA (EGO-NET)")
    print("==========================================\n")
    
    # ==========================================
    # PASSO 1: CARREGAR O GRAFO TRATADO
    # ==========================================
    print("Carregando o grafo tratado da memória (.pickle)...")
    start_time = time.time()
    
    try:
        with open('grafo_tratado.pickle', 'rb') as f:
            G_tratado = pickle.load(f)
    except FileNotFoundError:
        print("ERRO: Arquivo 'grafo_tratado.pickle' não encontrado.")
        print("Por favor, execute o script 'tratamento.py' primeiro.")
        return

    print(f"-> Grafo carregado em {time.time() - start_time:.2f} segundos.")
    
    # ==========================================
    # PASSO 2: EXTRAÇÃO DO SUBGRAFO
    # ==========================================
    print("\nIdentificando o maior Hub...")
    graus_entrada = dict(G_tratado.in_degree())
    maior_hub = max(graus_entrada, key=graus_entrada.get)
    print(f"-> Maior Hub encontrado: Nó {maior_hub} ({graus_entrada[maior_hub]} citações recebidas).")

    print("\nExtraindo subgrafo de vizinhos para visualização...")
    vizinhos = list(G_tratado.predecessors(maior_hub))[:60]
    nos_do_subgrafo = vizinhos + [maior_hub]
    subgrafo_reduzido = G_tratado.subgraph(nos_do_subgrafo).copy()

    # ==========================================
    # PASSO 3: RENDERIZAÇÃO DA IMAGEM
    # ==========================================
    print("\nCalculando posições físicas (Spring Layout)...")
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(subgrafo_reduzido, k=0.15, seed=42)

    cores_nos = ['#FF4500' if no == maior_hub else '#1E90FF' for no in subgrafo_reduzido.nodes()]
    tamanhos_nos = [400 if no == maior_hub else 60 for no in subgrafo_reduzido.nodes()]

    print("Desenhando elementos...")
    nx.draw_networkx_nodes(subgrafo_reduzido, pos, node_color=cores_nos, node_size=tamanhos_nos, alpha=0.9)
    nx.draw_networkx_edges(subgrafo_reduzido, pos, edge_color='#D3D3D3', arrows=True, arrowsize=10, width=0.8)

    labels = {maior_hub: f"HUB: {maior_hub}"}
    nx.draw_networkx_labels(subgrafo_reduzido, pos, labels, font_size=10, font_weight="bold")

    plt.title(f"Visualização Reduzida do Grafo: Rede de Ego ao redor do Maior Hub Tecnológico", fontsize=12)
    plt.axis('off')

    print("\nSalvando imagem final no disco...")
    plt.savefig("visualizacao_reduzida_grafo.png", dpi=300, bbox_inches='tight')
    print("-> Imagem 'visualizacao_reduzida_grafo.png' gerada com sucesso!")
    
    # Mostrar a imagem na tela
    plt.show()

if __name__ == "__main__":
    main()