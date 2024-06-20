import matrizlib
'''
Função que define a pior volta dada,e a volta em questão
MATRIZ -> TUPLA
'''
def Pior_volta(M):
    pior_tempo = -1
    pior_volta = -1
    pior_corredor = -1
    
    for corredor in range(len(M)):
        for volta in range(len(M[corredor])):
            if M[corredor][volta] > pior_tempo:
                pior_tempo = M[corredor][volta]
                pior_corredor = corredor
                pior_volta = volta

    return (pior_corredor,pior_tempo,pior_volta)

def main():
    matriz = matrizlib.CriarMatriz()
    corredor, tempo, volta = Pior_volta(matriz)
    print (f'A pior volta foi dada pelo corredor {corredor}, com {tempo:.1f} segundos na {volta} volta')

main()
