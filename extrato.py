



def extrato_anual(ano:int, arquivo_admissoes:dict, arquivo_penetras:dict, arquivo_funcionarios:dict=None, arquivo_demissoes:dict=None) -> None:
   

    if arquivo_funcionarios is None:
        quantidade_funcionarios = len(arquivo_admissoes.keys())        
    else:
        quantidade_funcionarios = len(arquivo_funcionarios.keys())
        
    
    if arquivo_demissoes is None:
        quantidade_demissoes = "Não houve!"
    else:
        quantidade_demissoes = len(arquivo_demissoes)
    
    # if ano == 2020:
    #     quantidade_demissoes = arquivo_demissoes

    # else: 
    #     quantidade_demissoes = len(arquivo_demissoes.keys())
    
    # quantidade_admissoes = len(arquivo_admissoes.keys())
    # quantidade_funcionarios = len(arquivo_funcionarios.keys())
    quantidade_admissoes = len(arquivo_admissoes.keys())
    quantidade_penetras =  len(arquivo_penetras.keys())
    
    print('============================')
    print(f'Relatório anual de {ano}: ')
    print('============================')
    print(f'Quantidade de funcionários: {quantidade_funcionarios} \n')
    print(f'Quantidade de admissões: {quantidade_admissoes} \n')
    print(f'Quantidade de demissões: {quantidade_demissoes} \n')
    print(f'Quantidade de penetras: {quantidade_penetras} \n')
