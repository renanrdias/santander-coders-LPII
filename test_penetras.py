import os
import configparser
from funcionarios_final import *
from penetras import *
import pytest

config = configparser.ConfigParser()
config.read_file(open("dl.cfg"))
BASE_PATH = config["BASE_PATH"]["ROOT"]
START_YEAR = 2020

def test_gerar_penetras_dict():
    argument_1 = ler_csv(START_YEAR, "festa.csv")
    argument_2 = ler_json_file(START_YEAR, "ff2020_2.json")

    actual = gerar_penetras_dict(argument_1, argument_2)
    expected = ler_json_file(START_YEAR, f"penetras_festa_2020.json")

    assert actual == expected, "VALOR DIVERGENTE"


if __name__ == "__main__":
    pass