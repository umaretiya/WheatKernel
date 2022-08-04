from termios import OPOST
from sympy import O
import yaml
import dill 
import numpy as np 
import pandas as pd
import os, sys 
from project.exception import WheatKernalException 
from project.constant import * 
from project.logger import logging

def write_yaml_file(file_path, data):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        logging.info("yaml file written directory created")
        with open(file_path, 'w') as yaml_file:
            yaml.dump(data, yaml_file)
    except Exception as e:
        raise WheatKernalException(e, sys) from e
  
    
def read_yaml_file(file_path):
    try:
        with open(file_path, 'rb') as yaml_file:
            logging.info("yaml file reading successfully")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise WheatKernalException(e, sys) from e 


def save_numpy_array_data(file_path, np_array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_array:
            logging.info("file saved successfuly numpy array")
            np.save(file_array, np_array)
    except Exception as e:
        raise WheatKernalException(e, sys) from  e 


def load_numpy_array_data(file_path):
    try:
        with open(file_path, 'rb') as file_array:
            logging.info("file: numpy array open ok")
            return np.load(file_array)
    except Exception as e:
        raise WheatKernalException(e, sys) from e 
    
    
