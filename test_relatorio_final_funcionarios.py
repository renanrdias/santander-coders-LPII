import os
import configparser
from funcionarios_final import *
import pytest

config = configparser.ConfigParser()
config.read_file(open("dl.cfg"))
BASE_PATH = config["BASE_PATH"]["ROOT"]
START_YEAR = 2020

def test_relatorio_final_funcionarios():
    previous_year_argument = {"ID6": {
        "Nome": "Carolina Santos",
        "Idade": 29,
        "Cargo": "Analista de Recursos Humanos",
        "Salário": 4800.00,
        "Email": "carolina.santos@example.com",
        "Data de Admissão": "2020-08-18",
        "Subordinados": [""]
    }}

    argument = {"ID6": {
        "Nome": "Carolina Santos",
        "Idade": 29,
        "Cargo": "Gerente de Projetos",
        "Salário": 9000.00,
        "Email": "carolina.santos@example.com",
        "Data de Admissão": "2020-08-18",
        "Subordinados": ["ID11,ID14"],
    }}
    
    expected = {"ID6": {
        "Nome": "Carolina Santos",
        "Idade": 29,
        "Cargo": "Gerente de Projetos",
        "Salário": 9000.00,
        "Email": "carolina.santos@example.com",
        "Data de Admissão": "2020-08-18",
        "Subordinados": [
            "ID11", 
            "ID14"
        ],
        "Promoção": {
            "2022": "Gerente de Projetos"
        }
    }}
    actual = relatorio_final_funcionarios(2022, argument, previous_final_report=previous_year_argument)

    assert actual == expected, "Não corresponde ao resutado esperado"