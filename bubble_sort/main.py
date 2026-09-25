"""
Bubble Sort - Estruturas Discretas
Ordena um vetor de inteiros em ordem crescente.

A cada iteração do laço externo, percorremos a parte que ainda
não ordenada do vetor comparando os vizinhos e trocando os que estão 
fora de ordem. Dessa forma, o maior elemento dessa parte "borbulha" 
até o fim dela.
"""


def bubble_sort(A):
    """
    Ordena a lista A in-place (modifica a própria lista) e a retorna.
    Imprime o estado do vetor antes de começar e ao final de cada
    iteração do laço externo.
    """
    n = len(A)

    # Estado inicial do vetor
    print(f"A(0) = {A}")

    # Laço externo: i = 0, 1, ..., n-2  (n-1 iterações)
    # Invariante (no início da iteração i):
    #   as últimas i posições, A[n-i..n-1], contêm os i maiores
    #   elementos do vetor, já em ordem crescente.
    for i in range(n - 1):

        # Laço interno: compara pares vizinhos A[j] e A[j+1]
        # apenas na parte ainda não ordenada, A[0..n-1-i].
        for j in range(n - 1 - i):
            if A[j] > A[j + 1]:
                # Estão fora de ordem -> troca
                A[j], A[j + 1] = A[j + 1], A[j]

        # Ao fim da iteração i, o maior elemento de A[0..n-1-i]
        # está na posição n-1-i.
        print(f"A({i + 1}) = {A}")

    return A


def testar(A):
    """Roda o bubble sort em uma cópia de A e mostra o resultado."""
    print("=" * 50)
    print(f"Vetor de entrada: {A}")
    print("=" * 50)
    resultado = bubble_sort(A[:])   # cópia, para não alterar o original
    print(f"Vetor ordenado: {resultado}")
    print()


if __name__ == "__main__":
    # Vetor dado no enunciado
    testar([7, 3, 9, 2, 8, 1, 5, 4, 6])

    # Vetor escolhido com 15 elementos (mesmo usado no Quicksort)
    testar([12, 4, 15, 7, 4, 10, 3, 14, 8, 2, 11, 6, 13, 5, 9])