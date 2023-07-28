from copy import deepcopy
from typing import List
import os
import json
import configparser
import csv
from exceptions import EmptyFileException

config = configparser.ConfigParser()
config.read_file(open("dl.cfg"))
BASE_PATH = config["BASE_PATH"]["ROOT"]


def ler_csv(year:int, input_file_name:str, check_file_size:bool=True) -> List[List]:
    """Read a csv file and returns a list of lists. The first inner list contains the columns or attributes.

    Args:
        year (int): The year that data refers to.
        input_file_name (str): The name of the csv file to be read.

    Returns:
        List[List]
    """

    if input_file_name == "":
        return None
    else:
        input_file_path = BASE_PATH+f"/{year}/{input_file_name}"
        if not os.path.isfile(input_file_path):
            raise FileNotFoundError(f"O arquivo {input_file_name} não existe.")
        with open(input_file_path, "r", encoding="UTF-8") as file:
            arquivo = list(csv.reader(file, delimiter=",", lineterminator="\n"))
        if check_file_size:
            if len(arquivo) > 0:
                return arquivo
            else:
                raise EmptyFileException(f"O arquivo {input_file_name} está vazio.")
        else:
            return None
    
    # if input_file_name != "":
    #     input_file_path = BASE_PATH+f"/{year}/{input_file_name}"
    #     try:
    #         assert os.path.isfile(input_file_path) is True
    #     except:
    #         print(f"O arquivo {input_file_name} não existe.")
    #     else:
    #         try:
    #             with open(f"{input_file_path}", "r", encoding="UTF-8") as file:
    #                 arquivo = list(csv.reader(file, delimiter=",", lineterminator="\n"))
    #                 assert len(arquivo) > 0
    #         except:
    #             print(f"O arquivo {input_file_name} está vazio")
    #         else:
    #             return arquivo
    #         #  print(arquivo)
    # else:
    #     return None

def gerar_admissoes_dict(lista_admissoes:List[List]) -> dict:
    """Reads in a list of lists. The first list contains attributes and the rest ones have the data.
        Returns a dictionary.
    Args:
        lista_admissoes (list): A list of lists, or matrix. The first list contains the attributes and the other ones have the data.
    
    Returns:
        dict
    """

    colunas = lista_admissoes[0][1:]
    admissoes_dict = {}
    for info in lista_admissoes[1:]:
        lista_pares = [(k, v) if k != "Subordinados" else (k, v.split(",")) for k,v in zip(colunas, info[1:])]
        admissoes_dict.update({info[0]:dict(lista_pares)})

    return admissoes_dict

def gerar_demissoes_dict(lista_demissoes:List[List]=None) -> dict:
    """Writes a json file with output_file_name on corresponding year folder.

    Args:
        output_file_file (str): Name of the file with json extension.
        year (int): Corresponding year of the data. It will be used to write the json file in the corresponding folder.
        lista_demissoes (list): A list with the data.

    Returns:
        None
    """

    colunas = lista_demissoes[0][1:]
    for e in lista_demissoes[1:]:
        teste_demissoes = [(k, v) for k, v in zip(colunas, e[1:])]
    return {key[0]: dict(teste_demissoes) for key in lista_demissoes[1:]}


def ler_json_file(year: int,file_name:str) -> dict:
    """Read in a json file and parses it into a dictionary.
    
    Args:
        file_name (str): Json file path to be read in and parsed into a dictionary.
    
    Returns:
        dict
    """
    if not os.path.isfile(f"{BASE_PATH}/{year}/{file_name}"):
        raise FileNotFoundError(f"O arquivo {file_name} não existe.")
    else:
        with open(f"{BASE_PATH}/{year}/{file_name}", "r") as file:
            f = file.readlines()
        if len(f) <= 0:
            raise EmptyFileException(f"O arquivo {file_name} está vazio.")
        else:
            with open(f"{BASE_PATH}/{year}/{file_name}", "r") as file:
                arquivo = json.load(file)
        return arquivo
    
    # try:
    #     with open(f"{BASE_PATH}/{year}/{file_name}", "r") as file:
    #         arquivo = json.load(file)
    # except:
    #     print(f"O arquivo {file_name} não existe.")
    # else:
    #     return arquivo

