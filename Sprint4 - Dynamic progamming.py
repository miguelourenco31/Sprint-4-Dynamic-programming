import random
import time #Para comparar o tempo da versão recursiva e iterativa

# --- Classe para representar um insumo ---
class Insumo:
    def __init__(self, nome, quantidade_consumida, validade):
        self.nome = nome
        self.quantidade_consumida = quantidade_consumida
        self.validade = validade

    def __repr__(self):
        return f"Insumo(Nome: {self.nome}, Consumo: {self.quantidade_consumida}, Validade: {self.validade})"


# --- Simulação de dados de consumo diário ---
def simular_consumo(num_dias):
    insumos_disponiveis = [
        "Reagente A", "Tubo de Ensaio", "Luvas Cirúrgicas",
        "Algodão", "Swab", "Máscara N95", "Placa de Petri"
    ]
    consumo_diario = []

    for dia in range(num_dias):
        nome_insumo = random.choice(insumos_disponiveis)
        quantidade = random.randint(10, 100)
        validade_ano = 2026 + random.randint(0, 3)
        validade_mes = random.randint(1, 12)
        validade_str = f"{validade_mes:02d}/{validade_ano}"

        consumo_diario.append(Insumo(nome_insumo, quantidade, validade_str))

    return consumo_diario


# --- Estruturas de Dados: Fila e Pilha ---

def registrar_consumo_fila(consumos):
    fila_consumo = []
    for insumo in consumos:
        fila_consumo.append(insumo)
    return fila_consumo


def registrar_consumo_pilha(consumos):
    pilha_consumo = []
    for insumo in consumos:
        pilha_consumo.append(insumo)
    return pilha_consumo


# --- Algoritmos de Busca ---

def busca_sequencial(lista, nome_insumo):
    for i, insumo in enumerate(lista):
        if insumo.nome == nome_insumo:
            return f"Busca Sequencial: Encontrado '{nome_insumo}' na posição {i}."
    return f"Busca Sequencial: '{nome_insumo}' não encontrado."


def busca_binaria(lista, nome_insumo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio].nome == nome_insumo:
            return f"Busca Binária: Encontrado '{nome_insumo}' na posição {meio}."
        elif lista[meio].nome < nome_insumo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return f"Busca Binária: '{nome_insumo}' não encontrado."


# --- Algoritmos de Ordenação ---

def merge_sort(lista, chave):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda, chave)
        merge_sort(direita, chave)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if getattr(esquerda[i], chave) < getattr(direita[j], chave):
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1
    return lista


