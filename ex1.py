import matrizlib

'''
Função que determina a simetria de uma matriz informada
Entradas: Matriz(LISTA FLOAT) / Saída: BOOL
'''
def simetrica(Matriz):

    # Verifica se a matriz é quadrada
    N_linhas = len(Matriz)
    
    for linha in Matriz:
        if len(linha) != N_linhas:
            return False
    
    # Confere se a matriz é equivalente à transposta
    for i in range(N_linhas):
        for j in range(N_linhas):
            if Matriz[i][j] != Matriz[j][i]:
               return False
            
    return True

def main():
    Matriz1 = matrizlib.CriarMatriz()    
    
    if simetrica(Matriz1):
        print('A matriz é simetrica')
    else:
        print('Não é')

        
main()        
    
    
        
    
