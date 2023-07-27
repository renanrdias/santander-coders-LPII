from typing import List


def gerar_penetras_dict(lista_presentes:List[List], final_report:dict,) -> dict:
    """Reads in a 2-dimensional list and convert it to a dict.
    
    Args:
        lista_presentes (List): 2-dimensional list.
        final_report (dict): Dictionary that contains relevant data about employees.
    Return:
        dict
    """

    # colunas = lista_presentes[0][1:]
    festa_dict = {k: v for k, v in zip([idx[0] for idx in lista_presentes[1:]], \
                                       [*map(dict, [[*zip(lista_presentes[0][1:], entrada[1:])]\
                                                     for entrada in lista_presentes[1:]])])}
    
    penetra_dict = {e: festa_dict[e] for e in festa_dict if (e not in final_report) or (e in final_report and festa_dict[e]["Nome"] != final_report[e]["Nome"])}
    return penetra_dict



if __name__ == "__main__":
    pass



    
    