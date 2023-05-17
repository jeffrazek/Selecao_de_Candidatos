'''SELEÇÃO DE CANDIDATOS Á VAGA'''

#ESTA FUNÇÃO FORMATA AS NOTAS PARA eX_tX_pX_sX (X = AVALIAÇÃO DO CANDIDATO | E = ENTREVISTA | T = TESTE TEÓRICO | P = TESTE PRÁTICO | S = SOFT SKILLS)
def nota_formatada(nota_candidato):
    return str(f'e{nota_candidato[0]}_t{nota_candidato[1]}_p{nota_candidato[2]}_s{nota_candidato[3]}')

# ESTA FUNÇÃO BUSCA O CANDIDATO NA LISTA DE CANDIDATOS, COMPARA COM AS NOTAS NA LISTA DE NOTAS E GUARDA OS SELECIONADO EM OUTRA LISTA
def busca_candidato(notas_candidatos):
    candidatos_selecionados = []
    for i in range(len(notas_candidatos)):
        notas = notas_candidatos[i]
        selecionado = True
        for j in range(len(notas)):
            if notas[j] < nota_candidato[j]:
                selecionado = False
                break
        if selecionado:
            candidatos_selecionados.append(candidato_vaga[i])
    return candidatos_selecionados
    

#LISTA COM AS NOTAS OBTIDAS POR CADA CANDIDATO RESPECTIVAMENTE
nota_final_candidato = [
    (6, 8, 5, 1),
    (9, 6, 7, 8),
    (6, 8, 1, 0),
    (9, 7, 8, 10),
    (1, 7, 10, 10),
    (7, 1, 1, 6),
    (3, 8, 5, 2),
    (0, 2, 10, 9),
    (4, 6, 7, 4),
    (0, 7, 7, 0)
]

#LISTA COM OS CANDIDATOS
candidato_vaga = ['CAND_1' ,
            'CAND_2' ,
            'CAND_3' ,
            'CAND_4' ,
            'CAND_5' ,
            'CAND_6' ,
            'CAND_7' ,
            'CAND_8' ,
            'CAND_9' ,
            'CAND_10'
            ]

#LISTA VAZIA QUE RECEBERÁ AS NOTAS SOLICITADAS PELO USUÁRIO
nota_candidato = []
#TESTES QUE OS CANDIDATOS IRÃO FAZER
teste_candidato = ['Entrevista' , 'Teste Teórico' , 'Teste Prático' , 'Avaliação Soft Skills']

#LAÇO PARA PERCORRER OS TESTES E PERGUNTAR AO USUÁRIO QUE NOTA ELE DESEJA PARA CADA TESTE
for i in range(0 , 4):
    nota_candidato.append(int(input(f'Digite a nota para {teste_candidato[i]}: ')))

#LAÇO COM INFORMAÇÕES FINAIS ONDE MOSTRA AS NOTAS SOLICITADAS PELO USUÁRIO, VE QUAL CANDIDATO SE ENCAIXA E DEVOLVE O RESULTADO SE HÁ OU NÃO UM CLASSIFICADO
def infor():
    print('=-'*50)
    print(f'As notas solicitadas foram {nota_formatada(nota_candidato)}')
    candidatos_selecionados = busca_candidato(nota_final_candidato)
    if len(candidatos_selecionados) > 0:
        print(f'Os candidatos que foram selecionados são: {busca_candidato(nota_final_candidato)}.')
    else:
        print('Nenhum candidato foi selecionado com as notas solicitadas.')
    print('=-'*50)

#CHAMADO FINAL DA FUNÇÃO PARA EXECUÇÃO DO CÓDIGO
infor()