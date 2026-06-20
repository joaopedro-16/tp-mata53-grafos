import networkx as nx
import pandas as pd
import time
import pickle

def main():
    print("==========================================")
    print(" INICIANDO PIPELINE DE TRATAMENTO DE DADOS")
    print("==========================================\n")
    
    # ==========================================
    # PASSO 1: CARREGAR OS DADOS
    # ==========================================
    print("[1/4] Carregando o arquivo bruto cit-Patents.txt...")
    start_time = time.time()

    df = pd.read_csv("cit-Patents.txt", sep='\t', comment='#', names=['FromNodeId', 'ToNodeId'], dtype=int)
    G = nx.from_pandas_edgelist(df, source='FromNodeId', target='ToNodeId', create_using=nx.DiGraph())

    print(f"      -> Grafo bruto carregado em {time.time() - start_time:.2f} segundos.")
    print(f"      -> Vértices originais: {G.number_of_nodes()}")
    print(f"      -> Arestas originais: {G.number_of_edges()}")

    # ==========================================
    # PASSO 2: REMOÇÃO DE AUTO-LOOPS
    # ==========================================
    print("\n[2/4] Removendo auto-loops...")
    G.remove_edges_from(nx.selfloop_edges(G))
    print("      -> Auto-loops removidos com sucesso.")

    # ==========================================
    # PASSO 3: EXTRAÇÃO DA MAIOR COMPONENTE (WCC)
    # ==========================================
    print("\n[3/4] Calculando a Maior Componente Fracamente Conexa (WCC)...")
    maior_wcc_nos = max(nx.weakly_connected_components(G), key=len)
    G_tratado = G.subgraph(maior_wcc_nos).copy()

    print(f"      -> Vértices no grafo tratado: {G_tratado.number_of_nodes()}")
    print(f"      -> Arestas no grafo tratado: {G_tratado.number_of_edges()}")

    # ==========================================
    # PASSO 4: EXPORTAÇÃO DO GRAFO TRATADO
    # ==========================================
    print("\n[4/4] Exportando o grafo tratado para arquivo binário (.pickle)...")
    export_start = time.time()
    
    with open('grafo_tratado.pickle', 'wb') as f:
        pickle.dump(G_tratado, f)
        
    print(f"      -> Arquivo 'grafo_tratado.pickle' gerado em {time.time() - export_start:.2f} segundos.")
    print("\n==========================================")
    print(" TRATAMENTO CONCLUÍDO COM SUCESSO!")
    print("==========================================")

if __name__ == "__main__":
    main()