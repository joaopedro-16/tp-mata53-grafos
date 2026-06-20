import networkx as nx
import time
import pickle
import random
import statistics
import math

def analise_teorica_bfs():
    print("==========================================")
    print(" ANÁLISE TEÓRICA: BUSCA EM LARGURA (BFS)")
    print("==========================================")
    print("Complexidade de Tempo: O(V + E)")
    print(" - Onde V é o número de Vértices e E é o número de Arestas.")
    print(" - O algoritmo visita cada vértice inserido na fila exatamente uma vez e")
    print("   inspeciona todas as suas arestas de saída para encontrar novos vizinhos.")
    print("\nComplexidade de Espaço: O(V)")
    print(" - No pior caso, a fila e o conjunto de vértices visitados armazenarão")
    print("   todos os nós do grafo, consumindo memória proporcional a V.\n")

def main():
    analise_teorica_bfs()
    
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
    
    # Sorteando 30 nós aleatórios como ponto de partida (Raiz)
    # Convertendo os nós para lista (isso usa um pouco de RAM, mas é seguro nos seus 16GB)
    print("Sorteando 30 vértices aleatórios como raízes para a BFS...")
    lista_nos = list(G_tratado.nodes())
    raizes = random.sample(lista_nos, n_execucoes)

    # 3. Laço de Execução e Medição
    print("\nIniciando as execuções da BFS...")
    for i, raiz in enumerate(raizes):
        start_time = time.time()
        
        # Executando a BFS nativa do NetworkX
        # O list() força o iterador a percorrer todo o caminho, simulando o custo real
        arestas_bfs = list(nx.bfs_edges(G_tratado, source=raiz))
        
        end_time = time.time()
        duracao = end_time - start_time
        tempos_execucao.append(duracao)
        
        # Mostrando o progresso
        nos_visitados = len(arestas_bfs) + 1 if arestas_bfs else 1
        print(f"Execução {i+1:02d}/30 | Raiz: {raiz:<8} | Visitados: {nos_visitados:<7} | Tempo: {duracao:.6f} s")

    # 4. Cálculos Estatísticos (Conforme a regra n >= 30)
    # Z-score para 95% de Nível de Confiança (alfa = 0.05 -> Z_alfa/2 = 1.96)
    z_score = 1.96  
    
    media = statistics.mean(tempos_execucao)
    desvio_padrao = statistics.stdev(tempos_execucao)
    
    # Fórmula: IC = Z * (sigma / sqrt(n))
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