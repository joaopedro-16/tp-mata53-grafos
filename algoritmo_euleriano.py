import networkx as nx
import time
import pickle
import statistics
import math

def analise_teorica_eulerianidade():
    print("==========================================")
    print(" ANÁLISE TEÓRICA: VERIFICAÇÃO DE EULERIANIDADE")
    print("==========================================")
    print("Complexidade de Tempo: O(V) no melhor caso, O(V + E) no pior.")
    print(" - O algoritmo primeiro verifica se o grau de entrada é igual ao")
    print("   grau de saída para todos os vértices (O(V)).")
    print(" - Se a verificação de graus falhar, ele retorna False imediatamente.")
    print(" - Só faz a travessia O(V + E) se a regra dos graus for satisfeita.")
    print("\nComplexidade de Espaço: O(V)")
    print(" - Consumo básico para manter dicionários de graus ou filas caso")
    print("   precise verificar componentes fortemente conexas.\n")

def main():
    analise_teorica_eulerianidade()
    
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
    # Para a eulerianidade não sorteamos raízes, pois a checagem é global no grafo inteiro.
    n_execucoes = 30
    tempos_execucao = []
    
    # 3. Laço de Execução e Medição
    print(f"Iniciando as {n_execucoes} execuções de verificação (nx.is_eulerian)...")
    for i in range(n_execucoes):
        start_time = time.time()
        
        # Executa a verificação. Vai retornar um booleano (True ou False)
        resultado = nx.is_eulerian(G_tratado)
        
        end_time = time.time()
        duracao = end_time - start_time
        tempos_execucao.append(duracao)
        
        # Mostrando o progresso
        print(f"Execução {i+1:02d}/30 | Resultado: {str(resultado):<5} | Tempo: {duracao:.6f} s")

    # 4. Cálculos Estatísticos (Conforme a regra n >= 30)
    # Z-score para 95% de Nível de Confiança (alfa = 0.05 -> Z_alfa/2 = 1.96)
    z_score = 1.96  
    
    media = statistics.mean(tempos_execucao)
    
    # Prevenção caso o algoritmo seja TÃO rápido que a variação de tempo seja nula para o processador
    try:
        desvio_padrao = statistics.stdev(tempos_execucao)
    except statistics.StatisticsError:
        desvio_padrao = 0.0
        
    # Fórmula: IC = Z * (sigma / sqrt(n))
    margem_erro = z_score * (desvio_padrao / math.sqrt(n_execucoes))
    
    limite_inferior = media - margem_erro
    limite_superior = media + margem_erro

    # 5. Exibição dos Resultados para o Relatório
    print("\n==========================================")
    print(" RESULTADOS ESTATÍSTICOS FINAIS")
    print("==========================================")
    print(f"É um Grafo Euleriano?   {resultado}")
    print(f"Tamanho da Amostra (n): {n_execucoes}")
    print(f"Tempo Médio (x̄):        {media:.6f} segundos")
    print(f"Desvio Padrão (σ):      {desvio_padrao:.6f} segundos")
    print(f"Margem de Erro:       ± {margem_erro:.6f} segundos")
    print(f"Intervalo de Confiança: [{limite_inferior:.6f} s, {limite_superior:.6f} s] (95% de confiança)")
    print("==========================================")

if __name__ == "__main__":
    main()