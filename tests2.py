import os
import configparser
from funcionarios_final import *
from penetras import gerar_penetras_dict

config = configparser.ConfigParser()
config.read_file(open("dl.cfg"))
BASE_PATH = config["BASE_PATH"]["ROOT"]
START_YEAR = 2020

def teste_ler_json_file():
    try:
        ler_json_file(2020, "json_vazio.json")
    except EmptyFileException as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    else:
        print("Tudo ok!!")


    

if __name__ == "__main__":
    teste_ler_json_file()
