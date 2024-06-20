



def CriarMatriz():
    #Define a lista que conterá as linhas da matriz
    Matriz = []
    #Pede ao usuário o número de linhas que haverão na matriz
    N_linhas = int(input('Insira o total de linhas que a matriz terá:\n'))

    for i in range(N_linhas):
        #Pede ao usuário os elementos da linha
        elem = input('Insira os elementos da Matriz, separados por vírgula: \n')
        # Divide os elementos em uma lista nomeada de linha
        linha = [int(x) for x in elem.split(',')] 
        # Adiciona a lista chamada linha à matriz
        Matriz.append(linha)
    return Matriz