import shutil
def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    nota_aluno = arquivo.read()
    #print(nota_aluno)
    nota_aluno =nota_aluno.split('\n')
    #print(nota_aluno)

    for x in nota_aluno:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas ]) / 4
        print(aluno, media(lista_notas))

def copiar_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/agnes/PycharmProjects/')

def mover_arquivo(nome_arquivo):
    shutil.move(nome_arquivo,'C:/Users/agnes/PycharmProjects/')

if __name__ == '__main__':
    mover_arquivo('notas.txt')
    #copiar_arquivo('notas.txt')
    #media_notas('notas.txt')
    # escrever_arquivo('Primeira linha.\n')
    #aluno = 'Cesar, 7, 9, 3, 8\n'
    #atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')