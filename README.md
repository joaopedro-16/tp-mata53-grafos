# Trabalho Prático - Teoria dos Grafos

Este diretório contém os códigos desenvolvidos para o trabalho prático da disciplina MATA53 - Teoria dos Grafos.

## Requisitos

Certifique-se de ter o Python (versão 3.6 ou superior) instalado em sua máquina.
As bibliotecas necessárias para a execução dos scripts podem ser instaladas utilizando o gerenciador de pacotes `pip`. 

Abra o terminal na pasta onde os códigos estão (por exemplo, `trabalho-pratico/code/`) e execute:

```bash
pip install networkx pandas matplotlib numpy scipy
```

## Como Executar

### Passo 1: Preparação da Base de Dados
O projeto utiliza a base de dados de citações de patentes **cit-Patents.txt**. 
Como o arquivo é muito grande para ser hospedado no GitHub, você deve baixá-lo no site oficial do SNAP (Stanford Network Analysis Project):
[https://snap.stanford.edu/data/cit-Patents.html](https://snap.stanford.edu/data/cit-Patents.html)

Após o download (e extração, se necessário), certifique-se de que o arquivo `cit-Patents.txt` está presente na mesma pasta que os arquivos Python.

### Passo 2: Tratamento e Processamento Inicial dos Dados
O primeiro script a ser executado **DEVE** ser o `tratamento.py`. 
Ele é responsável por:
- Ler o arquivo `.txt` original.
- Remover eventuais auto-loops.
- Encontrar e extrair a Maior Componente Fracamente Conexa (WCC).
- Exportar e salvar a estrutura de dados otimizada em um arquivo binário chamado `grafo_tratado.pickle`.

> **Importante:** Assim como a base de dados original, o arquivo `grafo_tratado.pickle` também é muito pesado e **não está no repositório**. Portanto, executar o `tratamento.py` é uma etapa obrigatória para que esse arquivo seja gerado localmente na sua máquina antes de rodar os demais scripts.

Para executá-lo, digite no terminal:
```bash
python tratamento.py
```
> **Aviso:** Este passo é pesado. Pode demorar alguns minutos e consumirá uma quantidade considerável de memória RAM durante o carregamento. Aguarde a mensagem final "TRATAMENTO CONCLUÍDO COM SUCESSO!".

### Passo 3: Execução dos Algoritmos e Medições
Uma vez gerado o arquivo `grafo_tratado.pickle`, os demais algoritmos rodarão de forma muito mais rápida, carregando o grafo pré-processado da memória. Você pode rodar qualquer um deles de forma independente.

Eles realizam simulações (geralmente executando repetidas vezes com amostras aleatórias) e calculam intervalos de confiança e tempos médios.

Comandos para executar cada algoritmo:

- **Busca em Largura (BFS):**
  ```bash
  python algoritmo_bfs.py
  ```

- **Busca em Profundidade (DFS):**
  ```bash
  python algoritmo_dfs.py
  ```

- **Algoritmo de Dijkstra (Caminhos Mínimos):**
  ```bash
  python algoritmo_dijkstra.py
  ```

- **Árvore Geradora Mínima (MST):**
  ```bash
  python algoritmo_mst.py
  ```

- **Verificação de Caminho/Ciclo Euleriano:**
  ```bash
  python algoritmo_euleriano.py
  ```

- **Componentes Fortemente Conexas (Algoritmo de Tarjan):**
  ```bash
  python algoritmo_tarjan.py
  ```

### Outras Análises e Visualizações

Além dos algoritmos, há scripts voltados para análise da rede, geração de métricas e plotagem de gráficos:

- **Análise do fenômeno de Redes de "Mundo Pequeno" (Small World):**
  ```bash
  python analise_small_world.py
  ```

- **Cálculo de Grau Máximo (e listagem de vértices de maior grau):**
  ```bash
  python calculo_grau_maximo.py
  ```

- **Comprovação da Lei de Potência (Gera o gráfico `lei_potencia.png`):**
  ```bash
  python plotar_lei_potencia.py
  ```

- **Geração de Visualização do Grafo (Gera imagem do grafo):**
  ```bash
  python visualizacao.py
  ```

---
**Observação**: Os tempos de execução, margens de erro e detalhes de complexidade teórica serão exibidos diretamente no console (terminal) ao final da execução de cada um dos scripts.