def quick_sort(lista, chave):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[len(lista) // 2]
        menores = [x for x in lista if getattr(x, chave) < getattr(pivo, chave)]
        iguais = [x for x in lista if getattr(x, chave) == getattr(pivo, chave)]
        maiores = [x for x in lista if getattr(x, chave) > getattr(pivo, chave)]

        return quick_sort(menores, chave) + iguais + quick_sort(maiores, chave)


# --- Programação Dinâmica ---

def prever_estoque_recursivo(dia, estoque, consumo, custo_reposicao, custo_falta, memo, max_estoque=100):
    """Versão recursiva com memoização - retorna custo mínimo a partir do estado (dia, estoque)."""
    if dia == len(consumo):
        return 0  # fim dos dias

    key = (dia, estoque)
    if key in memo:
        return memo[key]

    # Decisão 1: não repor hoje
    novo_estoque = max(0, estoque - consumo[dia])
    custo_sem_repor = (custo_falta if novo_estoque == 0 else 0) + prever_estoque_recursivo(
        dia + 1, novo_estoque, consumo, custo_reposicao, custo_falta, memo, max_estoque
    )

    # Decisão 2: repor (comprar até max_estoque)
    estoque_reposto = max_estoque
    # após repor, consome do mesmo dia
    novo_apos_repor = max(0, estoque_reposto - consumo[dia])
    custo_com_repor = custo_reposicao + prever_estoque_recursivo(
        dia + 1, novo_apos_repor, consumo, custo_reposicao, custo_falta, memo, max_estoque
    )

    melhor_custo = min(custo_sem_repor, custo_com_repor)
    memo[key] = melhor_custo
    return melhor_custo


def prever_estoque_iterativo(consumo, custo_reposicao, custo_falta, max_estoque=100, estoque_inicial=50):
    dias = len(consumo)
    dp = [[float('inf')] * (max_estoque + 1) for _ in range(dias + 1)]
    # custo 0 no dia final para qualquer estoque
    for s in range(max_estoque + 1):
        dp[dias][s] = 0

    for dia in range(dias - 1, -1, -1):
        for estoque in range(max_estoque + 1):
            # não repor
            novo_estoque = max(0, estoque - consumo[dia])
            custo_sem_repor = (custo_falta if novo_estoque == 0 else 0) + dp[dia + 1][novo_estoque]

            # repor até max_estoque
            estoque_reposto = max_estoque
            novo_apos_repor = max(0, estoque_reposto - consumo[dia])
            custo_com_repor = custo_reposicao + dp[dia + 1][novo_apos_repor]

            dp[dia][estoque] = min(custo_sem_repor, custo_com_repor)

    return dp[0][estoque_inicial]


# --- Execução do Programa ---
if __name__ == "__main__":
    print("Iniciando simulação do Totem Inteligente de Estoque...\n")

    # 1. Simular e Registrar Consumo
    consumo_diario = simular_consumo(10)
    print("Simulação de consumo (10 dias) realizada.")
    print("Amostra dos insumos simulados:")
    for ins in consumo_diario[:5]:
        print(" ", ins)
    print("... (total dias simulados:", len(consumo_diario), ")\n")

    # Fila (ordem de chegada)
    fila = registrar_consumo_fila(consumo_diario)
    print("--- Registro de Consumo (Fila - ordem cronológica) ---")
    print(fila, "\n")

    # Pilha (para consulta inversa)
    pilha = registrar_consumo_pilha(consumo_diario)
    print("--- Consulta de Últimos Consumos (Pilha - ordem inversa) ---")
    while pilha:
        item = pilha.pop()
        print(item)
    print("\nPilha esvaziada.\n")

    # 2. Ordenar os Dados
    print("--- Ordenando Dados ---")
    lista_para_ordenar = list(consumo_diario)

    lista_ordenada_consumo = merge_sort(list(lista_para_ordenar), 'quantidade_consumida')
    print("\nLista ordenada por quantidade consumida (Merge Sort):")
    for insumo in lista_ordenada_consumo:
        print(insumo)

    lista_ordenada_nome = quick_sort(list(lista_para_ordenar), 'nome')
    print("\nLista ordenada por nome (Quick Sort):")
    for insumo in lista_ordenada_nome:
        print(insumo)

    # 3. Buscar um Insumo
    print("\n--- Buscando um Insumo ---")
    nome_procurado = "Algodão"
    print(busca_sequencial(consumo_diario, nome_procurado))
    print(busca_binaria(lista_ordenada_nome, nome_procurado))

    # --- 4. Programação Dinâmica para prever reposição ---
    print("\n--- Programação Dinâmica ---")
    consumo = [i.quantidade_consumida for i in consumo_diario]
    custo_reposicao = 50
    custo_falta = 100
    memo = {}

    inicio = time.time()
    resultado_rec = prever_estoque_recursivo(0, 50, consumo, custo_reposicao, custo_falta, memo)
    fim = time.time()
    print(f"Versão recursiva: Custo mínimo = {resultado_rec} (tempo {fim-inicio:.4f}s)")

    inicio2 = time.time()
    resultado_iter = prever_estoque_iterativo(consumo, custo_reposicao, custo_falta)
    fim2 = time.time()
    print(f"Versão iterativa: Custo mínimo = {resultado_iter} (tempo {fim2-inicio2:.4f}s)")

    print("\nSimulação finalizada.")



