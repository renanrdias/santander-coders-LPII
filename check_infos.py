import os
import glob
from configparser import ConfigParser
from exceptions import *

config = ConfigParser()
config.read_file(open("dl.cfg"))
BASE_PATH = config["BASE_PATH"]["ROOT"]


def check_available_years(year_folder):
    available_years = [int(year[:4]) for year in glob.glob("20*/", recursive=True)]
    if year_folder in available_years:
        return True 
    else:
        raise FolderDoesNotExists(f"Você pode gerar o relatório para os seguintes anos: {sorted(available_years)}")
    
if __name__ == "__main__":
    pass
