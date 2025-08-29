def insertion_sort_com_contador(lista):
    comparacoes = 0

    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        
        while j >= 0 and chave < lista[j]:
            comparacoes += 1
            lista[j + 1] = lista[j]
            j -= 1
        
        if j >= -1:
             comparacoes +=1

        lista[j + 1] = chave
        
    return lista, comparacoes

lista_pior_caso = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
n = len(lista_pior_caso)

print(f"Lista original (pior caso): {lista_pior_caso}")
lista_ordenada, num_comparacoes = insertion_sort_com_contador(lista_pior_caso)
print(f"Lista ordenada: {lista_ordenada}")
print(f"Tamanho da lista (n): {n}")
print(f"Número de comparações: {num_comparacoes}")

print(f"Valor teórico aproximado (n*(n-1)/2): {n*(n-1)/2}")