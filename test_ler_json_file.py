import os
import configparser
from funcionarios_final import *
import pytest

config = configparser.ConfigParser()
config.read_file(open("dl.cfg"))
BASE_PATH = config["BASE_PATH"]["ROOT"]
START_YEAR = 2020

def teste_ler_json_file_not_found():
    arguments = [2020, "abc.json"]
    with pytest.raises(FileNotFoundError) as exception_info:
        ler_json_file(arguments[0], arguments[1])
    assert exception_info.match(f"O arquivo {arguments[1]} não existe.")


def teste_ler_json_file_empty():
    arguments = [2020, "json_vazio.json"]
    with pytest.raises(EmptyFileException) as exception_info:
        ler_json_file(arguments[0], arguments[1])
    assert exception_info.match(f"O arquivo {arguments[1]} está vazio.")

def teste_ler_json_file_correct():
    arguments = [2020, "teste2020.json"]
    with open(f"{BASE_PATH}/{arguments[0]}/{arguments[1]}", "r") as file:
        arquivo = json.load(file)
    expected = arquivo
    actual = ler_json_file(arguments[0], arguments[1])
    assert actual == expected, "Os arquivos não são iguais"