def escrever_json_file(year:int, output_file_name:str, to_write_json:dict) -> None:
    """Takes a dictionary and writes it as a json file
    
    Args:
        year (int): It will be used to determine the path of the file to be written in.
        output_file_name (str): the name of the file with .json extention.
        to_write_json (dict): A dictionary to be parsed and written as a json file.
    
    Returns:
        None
    """
    
    try:
        with open(f"{BASE_PATH}/{year}/{output_file_name}", "w") as file:
            json.dump(to_write_json, file, indent=4, ensure_ascii=False)
    except:
        print(f"Não foi possível salvar o arquivo {output_file_name}")
    else:
        print(f"Arquivo {output_file_name} foi gerado com sucesso!")

def relatorio_final_funcionarios(year:int, previous_final_report:dict, current_admissions_dict:dict, current_layoff_dict:dict=None) -> dict:
    """Returns the final employees report based on the previous' year final report.
    
    Args:
        year (int): The year the report will refer to.
        previous_final_report (dict): Previous year employee final report
        current_admissions_dict (dict): The current year admissions.
        current_layoff_dict (dict, optional): The current year layoff, if any.
    
    Returns:
        dict
    """
    
    current_admissions_cp = deepcopy(current_admissions_dict)
    if current_layoff_dict is not None: current_layoff_cp = deepcopy(current_layoff_dict)
    if previous_final_report is not None: previous_final_report_cp = deepcopy(previous_final_report)

    for key in current_admissions_cp:
            if key in previous_final_report_cp:
                previous_final_report_cp[key]["Cargo"] = current_admissions_cp[key]["Cargo"]
                previous_final_report_cp[key]["Salário"] = current_admissions_cp[key]["Salário"]
                previous_final_report_cp[key]["Promoção"] = {f"{year}": current_admissions_cp[key]["Cargo"]} # pegamos somente o ano da promoção
                
                # atualizamos a lista de subordinados, desconsiderando caracteres "" quando o funcionário promovido ganha subordinados.
                previous_final_report_cp[key]["Subordinados"] = [*[ sub for sub in previous_final_report_cp[key]["Subordinados"] if sub != ""], \
                                                              *[i for i in current_admissions_cp[key]["Subordinados"] \
                                                                if i not in previous_final_report_cp[key]["Subordinados"] and i != ""]]\
                                                                if previous_final_report_cp[key]["Subordinados"] != current_admissions_cp[key]["Subordinados"]\
                                                                else previous_final_report_cp[key]["Subordinados"]
            else:
                previous_final_report_cp.update({key: current_admissions_cp[key]})
    
    # Retirar as demissões se existirem
    if current_layoff_dict is not None:
        for key in current_layoff_cp:
            previous_final_report_cp.pop(key)
    
    return previous_final_report_cp
    # escrever_json_file(year, output_file_name, previous_final_report)
    
    # try:
    #     current_admissions_cp = deepcopy(current_admissions_dict)
    #     current_layoff_cp = deepcopy(current_layoff_dict)
    # except:
    #     print("Ocorreu um erro com a cópia dos dicionários.")    
    # else:
    #     # Existe keys em comum no relatorio final do ano anterior e admissoes do ano corrente? Sim -> Promocao // Nao -> Somente acrescentar
    #     # TODO DONE: Atualizar o salário
    #     # TODO DONE: Atualizar os subordinados se for o caso
    #     for key in current_admissions_cp:
    #         if key in previous_final_report:
    #             previous_final_report[key]["Cargo"] = current_admissions_cp[key]["Cargo"]
    #             previous_final_report[key]["Salário"] = current_admissions_cp[key]["Salário"]
    #             previous_final_report[key]["Promoção"] = {f"{year}": current_admissions_cp[key]["Cargo"]} # pegamos somente o ano da promoção
                
    #             # atualizamos a lista de subordinados, desconsiderando caracteres "" quando o funcionário promovido ganha subordinados.
    #             previous_final_report[key]["Subordinados"] = [*[ sub for sub in previous_final_report[key]["Subordinados"] if sub != ""], \
    #                                                           *[i for i in current_admissions_cp[key]["Subordinados"] \
    #                                                             if i not in previous_final_report[key]["Subordinados"] and i != ""]]\
    #                                                             if previous_final_report[key]["Subordinados"] != current_admissions_cp[key]["Subordinados"]\
    #                                                             else previous_final_report[key]["Subordinados"]
    #         else:
    #             previous_final_report[key] = current_admissions_cp[key]
                
    #     # Retirar as demissões se existirem
    #     if current_layoff_dict is not None:
    #         for key in current_layoff_cp:
    #             previous_final_report.pop(key)
            
        # escrever_json_file(year, output_file_name, previous_final_report)
        

if __name__ == "__main__":
    pass