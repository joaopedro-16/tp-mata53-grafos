import networkx as nx
import time
import pickle
import statistics
import math

def analise_teorica_mst():
    print("==========================================")
    print(" ANÁLISE TEÓRICA: ÁRVORE GERADORA MÍNIMA (KRUSKAL)")
    print("==========================================")
    print("Complexidade de Tempo: O(E log E) ou O(E log V)")
    print(" - O gargalo do algoritmo de Kruskal é a ordenação inicial de")
    print("   todas as arestas do grafo pelo seu peso.")
    print(" - O uso da estrutura Union-Find para evitar ciclos leva tempo quase linear.")
    print("\nComplexidade de Espaço: O(V + E)")
    print(" - Exige a conversão do grafo para não direcionado e o armazenamento")
    print("   das estruturas de conjuntos disjuntos (Union-Find).\n")

def main():
    analise_teorica_mst()
    
    print("==========================================")
    print(" EXECUÇÃO PRÁTICA E ESTATÍSTICA (n = 30)")
    print("==========================================\n")
    
    # 1. Carregar o Grafo Tratado
    print("Carregando 'grafo_tratado.pickle' da memória...")
    try:
        with open('grafo_tratado.pickle', 'rb') as f:
            G_tratado = pickle.load(f)
    except FileNotFoundError:
        print("ERRO: O arquivo 'grafo_tratado.pickle' não foi encontrado.")
        return
    print("-> Grafo direcionado carregado com sucesso!\n")

    # 2. Adaptação do Grafo (Requisito Teórico)
    print("Adaptando o grafo: Convertendo para Não Direcionado...")
    start_conversao = time.time()
    # A conversão é feita fora do laço de tempo para medir estritamente o Kruskal
    G_nao_direcionado = G_tratado.to_undirected()
    print(f"-> Conversão concluída em {time.time() - start_conversao:.2f} s.\n")

    # 3. Configurar a Amostragem
    n_execucoes = 30
    tempos_execucao = []
    
    # 4. Laço de Execução e Medição
    print(f"Iniciando as {n_execucoes} execuções de Kruskal... (Isso vai demorar um pouco)")
    for i in range(n_execucoes):
        start_time = time.time()
        
        # nx.minimum_spanning_tree usa Kruskal por padrão.
        # Como o grafo não tem o atributo 'weight', ele assume que todas as arestas têm peso 1.
        mst = nx.minimum_spanning_tree(G_nao_direcionado, algorithm='kruskal')
        
        end_time = time.time()
        duracao = end_time - start_time
        tempos_execucao.append(duracao)
        
        # Mostrar o progresso e confirmar que o tamanho da árvore está correto (V - 1 arestas)
        if i == 0:
            arestas_mst = mst.number_of_edges()
            vertices_mst = mst.number_of_nodes()
            
        print(f"Execução {i+1:02d}/30 | Tempo: {duracao:.4f} s")

    # 5. Cálculos Estatísticos (Conforme a regra n >= 30)
    z_score = 1.96  
    
    media = statistics.mean(tempos_execucao)
    desvio_padrao = statistics.stdev(tempos_execucao)
    
    margem_erro = z_score * (desvio_padrao / math.sqrt(n_execucoes))
    
    limite_inferior = media - margem_erro
    limite_superior = media + margem_erro

    # 6. Exibição dos Resultados para o Relatório
    print("\n==========================================")
    print(" RESULTADOS ESTRUTURAIS")
    print("==========================================")
    print(f"Vértices na MST: {vertices_mst}")
    print(f"Arestas na MST:  {arestas_mst} (Matematicamente deve ser V - 1)")
    
    print("\n==========================================")
    print(" RESULTADOS ESTATÍSTICOS DE TEMPO")
    print("==========================================")
    print(f"Tamanho da Amostra (n): {n_execucoes}")
    print(f"Tempo Médio (x̄):        {media:.4f} segundos")
    print(f"Desvio Padrão (σ):      {desvio_padrao:.4f} segundos")
    print(f"Margem de Erro:       ± {margem_erro:.4f} segundos")
    print(f"Intervalo de Confiança: [{limite_inferior:.4f} s, {limite_superior:.4f} s] (95% de confiança)")
    print("==========================================")

if __name__ == "__main__":
    main()