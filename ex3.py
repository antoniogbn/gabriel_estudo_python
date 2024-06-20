import matrizlib
'''
Função que executa a média de uma coluna especificada
MATRIZ -> FLOAT
'''
def MedCol(Col):
    N_linhas = len(Col)
    N_colunas = len(Col[0])
    # Pede a coluna desejada ao usuário
    ColunaD = int(input('Insira a coluna desejada'))
    # Lista que contém as colunas desejadas
    Colunas_importantes = []
    
    #separação das colunas desejadas
    for i in range(N_linhas):
        Colunas_importantes.append(Col[i][ColunaD])
        
    #Cálculo da média
    media = sum(Colunas_importantes)/N_colunas

    return media
    

def main():
    Matriz = matrizlib.CriarMatriz()
    MediaF = MedCol(Matriz)
    print(f'A média das colunas é {MediaF:.2f}')

main()
    
        
            
