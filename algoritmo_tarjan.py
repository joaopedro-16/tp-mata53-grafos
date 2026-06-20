import networkx as nx
import time
import pickle
import statistics
import math

def analise_teorica_tarjan():
    print("==========================================")
    print(" ANÁLISE TEÓRICA: ALGORITMO DE TARJAN (SCC)")
    print("==========================================")
    print("Complexidade de Tempo: O(V + E)")
    print(" - O algoritmo realiza uma única travessia em profundidade (DFS)")
    print("   global, visitando cada vértice e explorando cada aresta exatamente uma vez.")
    print("\nComplexidade de Espaço: O(V)")
    print(" - Exige estruturas de dados auxiliares proporcionais ao número de vértices,")
    print("   como arrays para 'low-link values', IDs de descoberta e a pilha de execução.\n")

def main():
    analise_teorica_tarjan()
    
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
    # Tarjan é um algoritmo de varredura global, não utiliza nós raízes aleatórios.
    n_execucoes = 30
    tempos_execucao = []
    tamanho_maior_scc = 0
    total_sccs = 0
    
    # 3. Laço de Execução e Medição
    print(f"Iniciando as {n_execucoes} execuções globais de Tarjan... (Isso pode demorar vários minutos)")
    for i in range(n_execucoes):
        start_time = time.time()
        
        # nx.strongly_connected_components usa Tarjan/Nuutila por baixo dos panos
        # O list() força o gerador a processar todos os nós
        sccs = list(nx.strongly_connected_components(G_tratado))
        
        end_time = time.time()
        duracao = end_time - start_time
        tempos_execucao.append(duracao)
        
        # Coletar estatísticas estruturais apenas na primeira iteração (já que o grafo não muda)
        if i == 0:
            total_sccs = len(sccs)
            tamanho_maior_scc = len(max(sccs, key=len))
            
        print(f"Execução {i+1:02d}/30 | Tempo: {duracao:.4f} s")

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
    print(" RESULTADOS ESTRUTURAIS (O que Tarjan encontrou)")
    print("==========================================")
    print(f"Total de Componentes Fortemente Conexas (SCCs): {total_sccs}")
    print(f"Tamanho da Maior SCC encontrada: {tamanho_maior_scc} nó(s)")
    if tamanho_maior_scc == 1:
        print("-> Conclusão: O grafo é um DAG (Grafo Acíclico Dirigido). Sem ciclos temporais.")
        
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