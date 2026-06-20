import networkx as nx
import time
import pickle
import random
import statistics
import math

def analise_teorica_dijkstra():
    print("==========================================")
    print(" ANÁLISE TEÓRICA: DIJKSTRA (SINGLE-SOURCE)")
    print("==========================================")
    print("Complexidade de Tempo: O(E + V log V)")
    print(" - Onde V é o número de Vértices e E é o número de Arestas.")
    print(" - Utiliza uma Fila de Prioridade (Min-Heap) para extrair o nó mais próximo.")
    print("\nComplexidade de Espaço: O(V)")
    print(" - Armazena as distâncias para todos os V vértices e a Fila de Prioridade.\n")

def main():
    analise_teorica_dijkstra()
    
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
    print("-> Grafo carregado com sucesso!\n")

    # 2. Configurar a Amostragem
    n_execucoes = 30
    tempos_execucao = []
    
    print("Sorteando 30 vértices aleatórios como fontes (sources)...")
    lista_nos = list(G_tratado.nodes())
    raizes = random.sample(lista_nos, n_execucoes)

    # 3. Laço de Execução e Medição
    print("\nIniciando as execuções do Dijkstra (Single-Source)...")
    for i, raiz in enumerate(raizes):
        start_time = time.time()
        
        # Executando o Dijkstra para encontrar o tamanho do caminho para todos os nós alcançáveis.
        # Como o grafo original não tem a propriedade 'weight', o NetworkX assume peso 1 para todas as arestas.
        distancias = nx.single_source_dijkstra_path_length(G_tratado, source=raiz)
        
        end_time = time.time()
        duracao = end_time - start_time
        tempos_execucao.append(duracao)
        
        # Mostrando o progresso
        nos_alcancados = len(distancias)
        print(f"Execução {i+1:02d}/30 | Raiz (Source): {raiz:<8} | Alcançados: {nos_alcancados:<7} | Tempo: {duracao:.6f} s")

    # 4. Cálculos Estatísticos (Conforme a regra n >= 30)
    z_score = 1.96  
    
    media = statistics.mean(tempos_execucao)
    desvio_padrao = statistics.stdev(tempos_execucao)
    
    margem_erro = z_score * (desvio_padrao / math.sqrt(n_execucoes))
    
    limite_inferior = media - margem_erro
    limite_superior = media + margem_erro

    # 5. Exibição dos Resultados para o Relatório
    print("\n==========================================")
    print(" RESULTADOS ESTATÍSTICOS FINAIS")
    print("==========================================")
    print(f"Tamanho da Amostra (n): {n_execucoes}")
    print(f"Tempo Médio (x̄):        {media:.6f} segundos")
    print(f"Desvio Padrão (σ):      {desvio_padrao:.6f} segundos")
    print(f"Margem de Erro:       ± {margem_erro:.6f} segundos")
    print(f"Intervalo de Confiança: [{limite_inferior:.6f} s, {limite_superior:.6f} s] (95% de confiança)")
    print("==========================================")

if __name__ == "__main__":
    main()