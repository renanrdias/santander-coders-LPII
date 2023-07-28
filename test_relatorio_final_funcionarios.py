import os
import configparser
from funcionarios_final import *
import pytest

config = configparser.ConfigParser()
config.read_file(open("dl.cfg"))
BASE_PATH = config["BASE_PATH"]["ROOT"]
START_YEAR = 2020

def test_relatorio_final_funcionarios():
    pass