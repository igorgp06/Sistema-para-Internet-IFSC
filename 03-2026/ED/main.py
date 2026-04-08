# import numpy as np TODO: corrigir erro de importação


def pegar_medias():
    

    medias = []
    for i in range(5):
        print("Escreva 'n' para sair.")
        media = float(input(f"Digite a média do aluno {i + 1}: "))

        if media == 'n':
            break

        if media < 0 or media > 10:
            print("Média inválida. Digite uma média entre 0 e 10.")
            return pegar_medias()
        
        medias.append(media)
    return medias

# busca linear (em vetores não ordenados)

def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i  # encontrou
    return -1  # retornar elemento não encontrado


# pesquisa binária (em vetores ordenados)

def busca_binaria(lista, alvo):

    pegar_medias.medias = pegar_medias()




    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        
        if lista[meio] == alvo:
            return meio  # encontrou
        elif lista[meio] < alvo:
            baixo = meio + 1  # metade direita
        else:
            alto = meio - 1  # metade esquerda
            
    return -1  # retornar elemento não encontrado

minha_lista = [1, 3, 5, 7, 9, 11]
alvo = 7
resultado = busca_binaria(minha_lista, alvo)
print(f"Índice do elemento: {resultado}") # Saída: 3

