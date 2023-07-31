import os
import glob
from configparser import ConfigParser
from exceptions import *

config = ConfigParser()
config.read_file(open("dl.cfg"))
BASE_PATH = config["BASE_PATH"]["ROOT"]


def check_available_years(year_folder:int) -> bool:
    """Read in the year that refers to a directory and check how many directories
        there are in the root within the century.
    Args:
        year_folder (int): The searched folders that belongs to a century.
    Returns:
        bool
    
    Raises:
        FolderDoesNotExists: It warns the user the folder years avaliable.
    """
    available_years = [int(year[:4]) for year in glob.glob("20*/", recursive=True)]
    if year_folder in available_years:
        return True 
    else:
        raise FolderDoesNotExists(f"Você pode gerar o relatório para os seguintes anos: {sorted(available_years)}")

def available_year():
    return sorted([int(year[:4]) for year in glob.glob("20*/", recursive=True)])

if __name__ == "__main__":
    pass
