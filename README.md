# Sprint-4-Dynamic-programming
- Integrantes
Lorenzzo Vendruscolo Dias - RM558305 
Gabriel Martins Vannucci - RM556883 
Miguel Marques Lourenço - RM555426 
Pedro Henrique Ferronato - RM554757 
Athos Rodrigues Alves - RM:555515

Este projeto simula um sistema de controle de estoque utilizando um “totem inteligente”. O código permite registrar consumos de insumos, realizar buscas e ordenações, e prever reposições futuras utilizando programação dinâmica. A ideia principal é fornecer uma visão estratégica sobre o gerenciamento de materiais, útil para laboratórios, hospitais ou qualquer ambiente que dependa de controle de insumos. O Problema em muitas unidades de saúde, como o registro manual do consumo de insumos (como reagentes e descartáveis) não é preciso, o que dificulta o controle de estoque e a previsão de reposição. Este código oferece uma solução simples e didática para organizar esses dados de forma eficiente.

O projeto é implementado em Python e utiliza conceitos como:

- Estruturas de dados: fila e pilha
- Algoritmos de busca: sequencial e binária
- Algoritmos de ordenação: Merge Sort e Quick Sort
- Programação dinâmica: previsão de reposição de estoque
- Simulação de consumo diário de insumos

Funcionalidades

- Simulação de Consumo
Gera insumos aleatórios consumidos diariamente.
Cada insumo possui: nome, quantidade consumida e validade.

- Registro de Consumo
Fila: registra os consumos na ordem cronológica.
Pilha: permite consultar os últimos consumos de forma inversa.

- Ordenação
Merge Sort: ordena os insumos por quantidade consumida.
Quick Sort: ordena os insumos por nome.

- Busca de Insumos
Busca Sequencial: procura insumos na lista original.
Busca Binária: procura insumos na lista ordenada por nome.

- Previsão de Estoque (Programação Dinâmica)
Calcula o custo mínimo de reposição considerando:
Estoque atual
Consumo diário
Custo de reposição
Custo de falta

- Implementações:
Versão recursiva com memoização
Versão iterativa baseada em tabela

Como executar:
- Clone o repositório ou copie o código para sua máquina.
- Certifique-se de ter Python 3 instalado.
-Execute o script: python totem_estoque.py

- O programa irá:
Simular 10 dias de consumo de insumos
Registrar e exibir consumos em fila e pilha
Ordenar os insumos por quantidade e por nome
Realizar buscas de um insumo específico
Calcular a previsão de reposição de estoque usando programação dinâmica

- Estrutura do Código
class Insumo: representa cada insumo com nome, quantidade consumida e validade.
Funções de simulação: simular_consumo(num_dias)
Estruturas de dados: registrar_consumo_fila e registrar_consumo_pilha
Algoritmos de busca: busca_sequencial e busca_binaria
Algoritmos de ordenação: merge_sort e quick_sort
Programação dinâmica: prever_estoque_recursivo e prever_estoque_iterativo
Execução principal: bloco if __name__ == "__main__": realiza toda a simulação e exibição de resultados
