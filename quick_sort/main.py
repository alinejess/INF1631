"""
- Pivô: o ÚLTIMO elemento do vetor.
- Partição: separa os demais elementos em dois vetores novos:
    L -> elementos MENORES OU IGUAIS ao pivô
    R -> elementos MAIORES que o pivô
- Resultado: quicksort(L) + [pivô] + quicksort(R)
"""


def particao(A):
    """
    Recebe um vetor A com pelo menos 2 elementos.
    Retorna (pivo, L, R), onde:
      - pivo é o último elemento de A;
      - L contém os elementos de A[0..n-2] que são <= pivo;
      - R contém os elementos de A[0..n-2] que são > pivo.
    """
    pivo = A[-1]   # escolhemos o último elemento como pivô
    L = []         # vai guardar os elementos <= pivô
    R = []         # vai guardar os elementos > pivô

    # Percorremos todos os elementos, EXCETO o pivô (último).
    # Cada elemento cai em exatamente um dos dois vetores.
    for x in A[:-1]:
        if x <= pivo:
            L.append(x)
        else:
            R.append(x)

    # Impressão pedida no enunciado, para cada chamada da partição
    print(f"A = {A}")
    print(f"Pivô = {pivo}")
    print(f"L = {L}   R = {R}")
    print()

    return pivo, L, R


def quicksort(A):
    """
    Retorna uma NOVA lista com os elementos de A em ordem crescente.
    """
    # Caso base: vetor com 0 ou 1 elemento já está ordenado.
    # Aqui a partição não é chamada.
    if len(A) <= 1:
        return A[:]

    # Passo recursivo: particiona e ordena cada lado separadamente.
    pivo, L, R = particao(A)
    L_ordenado = quicksort(L)
    R_ordenado = quicksort(R)

    # Junta: (menores ou iguais ordenados) + pivô + (maiores ordenados)
    return L_ordenado + [pivo] + R_ordenado


def testar(A):
    """Roda o quicksort em A mostrando o passo a passo e o resultado."""
    print("=" * 50)
    print(f"Vetor de entrada: {A}")
    print("=" * 50)
    resultado = quicksort(A)
    print(f"Vetor ordenado: {resultado}")
    print()


if __name__ == "__main__":
    # Vetor dado no enunciado
    testar([7, 3, 9, 2, 8, 1, 5, 4, 6])

    # Vetor escolhido com 15 elementos (tem um valor repetido, o 4,
    # para mostrar que elementos iguais ao pivô vão para L)
    testar([12, 4, 15, 7, 4, 10, 3, 14, 8, 2, 11, 6, 13, 5, 9])