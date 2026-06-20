import networkx as nx
import pickle
import time

def main():
    print("Carregando 'grafo_tratado.pickle' da memória...")
    start_time = time.time()
    
    try:
        with open('grafo_tratado.pickle', 'rb') as f:
            G_tratado = pickle.load(f)
    except FileNotFoundError:
        print("ERRO: O arquivo 'grafo_tratado.pickle' não foi encontrado.")
        return
        
    print(f"-> Grafo carregado em {time.time() - start_time:.2f} segundos.\n")
    
    print("Calculando os graus máximos e médios...")

    # 1. GRAU DE ENTRADA (In-Degree) - Citações Recebidas
    in_degrees = dict(G_tratado.in_degree())
    max_in_node = max(in_degrees, key=in_degrees.get)
    max_in_val = in_degrees[max_in_node]
    
    # 2. GRAU DE SAÍDA (Out-Degree) - Citações Feitas
    out_degrees = dict(G_tratado.out_degree())
    max_out_node = max(out_degrees, key=out_degrees.get)
    max_out_val = out_degrees[max_out_node]

    # 3. GRAU TOTAL (In + Out)
    total_degrees = dict(G_tratado.degree())
    max_total_node = max(total_degrees, key=total_degrees.get)
    max_total_val = total_degrees[max_total_node]
    
    # Exibição dos Resultados para copiar para a Tabela da Parte I
    print("\n==========================================")
    print(" RESULTADOS PARA A TABELA (PARTE I)")
    print("==========================================")
    print(f"Grau Máximo de Entrada (In-Degree):  {max_in_val} (Patente Hub: {max_in_node})")
    print(f"Grau Máximo de Saída (Out-Degree):   {max_out_val} (Patente que mais citou: {max_out_node})")
    print(f"Grau Máximo Absoluto (Total):        {max_total_val} (Patente: {max_total_node})")
    print("==========================================")
    
    print("\nDica para o relatório: O Grau Máximo que costuma importar na teoria de redes Scale-Free (Lei de Potência) é o Grau de Entrada, que identifica o grande Hub da rede.")

if __name__ == "__main__":
    main()