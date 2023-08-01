from typing import List
from funcionarios_final import *
import configparser
import glob

config = configparser.ConfigParser()
config.read_file(open("dl.cfg"))
BASE_PATH = config["BASE_PATH"]["ROOT"]

def gerar_penetras_dict(lista_presentes:List[List], final_report:dict,) -> dict:
    """Reads in a 2-dimensional list and convert it to a dict.
    
    Args:
        lista_presentes (List): 2-dimensional list.
        final_report (dict): Dictionary that contains relevant data about employees.
    Return:
        dict
    """
    
    # Excluir Histórico de Promoção de cada lista
    lista_presentes = [l[:3] for l in lista_presentes]
    
    festa_dict = {e[0]: dict(*map(dict,[zip(lista_presentes[0][1:], e[1:])])) for e in lista_presentes[1:]}
    
    penetra_dict = {e: festa_dict[e] for e in festa_dict if (e not in final_report) or (e in final_report and festa_dict[e]["Nome"] != final_report[e]["Nome"])}
    
    return penetra_dict





if __name__ == "__main__":    
    pass