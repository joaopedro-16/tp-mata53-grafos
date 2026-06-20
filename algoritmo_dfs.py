import networkx as nx
import time
import pickle
import random
import statistics
import math

def analise_teorica_dfs():
    print("==========================================")
    print(" ANÁLISE TEÓRICA: BUSCA EM PROFUNDIDADE (DFS)")
    print("==========================================")
    print("Complexidade de Tempo: O(V + E)")
    print(" - Onde V é o número de Vértices e E é o número de Arestas.")
    print(" - O algoritmo visita cada vértice e explora o caminho mais longo")
    print("   possível antes de retroceder (backtracking).")
    print("\nComplexidade de Espaço: O(V)")
    print(" - No pior caso (um grafo em formato de linha reta), a Pilha de")
    print("   recursão ou Pilha explícita armazenará todos os nós, consumindo O(V).\n")

def main():
    analise_teorica_dfs()
    
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
    
    # Sorteando 30 nós aleatórios usando uma seed fixa (opcional) para reprodutibilidade
    # Se quiser testar exatamente as mesmas raízes da BFS, você pode salvar a lista da BFS num txt
    print("Sorteando 30 vértices aleatórios como raízes para a DFS...")
    lista_nos = list(G_tratado.nodes())
    raizes = random.sample(lista_nos, n_execucoes)

    # 3. Laço de Execução e Medição
    print("\nIniciando as execuções da DFS...")
    for i, raiz in enumerate(raizes):
        start_time = time.time()
        
        # Executando a DFS nativa do NetworkX
        # O list() força o iterador a percorrer todo o ramo até o fim
        arestas_dfs = list(nx.dfs_edges(G_tratado, source=raiz))
        
        end_time = time.time()
        duracao = end_time - start_time
        tempos_execucao.append(duracao)
        
        # Mostrando o progresso
        nos_visitados = len(arestas_dfs) + 1 if arestas_dfs else 1
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