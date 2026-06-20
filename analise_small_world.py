import math

def analise_small_world(N, k_medio, L_real, C_real):
    print("=== ANÁLISE DE SMALL-WORLD (Implementação Matemática) ===")
    
    # 1. Cálculos do Grafo Aleatório Equivalente (Erdős-Rényi)
    C_rand = k_medio / N
    L_rand = math.log(N) / math.log(k_medio)
    
    print(f"1. Coeficiente de Clusterização (C):")
    print(f"   - Rede Real C(G):     {C_real:.6f}")
    print(f"   - Rede Aleatória:     {C_rand:.8f}")
    print(f"   - Razão (C_real / C_rand): {C_real / C_rand:.0f} vezes maior.")
    
    print(f"\n2. Comprimento Médio dos Caminhos (L):")
    print(f"   - Rede Real L(G) (Aprox.): {L_real:.2f}")
    print(f"   - Rede Aleatória:          {L_rand:.2f}")
    
    print("\nCONCLUSÃO FORMAL:")
    if (C_real > C_rand * 10) and (math.isclose(L_real, L_rand, rel_tol=0.5)):
        print("-> A rede POSSUI a propriedade de Small-World.")
        print("   C(G) >> C_rand e L(G) é comparável a L_rand.")

# Usando os dados que já conhecemos do dataset SNAP:
analise_small_world(N=3764117, k_medio=4.38, L_real=9.4, C_real=0.0757)